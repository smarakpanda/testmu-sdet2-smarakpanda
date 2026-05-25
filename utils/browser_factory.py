def launch_browser(playwright, browser_name, headless):
    if browser_name.lower() == "chromium":
        return playwright.chromium.launch(headless=headless)

    elif browser_name.lower() == "firefox":
        return playwright.firefox.launch(headless=headless)

    elif browser_name.lower() == "webkit":
        return playwright.webkit.launch(headless=headless)

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")