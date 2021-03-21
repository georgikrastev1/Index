from datetime import date

from django.utils import timezone

from django.db import models

# Create your models here.

class Peer_group_lists(models.Model):
    Group_name=models.CharField(max_length=200,default="Pulp")
    Group_description=models.CharField(max_length=400)

    def __str__(self):
        return self.Group_name

    class Meta:
        verbose_name_plural = 'Peer group lists'


class Companies(models.Model):
    name=models.CharField(max_length=5000,null=True)
    Stock_code=models.CharField(max_length=100,null=False)
    Peer_group=models.ForeignKey(Peer_group_lists,on_delete=models.CASCADE,null=True)
    Fx_company_choices=(
        ('AUD', 'AUD'),
        ('BRL', 'BRL'),
        ('CNY', 'CNY'),
        ('GBP', 'GBP'),
        ('HKD', 'HKD'),
        ('JPY', 'JPY'),
        ('NOK', 'NOK'),
        ('SEK', 'SEK'),
        ('USD', 'USD'),
        ('CLP', 'CLP'),
        ('ZAR', 'ZAR'),
        ('IDR', 'IDR'),
        ('THB', 'THB'),
        ('PLN', 'PLN'),
        ('INR', 'INR'),
        ('ILS', 'ILS'),
        ('EUR', 'EUR'),
    )
    Fx_company = models.CharField(max_length=200, choices=Fx_company_choices, default="EUR")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Companies'

class FX(models.Model):
    currency=models.CharField(max_length=100,null=True)
    exchange_rate=models.FloatField(max_length=50,null=True,default=1)

    class Meta:
        verbose_name_plural = 'FX'

    def __str__(self):
        return self.currency

class Financial_data(models.Model):
    company_id=models.ForeignKey(Companies,on_delete=models.CASCADE)
    market_capitalization_original=models.FloatField(max_length=50,null=True)
    market_capitalization_euro = models.FloatField(max_length=50, null=True)
    share_price_original = models.FloatField(max_length=50, null=True)
    share_price_euro = models.FloatField(max_length=50, null=True)
    shares_number=models.FloatField(max_length=50, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'Financial_Data'

class Peer_group_Financial_data(models.Model):
    Peer_group=models.ForeignKey(Peer_group_lists,on_delete=models.CASCADE)
    Market_capitalization=models.FloatField(max_length=50, null=True)
    Market_capitalization_percent=models.FloatField(max_length=50, null=True)
    created_at = models.DateField(default=date.today)

    class Meta:
        verbose_name_plural = 'Peer_group_Financial_data'

    def __str__(self):
        return f"{self.Peer_group}"