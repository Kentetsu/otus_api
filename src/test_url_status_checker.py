import pytest
import requests


def test_url_status(base_url, status_code_await):
    r = requests.get(base_url)
    assert r.status_code == int(status_code_await)
