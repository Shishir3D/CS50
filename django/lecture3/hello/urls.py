from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shishir', views.shishir, name='shishir'),
    path('bob', views.bob, name='bob')
    # other URL patterns
]
