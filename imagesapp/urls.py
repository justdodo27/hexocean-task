from django.urls import path
from .views import ImageListView, ImageDetailView, redirectImageURL, CreateTemporaryView

urlpatterns = [
    path('images/', ImageListView.as_view()),
    path('images/<int:pk>', ImageDetailView.as_view()),
    path('images/<int:pk>/<int:seconds>', CreateTemporaryView.as_view()),
    path('tempurl/<int:pk>', redirectImageURL),
]