import pytest
from rest_framework import status

from app.models import Document



# @pytest.mark.django_db
# def test_document_create_ok(client):
#     data = {
#         "title": "Test title",
#         "content": "Some content",
#     }
#     response = client.post(f"api/v1/document", data=data)
#     assert response.status_code == status.HTTP_201_CREATED
#     assert Document.objects.filter(title=data["title"])

def test_func():
    assert 1 == 1

