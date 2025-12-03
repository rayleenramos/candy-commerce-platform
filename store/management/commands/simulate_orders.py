import time
import random
from django.core.management.base import BaseCommand
from store.models import Order

class Command(BaseCommand):
    help = 'Simulates order status progression (Created -> Shipped -> Delivered)'

    def handle(self, *args, **options):
        self.stdout.write("Starting order simulation...")
        
        while True:
            orders = Order.objects.exclude(status='Delivered')
            
            if not orders.exists():
                self.stdout.write("No active orders to update. Waiting...")
                time.sleep(5)
                continue
                
            for order in orders:
                if order.status == 'Created':
                    self.stdout.write(f"Order #{order.id}: Created -> Shipped")
                    order.status = 'Shipped'
                    order.tracking_number = f"TRK-{random.randint(10000, 99999)}"
                    order.save()
                elif order.status == 'Shipped':
                    self.stdout.write(f"Order #{order.id}: Shipped -> Delivered")
                    order.status = 'Delivered'
                    order.save()
            
            self.stdout.write("Waiting 10 seconds before next update...")
            time.sleep(10)
