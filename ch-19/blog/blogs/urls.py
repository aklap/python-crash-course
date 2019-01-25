from django.urls import path


from . import views

app_name = 'blogs'
urlpatterns = [
    # Home page
    path('', views.index, name="index"),
    # Add a new post
    path('new_blogpost/', views.new_blogpost, name="new_blogpost"),
    # View a single post
    path('blogposts/<int:blogpost_id>/', views.blogpost, name="blogpost"),
    # Edit a single post
    path('edit_blogpost/<int:blogpost_id>/', views.edit_blogpost,name="edit_blogpost"),
    # Delete a post
    path('delete_blogpost/<int:blogpost_id>/', views.delete_blogpost, name="delete_blogpost"),
]
