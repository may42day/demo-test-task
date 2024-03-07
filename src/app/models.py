from django.db import models
from django.contrib.auth.models import User


class Document(models.Model):
    PUBLISHED = "published"
    ARCHIVED = "archived"
    DRAFT = "draft"

    DOC_STATUSES = [
        (PUBLISHED, "Published"),
        (ARCHIVED, "Archived"),
        (DRAFT, "Draft"),
    ]

    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.CharField(max_length=9, choices=DOC_STATUSES, default=DRAFT)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
