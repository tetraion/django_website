from django.urls import path
from .views import IndexView, AboutView, Index

urlpatterns = [
    path('', IndexView.as_view()),
    path('about/', AboutView.as_view()),
    path('index2/', Index.as_view()),
]
