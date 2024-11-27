# from django.conf.urls import url 
from django.urls import path

from .views import (
    BranchAPIView,
    BranchDetailAPIView,
    BankAPIView,
    BankDetailAPIView,
    CreateAccountAPIView,
    AccountListAPIView,
    DepositAPIView,
    WithdrawAPIView,
    AccountDetailAPIView,
)

urlpatterns = [
    path('branch/', BranchAPIView.as_view(),name='branches'),
    path('branch/<int:pk>/', BranchDetailAPIView.as_view(),name='branch-detail'),
    path('bank/', BankAPIView.as_view(), name='banks'),
    path('bank/<int:pk>/', BankDetailAPIView.as_view(), name='bank-detail'),
    path('create-account/', CreateAccountAPIView.as_view(), name='create-account'),
    path('account/', AccountListAPIView.as_view(), name='accounts'),
    path('deposit/', DepositAPIView.as_view(), name='deposit'),
    path('withdraw/', WithdrawAPIView.as_view(), name='withdraw'),
    path('account/<int:pk>/', AccountDetailAPIView.as_view(), name='account-detail'),
]
