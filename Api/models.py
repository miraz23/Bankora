from django.db import models

# Create your models here.

class Branch(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    branch_code = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = "Branches"

    def json_object(self):
        return {
            "name":self.name,
            "address":self.address,
            "branch_code":self.branch_code
        }

    def __str__(self):
        return self.name

class Bank(models.Model):
    name = models.CharField(max_length=250) 
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def json_object(self):
        return {
            'name' : self.name,
            'branch' : self.branch
        }
    
    def __str__(self):
        return self.name
    
class Client(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)

    def json_object(self):
        return {
            'name' : self.name,
            'address' : self.address
        }

    def __str__(self):
        return self.name

class Account(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    open_date = models.CharField(max_length=250)
    account_type = models.CharField(max_length=250)

    @property
    def balance(self):
        deposits = sum([deposit.amount for deposit in Deposit.objects.filter(account = self.id)])
        withdrawals = sum([withdraw.amount for withdraw in Withdraw.objects.filter(account = self.id)])
        total = deposits - withdrawals

        return total

    def json_object(self):
        return {
            "open_date" : self.open_date,
            "account_type" : self.account_type,
            "bank" : self.bank
        }

    def __str__(self):
        return self.account_type

class Deposit(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.FloatField()

class Withdraw(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.FloatField()