import pytest
from django.urls import reverse

from portfolio.django_assertions import assert_contains


@pytest.fixture
def response(client):
    response = client.get(reverse('base:home'))
    return response


def test_status_code(response):
    assert response.status_code == 200


def test_home_link(response):
    assert_contains(response, f'href="{reverse('base:home')}">Home</a>')


def test_knowledge_link(response):
    assert_contains(response, f'href="{reverse('knowledge:knowledge')}">Knowledge</a>')


def test_projects_link(response):
    assert_contains(response, f'href="{reverse('projects:projects')}">Projects</a>')
