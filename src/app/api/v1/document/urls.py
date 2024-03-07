from django.urls import path
from app.api.v1.document import views
from app.models import Document


app_name = "document"

urlpatterns = [
    path("", views.DocumentCreateAPIView.as_view(), name="document-create"),
    path("list", views.DocumentListAPIView.as_view(), name="document-list"),
    path(
        "<int:pk>/archive/",
        views.DocumentDestroyView.as_view(),
        name="document-archive",
    ),
    path(
        "<int:pk>/",
        views.DocumentDetailUpdateView.as_view(),
        name="document-detail-update",
    ),
]
