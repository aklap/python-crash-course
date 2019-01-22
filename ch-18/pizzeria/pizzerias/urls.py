from django.urls import path


from . import views

app_name = 'pizzerias'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
]
