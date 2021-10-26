from django.urls import path
from .views import test_view, home_page

urlpatterns = [
    path("about/", test_view),
    path("", home_page)
]    