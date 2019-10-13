from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/', views.detail, name='detail'),
    path('shortcut/<int:question_tuple_id>/', views.shortcut, name='shortcut'),
    path('results/', views.results, name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]