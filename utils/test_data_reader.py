import json
from pathlib import Path
from typing import Any, Dict

from utils.decorators import log_decorator

@log_decorator
def get_login_data(env: str) -> Dict[str, Any]:
    """Return login data for the requested environment.
    Looks for test data in the package-relative path
    `playwright-framework/test_data/ui/login.json` by default. Can be
    overridden with the environment variable `TEST_DATA_DIR` which should
    point to the directory containing the `ui/login.json` file.
    """
    # Resolve path relative to this module so tests work from any CWD
    # By default the reader loads the project's packaged test data
    base = Path(__file__).resolve().parent.parent
    filepath = base / "test_data" / "ui" / "login.json"

    if not filepath.exists():
        raise FileNotFoundError(f"Login data file not found at: {filepath}")

    try:
        with filepath.open() as file:
            data = json.load(file)
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse JSON file {filepath}: {e}") from e

    if env not in data:
        raise ValueError(
            f"Environment '{env}' not found in login data file {filepath}. "
            f"Available environments: {list(data.keys())}"
        )

    return data[env]

@log_decorator
def get_user_data_api(env: str) -> Dict[str, Any]:
    """Return user data for the requested environment.
    Looks for test data in the package-relative path
    `playwright-framework/test_data/api/user.json` by default.
    can be overridden with filepath
    """
    # Resolve path relative to this module so tests work from any CWD
    # By default the reader loads the project's packaged test data
    base = Path(__file__).resolve().parent.parent
    filepath = base / "test_data" / "api" / "user.json"

    if not filepath.exists():
        raise FileNotFoundError(f"Login data file not found at: {filepath}")

    try:
        with filepath.open() as file:
            data = json.load(file)
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse JSON file {filepath}: {e}") from e

    if env not in data:
        raise ValueError(
            f"Environment '{env}' not found in login data file {filepath}. "
            f"Available environments: {list(data.keys())}"
        )

    return data[env]


@log_decorator
def get_web_table_form_addition_data(user_type: str) -> Dict[str, Any]:
    """Return login data for the requested environment.
    Looks for test data in the package-relative path
    `playwright-framework/test_data/ui/login.json` by default. Can be
    overridden with the environment variable `TEST_DATA_DIR` which should
    point to the directory containing the `ui/login.json` file.
    """
    # Resolve path relative to this module so tests work from any CWD
    # By default the reader loads the project's packaged test data
    base = Path(__file__).resolve().parent.parent
    filepath = base / "test_data" / "ui" / "web_table_add_form.json"

    if not filepath.exists():
        raise FileNotFoundError(f"Login data file not found at: {filepath}")

    try:
        with filepath.open() as file:
            data = json.load(file)
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse JSON file {filepath}: {e}") from e

    if user_type not in data:
        raise ValueError(
            f"Environment '{user_type}' not found in login data file {filepath}. "
            f"Available environments: {list(data.keys())}"
        )

    return data[user_type]