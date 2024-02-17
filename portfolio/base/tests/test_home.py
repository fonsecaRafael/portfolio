import pytest
from django.urls import reverse


@pytest.fixture
def response(client):
    response = client.get(reverse('base:home'))
    return response


def test_status_code(response):
    assert response.status_code == 200
