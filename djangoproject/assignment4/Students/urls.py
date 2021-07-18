from django.urls import path
from .import views

urlpatterns = [
    path('index/', views.listView, name='index'),

    path('student/create', views.create.as_view(), name='create'),

    path('student/', views.listView.as_view(), name='listView'),

    path('student/<pk>', views.detailView.as_view(), name='detailView'),

    path('student/update/<pk>', views.update.as_view(), name='update'),

    path('student/delete/<pk>', views.delete.as_view(), name='delete'),
]
