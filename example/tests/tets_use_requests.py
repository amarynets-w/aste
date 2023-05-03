from example.example import make_http_call


def test_make_request():
    response = make_http_call('http://example.com')
    assert response.status_code == 200
