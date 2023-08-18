from django.urls import path
from .views import BookUpdateView,BookDetalesView,BookCreateView,BookDeleteView,BooklistALLView
from rest_framework_simplejwt.views import TokenVerifyView
urlpatterns=[
    path('get_all/',BooklistALLView.as_view()),
    path("get_by_index/<int:pk>/",BookDetalesView.as_view()),
    path('create/',BookCreateView.as_view()),
    path("update/<int:pk>/",BookUpdateView.as_view()),
    path('delete/<int:pk>/',BookDeleteView.as_view()),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]