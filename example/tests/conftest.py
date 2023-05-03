import pytest
import requests


@pytest.fixture
def common_fixture():
    return 42


@pytest.fixture
def example_people_data():
    people = [
        {
            "first_name": "Alfonsa",
            "second_name": "Ruiz",
            "title": "Senior Software Engineer",
        },
        {
            "first_name": "Sayid",
            "second_name": "Khan",
            "title": "Project Manager",
        },
    ]
    return people


@pytest.fixture(autouse=True)
def disable_network_calls(monkeypatch):
    def stunted_get():
        raise RuntimeError("Network access not allowed during testing!")
    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: stunted_get())