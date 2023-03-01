import pytest
import requests


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru",
        help="This is request url"
    )

    parser.addoption(
        "--status_code",
        default=200,
    )


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def status_code_await(request):
    return request.config.getoption("--status_code")

