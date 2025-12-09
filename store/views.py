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


from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect


@staff_member_required
def inventory_list(request):
    """Staff-only view to list all candies and their stock"""
    candies = Candy.objects.all()
    context = {
        "candies": candies,
    }
    return render(request, "store/inventory_list.html", context)


@staff_member_required
def update_stock(request, candy_id):
    """Staff-only view to update stock for a candy"""
    candy = get_object_or_404(Candy, id=candy_id)

    if request.method == "POST":
        new_stock = request.POST.get("stock")
        if new_stock:
            candy.stock = int(new_stock)
            candy.save()
            return redirect("inventory_list")

    context = {
        "candy": candy,
    }
    return render(request, "store/update_stock.html", context)


from .forms import CandyForm


@staff_member_required
def candy_create(request):
    """Staff-only view to add a new candy"""
    if request.method == "POST":
        form = CandyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("inventory_list")
    else:
        form = CandyForm()

    return render(request, "store/candy_create.html", {"form": form})


@staff_member_required
def candy_delete(request, candy_id):
    """Staff-only view to delete a candy"""
    candy = get_object_or_404(Candy, id=candy_id)
    if request.method == "POST":
        candy.delete()
        return redirect("inventory_list")
    return render(request, "store/candy_confirm_delete.html", {"candy": candy})
