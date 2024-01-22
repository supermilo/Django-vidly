from django.urls import path
from . import views  # from this directory import views

#URLConf
# movies/
app_name = 'movies'

urlpatterns = [
    # path('movies/hello', views.index)
    # path('hello/', views.index)
    path('', views.index, name='index'),
    path('<int:movie_id>', views.detail, name='detail')
    ]    # path('', views.index, name='movies_index'),
    # path('<int:movie_id>', views.detail, name='movies_detail')


