import pytest
from playwright.sync_api import sync_playwright


def pytest_addoption(parser):
    """Allows passing a custom test URL via --test-url."""
    parser.addoption("--test-url", action="store", default="")


@pytest.fixture
def test_url(request):
    """Fixture to get the test URL from CLI or default."""
    return request.config.getoption("--test-url")


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()
