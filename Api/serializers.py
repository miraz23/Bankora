from rest_framework import serializers 
from .models import * 


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('name','address','branch_code',)
        read_only_fields = ('id',)

class BranchDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('__all__')

class BankSerializer(serializers.ModelSerializer):
    branch =  BranchSerializer()
    class Meta:
        model = Bank 
        fields = ('__all__')

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('__all__')

class AccountSerializer(serializers.ModelSerializer):
    bank = BankSerializer()
    client = ClientSerializer()
    class Meta:
        model = Account
        fields = ('__all__')

class AccountDetailSerializer(serializers.ModelSerializer):
    bank = BankSerializer()
    client = ClientSerializer()
    balance = serializers.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        model = Account
        fields = ['client', 'bank', 'balance', 'open_date', 'account_type', 'bank']

class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = ('__all__')

class WithdrawSerializer(serializers.ModelSerializer):
    class Meta:
        model = Withdraw
        fields = ('__all__')