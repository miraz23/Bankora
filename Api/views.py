from rest_framework import generics,status
from rest_framework.response import Response 
from rest_framework.views import APIView

from .models import *
from .serializers import *


class BranchAPIView(generics.ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class BranchDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class BankAPIView(generics.ListCreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class BankDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class CreateAccountAPIView(APIView):
    def post(self,request):
        """
        Create account, for example
        {
            "full_name": "John Doe",
            "address": "123 Main St",
            "open_date": "2018-01-01",
            "account_type": "savings",
            "bank": 1
        }
        """
        client = Client.objects.create(
            name = request.data['full_name'],
            address = request.data['address']
        )
        bank = Bank.objects.get(pk=request.data['bank'])
        account = Account.objects.create(
            client = client,
            open_date = request.data['open_date'],
            account_type = request.data['account_type'],
            bank = bank
        )

        serializer = AccountSerializer(account)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

class AccountListAPIView(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class DepositAPIView(generics.ListCreateAPIView):
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer

class WithdrawAPIView(generics.ListCreateAPIView):
    queryset = Withdraw.objects.all()
    serializer_class = WithdrawSerializer

class AccountDetailAPIView(generics.RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountDetailSerializer