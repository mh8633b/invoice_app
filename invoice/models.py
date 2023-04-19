from django.db import models
import datetime
# Create your models here.


class Invoice(models.Model):
    

    INVOICE_TYPE = (
        ('SALE' , 'sale'),
        ('PURCHASE' , 'purchase')
    )

    customer = models.CharField(max_length=100)
    credit_amount = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    billing_address = models.TextField(null=True, blank=True)
    date = models.DateField(auto_now_add= True)
    # due_date = models.DateField(null=True, blank=True)
    message = models.TextField(default= "this is a default message.")
    total_amount = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    status = models.BooleanField(default=False)
    invoice_type = models.CharField(max_length=100, choices=INVOICE_TYPE, default="SALE")
    def __str__(self):
        return str(self.customer)
    
    def get_status(self):
        return self.status

    # def save(self, *args, **kwargs):
        # if not self.id:             
        #     self.due_date = datetime.datetime.now()+ datetime.timedelta(days=15)
        # return super(Invoice, self).save(*args, **kwargs)

class LineItem(models.Model):
    customer = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    service = models.TextField()
    description = models.TextField()
    quantity = models.IntegerField()
    rate = models.DecimalField(max_digits=9, decimal_places=2)
    amount = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return str(self.customer)
   