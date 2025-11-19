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
                "description": "Delicious milk chocolate bar",
                "price": 2.99,
                "stock": 100,
                "category": "Chocolate",
                "image_url": "",
            },
            {
                "name": "Gummy Bears",
                "description": "Colorful fruit-flavored gummy bears",
                "price": 3.49,
                "stock": 150,
                "category": "Gummies",
                "image_url": "",
            },
            {
                "name": "Lollipop",
                "description": "Classic swirl lollipop",
                "price": 1.99,
                "stock": 200,
                "category": "Hard Candy",
                "image_url": "",
            },
            {
                "name": "Jelly Beans",
                "description": "Assorted flavors jelly beans",
                "price": 4.99,
                "stock": 120,
                "category": "Gummies",
                "image_url": "",
            },
            {
                "name": "Caramel",
                "description": "Soft caramel candies",
                "price": 3.99,
                "stock": 80,
                "category": "Caramel",
                "image_url": "",
            },
            {
                "name": "Sour Patch Kids",
                "description": "Sweet and sour gummy candies",
                "price": 4.49,
                "stock": 90,
                "category": "Gummies",
                "image_url": "",
            },
            {
                "name": "Peppermint",
                "description": "Cool peppermint candies",
                "price": 2.49,
                "stock": 180,
                "category": "Hard Candy",
                "image_url": "",
            },
            {
                "name": "Dark Chocolate",
                "description": "Rich dark chocolate bar",
                "price": 3.99,
                "stock": 70,
                "category": "Chocolate",
                "image_url": "",
            },
        ]

        for candy_data in candies_data:
            candy, created = Candy.objects.get_or_create(
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
