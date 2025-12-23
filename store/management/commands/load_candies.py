"""
Management command to load initial candy data
"""

from django.core.management.base import BaseCommand
from store.models import Candy


class Command(BaseCommand):
    help = "Load initial candy data into the database"

    def handle(self, *args, **options):
        candies_data = [
            {
                "name": "Chocolate Bar",
                "description": "Milk Chocolate Bar",
                "price": 2.99,
                "stock": 100,
                "category": "Chocolate",
                "image_url": "store/images/chocolate_bar.png",
            },
            {
                "name": "Gummy Bears",
                "description": "Fruit-flavored Gummy Bears",
                "price": 3.49,
                "stock": 150,
                "category": "Gummies",
                "image_url": "store/images/gummy_bears.png",
            },
            {
                "name": "Lollipop",
                "description": "Swirl Lollipop",
                "price": 1.99,
                "stock": 200,
                "category": "Hard Candy",
                "image_url": "store/images/lollipop.png",
            },
            {
                "name": "Jelly Beans",
                "description": "Flavored Jelly Beans",
                "price": 4.99,
                "stock": 120,
                "category": "Gummies",
                "image_url": "store/images/jelly_beans_v2.png",
            },
            {
                "name": "Caramel",
                "description": "Caramel Candies",
                "price": 3.99,
                "stock": 80,
                "category": "Caramel",
                "image_url": "store/images/caramel.png",
            },
            {
                "name": "Sour Patch Kids",
                "description": "Sweet and Sour Gummy Candies",
                "price": 4.49,
                "stock": 90,
                "category": "Gummies",
                "image_url": "store/images/sour_patch_kids.png",
            },
            {
                "name": "Peppermint",
                "description": "Peppermint Candies",
                "price": 2.49,
                "stock": 180,
                "category": "Hard Candy",
                "image_url": "store/images/peppermint.png",
            },
            {
                "name": "Dark Chocolate",
                "description": "Rich Dark Chocolate",
                "price": 3.99,
                "stock": 70,
                "category": "Chocolate",
                "image_url": "store/images/dark_chocolate.png",
            },
        ]

        for candy_data in candies_data:
            candy, created = Candy.objects.update_or_create(
                name=candy_data["name"], defaults=candy_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created candy: {candy.name}"))
            else:
                self.stdout.write(
                    self.style.WARNING(f"Candy already exists: {candy.name}")
                )

        self.stdout.write(
            self.style.SUCCESS(f"Successfully loaded {len(candies_data)} candies")
        )
