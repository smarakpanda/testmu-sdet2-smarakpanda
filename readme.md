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