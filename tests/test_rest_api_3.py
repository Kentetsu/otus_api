import requests
import pytest
base_jsonplaceholder_url = "https://jsonplaceholder.typicode.com/posts"


def test_list_all():
    r = requests.get(base_jsonplaceholder_url)
    assert r.status_code == 200


@pytest.mark.parametrize('input_number', ['/1',
                                          '/2',
                                          '/3',
                                          '/4'])
def test_get_resource(input_number):
    r = requests.get(base_jsonplaceholder_url + input_number)
    assert r.status_code == 200
    assert r.json()['id'] == int(input_number[1])


@pytest.mark.parametrize('input_id, output_id',
                         [(10000, '10000'),
                          (-1, '-1'),
                          (0, '0')])
@pytest.mark.parametrize('input_title, output_title',
                         [('title', 'title'),
                          ('', ''),
                          (100, '100'),
                          ('&', '&')])
def test_create_resource(input_id, output_id, input_title, output_title):
    r = requests.post(
        base_jsonplaceholder_url,
        data={'title': input_title, 'body': 'bar', 'userId': input_id})
    assert r.json()['title'] == output_title
    assert r.json()['body'] == 'bar'
    assert r.json()['userId'] == output_id


@pytest.mark.parametrize('input_number, input_id, output_id',
                         [('/1', 10, '10'),
                          ('/2', -1, '-1'),
                          ('/3', 0, '0')])
@pytest.mark.parametrize('input_title, output_title',
                         [('title', 'title'),
                          ('', ''),
                          (100, '100'),
                          ('&', '&')])
def test_update_resource(input_number, input_id, output_id, input_title, output_title):
    r = requests.put(
        base_jsonplaceholder_url + input_number,
        data={'title': input_title, 'body': 'body_test', 'userId': input_id})
    assert r.json()['title'] == output_title
    assert r.json()['body'] == 'body_test'
    assert r.json()['userId'] == output_id


@pytest.mark.parametrize('input_number, input_title', [('/1', 'foo'),
                                                       ('/2', "boo"),
                                                       ('/3', 'fast'),
                                                       ('/4', 'slow')])
def test_patch_resource(input_number, input_title):
    r = requests.patch(base_jsonplaceholder_url + input_number,
                       data={'title': input_title})
    assert r.json()['title'] == input_title
