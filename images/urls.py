from django.urls import path

from images.views import ImageSearchView


urlpatters = [
    path("search/images/", ImageSearchView.as_view(), name="image-search"),
]
