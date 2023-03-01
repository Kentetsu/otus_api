import pytest
import requests
from urllib.parse import urljoin

base_url = "https://dog.ceo/api/"
path_list_all = "breeds/list/all"
path_random = "breeds/image/random"


def test_list_all():
    r = requests.get(base_url + path_list_all)
    assert r.status_code == 200
    assert r.json()['status'] == "success"


def test_random():
    r = requests.get(base_url + path_random)
    assert r.status_code == 200
    assert r.json()['status'] == "success"
    img = requests.get(r.json()['message'])
    assert img.status_code == 200


@pytest.mark.parametrize('input_breed',
                         ['hound',
                          'mastiff',
                          'retriever'])
def test_by_breed(input_breed):
    r = requests.get(base_url + "breed/" + input_breed + '/images')
    assert r.status_code == 200
    assert r.json()['status'] == "success"
    img = requests.get(r.json()['message'][1])
    assert img.status_code == 200


@pytest.mark.parametrize('input_breed, input_sub_breed', [('hound', 'afghan'),
                                                            ('mastiff', 'bull'),
                                                            ('retriever', 'chesapeake')])
def test_by_sub_breed(input_breed, input_sub_breed):
    r = requests.get(base_url + "breed/" + input_breed + '/' + input_sub_breed + '/images')
    assert r.status_code == 200
    assert r.json()['status'] == "success"
    img = requests.get(r.json()['message'][1])
    assert img.status_code == 200


@pytest.mark.parametrize('input_breed',
                         ['hound',
                          'mastiff',
                          'retriever'])
def test_breeds_list(input_breed):
    r = requests.get(base_url + "breed/" + input_breed + "/images/random")
    assert r.status_code == 200
    assert r.json()['status'] == "success"
    img = requests.get(r.json()['message'])
    assert img.status_code == 200
