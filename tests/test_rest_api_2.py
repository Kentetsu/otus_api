import requests
import pytest

base_url = "https://api.openbrewerydb.org/breweries"
query_by_city = [
    {'by_city': 'san_diego',
        'per_page': 3},
    {'by_city': 'bend',
        'per_page': 1},
    {'by_city': 'williamsville',
        'per_page': 5}
]

query_search = [
    {'query': 'dog',
     'per_page': 3},
    {'query': 'cat',
     'per_page': 3},
    {'query': 'boss',
     'per_page': 3}
]


def test_list_all():
    r = requests.get(base_url)
    assert r.status_code == 200


def test_random():
    r = requests.get(base_url + "/random")
    assert r.status_code == 200


@pytest.mark.parametrize('input_query', query_by_city)
def test_by_city(input_query):
    r = requests.get(base_url, params=input_query)
    assert r.status_code == 200


@pytest.mark.parametrize('input_query', query_search)
def test_search(input_query):
    r = requests.get(base_url + '/search', params=input_query)
    assert r.status_code == 200


def test_meta():
    r = requests.get(base_url + '/meta')
    assert r.status_code == 200
