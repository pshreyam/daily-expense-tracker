from django.db import models
from django.urls import reverse
from django.db.models import Sum

from PIL import Image

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    img = models.ImageField(default='default.jpg', upload_to='items')

    def __str__(self):
        return f'Item: {self.name}'

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.img.path)
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.img.path)
    
    def get_absolute_url(self):
        return reverse('tracker-item-detail', kwargs={'pk' : self.pk})

class Purchase(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    date_purchased = models.DateField()
    purchase_amount = models.FloatField(default=0)

    def __str__(self):
        return f'Purchase: {self.id}'

    def get_absolute_url(self):
        return reverse('tracker-purchase-detail', kwargs={'pk' : self.pk})

    @staticmethod
    def total():
        total = Purchase.objects.aggregate(Sum('purchase_amount'))
        return total['purchase_amount__sum']

    def save(self):
        self.purchase_amount = self.item.price * self.quantity
        super().save()