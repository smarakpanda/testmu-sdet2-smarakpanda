Architecture Notes

This framework uses Python + Playwright with Pytest as the execution layer.

Design principles:
- Page Object Model (POM) for separation of concerns
- Reusable fixtures for browser lifecycle management
- Config-driven execution for environment flexibility
- Utility abstraction for shared helper logic
- Reporting and artifact capture for debugging

Folder responsibilities:
- tests/: test scenarios
- pages/: page abstractions
- fixtures/: reusable pytest fixtures
- config/: environment configuration
- utils/: helper modules
- reports/: execution reports
- screenshots/: failure artifacts
 
This scaffold is intentionally structured to support extensibility and maintainability as test coverage grows.

Test data
---------

Test data files are stored in the repository at:

```
playwright-framework/test_data/ui/
```

The test-data reader loads files directly from this location by resolving paths relative to the package source. This ensures tests work regardless of the current working directory, and no environment variables are required to run tests locally.

Example: UI login test data is automatically loaded from `playwright-framework/test_data/ui/login.json`.
