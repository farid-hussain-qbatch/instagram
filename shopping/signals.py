# code
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Productversion, Product


@receiver(pre_save, sender=Product)
def price_updated(instance, **kwargs):
    updated = Product.objects.filter(id = instance.id)
    print(updated)
    if  not updated:
        print("pass")
        pass
    else:
        updated = updated[0].price
        print(instance.price)
        print(updated)
        if(instance.price == updated):
           print('name')
           pass
        else:
	        Productversion.objects.create(products=instance, price=instance.price , brand = instance.brand)
        
   

@receiver(pre_save, sender=Product)
def save_product(sender, instance, **kwargs):
    print(instance)
	

