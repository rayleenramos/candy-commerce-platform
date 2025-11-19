"""
Store views for browsing candies
"""

from django.shortcuts import render, get_object_or_404
from .models import Candy


def home(request):
    """Home page showing all candies"""
    candies = Candy.objects.all()
    context = {
        "candies": candies,
    }
    return render(request, "store/home.html", context)


def candy_detail(request, candy_id):
    """Detail page for a single candy"""
    candy = get_object_or_404(Candy, id=candy_id)
    context = {
        "candy": candy,
    }
    return render(request, "store/candy_detail.html", context)
