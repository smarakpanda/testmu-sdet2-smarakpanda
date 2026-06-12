import pytest
from playwright.sync_api import sync_playwright
from config.config import get_value_from_config
from utils.browser_factory import launch_browser


@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session", params=["chromium", "firefox", "webkit"])
def browser_2(playwright, request):
    browser_name = request.param

    # optional override from .env (if you still want single browser mode)
    config_browser = get_value_from_config("BROWSERS")
    if config_browser and config_browser != "all":
        if browser_name != config_browser:
            pytest.skip(f"Skipping {browser_name} (config restricted to {config_browser})")

    headless = get_value_from_config("headless").lower() == "true"
    print(f"\nLaunching browser: {browser_name}")
    browser = launch_browser(playwright, browser_name, headless)

    yield browser
    browser.close()


@pytest.fixture(scope="session")
def browser(playwright):
    browser_name = get_value_from_config("BROWSERS")
    headless = get_value_from_config("headless").lower() == "true"

    browser = launch_browser(playwright, browser_name, headless)

    yield browser
    browser.close()


@pytest.fixture(scope="function")
def page(browser,request):
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True)
    page = context.new_page()
    page.goto(get_value_from_config("AMAZON_URL"))
    yield page
    test_name = request.node.name
    context.tracing.stop(path=f"traces/{test_name}_{browser.browser_type.name}.zip")
    context.close()