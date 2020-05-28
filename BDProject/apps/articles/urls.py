from django.urls import  path
from django.conf.urls import url
from . import views

from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:article_id>/', views.detail, name = 'detail'),
    path('<int:article_id>/leave_comment/', views.leave_comment, name='leave_comment'),
    url(r'^add_simple_photo/$', views.add_simple_photo, name='add_simple_photo'),
]