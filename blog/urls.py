from django.urls import path
from . import views

urlpatterns = [
    path("",views.starting_page,"staring-page"),
    path("posts",views.posts,"posts-page"),
    path("posts/<slug:slug>",views.post_details,"post-details-page")
]
