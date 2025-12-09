"""
Management command to update candy images
"""

from django.core.management.base import BaseCommand
from store.models import Candy


class Command(BaseCommand):
    help = "Update image URLs for candies"

    def handle(self, *args, **options):
        # Mapping of candy names to their image filenames
        # We will assume images are stored in static/store/images/
        image_mapping = {
            "Chocolate Bar": "store/images/chocolate_bar.png",
            "Gummy Bears": "store/images/gummy_bears.png",
            "Lollipop": "store/images/lollipop.png",
            "Jelly Beans": "store/images/jelly_beans.png",
            "Caramel": "store/images/caramel.png",
            "Sour Patch Kids": "store/images/sour_patch_kids.png",
            "Peppermint": "store/images/peppermint.png",
            "Dark Chocolate": "store/images/dark_chocolate.png",
        }

        for name, image_path in image_mapping.items():
            try:
                candy = Candy.objects.get(name=name)
                candy.image_url = image_path
                candy.save()
                self.stdout.write(self.style.SUCCESS(f"Updated image for {name}"))
            except Candy.DoesNotExist:
                self.stdout.write(self.style.WARNING(f"Candy not found: {name}"))
