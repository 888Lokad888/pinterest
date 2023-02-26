from django.urls import path 
from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('tag/<slug:tag_slug>/', HomePage.as_view(), name='tagged'),
    path('post/<uuid:post_uuid>/', ShowPost.as_view(), name='show_post'),
    path('add_post/', AddPost.as_view(), name='add_post'),
    path('registration/', RegisterUser.as_view(), name='registration'),
    path('login/', LoginUser.as_view(), name='login'),
    path('liked/', Liked.as_view(), name='liked'),
    path('profile/', profile, name='profile'),
    path('logout/', logout_user, name='logout'),
]