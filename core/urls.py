from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    # Auth
    path('register/', RegisterView.as_view()),
    path('login/', TokenObtainPairView.as_view()),

    # Products
    path('products/', ProductListView.as_view()),
    path('products/create/', ProductCreateView.as_view()),

    # Orders
    path('orders/', OrderListView.as_view()),
    path('orders/create/', OrderCreateView.as_view()),
    path('orders/update/<int:pk>/', OrderUpdateView.as_view()),
]