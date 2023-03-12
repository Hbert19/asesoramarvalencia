from django.db import models
from .utils import generate_gifcard
import secrets
from datetime import datetime, timedelta
from products.models import Products

class Gifcard(models.Model):
    code = models.CharField(verbose_name='Código Gifcard', default=generate_gifcard, max_length=100)
    date = models.DateField()
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    email = models.EmailField(verbose_name='Email Gifcard')
    status = models.BooleanField(default=False, verbose_name='Usada')
    status_payment = models.BooleanField(default=True, verbose_name='Pagada')

    def check_gifcard(self):
        # Check the token gifcard
        self.db_time = self.date
        self.time = datetime.now()
        self.date = self.time.strftime('%Y') + '-' + self.time.strftime('%m') + '-' + self.time.strftime('%d')
        self.year = self.time.strftime('%Y')
        self.month = self.time.strftime('%m')
        self.day = self.time.strftime('%d')
        self.gifcard_status = datetime(year=int(self.year), month=int(self.month), day=int(self.day)) - timedelta(days=365)
        # self.check return True if the gifcard is valid
        self.check = self.db_time != self.gifcard_status
        self.result = self.check and self.status == False
        return self.result

    def __str__(self):
        return self.code
