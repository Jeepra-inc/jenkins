from django.urls import path
from . import views

urlpatterns = [
    path('page/<int:page_id>/', views.page_detail, name='page_detail'),
]
