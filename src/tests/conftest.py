import pytest
from django.test import Client


# @pytest.mark.django_db
# @pytest.fixture
# def client():
#     """Creating Django client for API requests"""
#     return Client()


# @pytest.fixture(scope="session")
# def django_db_setup():
#     from django.conf import settings

#     settings.DATABASES["default"] = {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": ":memory:",
#         "ATOMIC_REQUESTS": True,
#     }
