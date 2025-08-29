from django.urls import path
from .views import ask_ai

urlpatterns = [
    path("ai/ask/", ask_ai, name="ask_ai"),
]
