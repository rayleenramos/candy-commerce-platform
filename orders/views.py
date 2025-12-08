from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    # GET: Displays the checkout form and cart summary.
    # POST: Saves the order to the database and clears the cart.
    cart = Cart(request)
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            # Create order object but don't save to DB yet
            # allows user to modify it before saving
            order = form.save(commit=False)
            
            # If user is logged in, link this order to their account
            if request.user.is_authenticated:
                order.user = request.user
            order.save()
            
            # Move items from the Session Cart to the Database Order
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    price=item["price"],
                    quantity=item["quantity"],
                )
            
            # Clear the cart now that the order is saved
            cart.clear()
            
            # Redirect to success page
            return render(request, "orders/created.html", {"order": order})
    else:
        form = OrderCreateForm()
    return render(request, "orders/create.html", {"cart": cart, "form": form})


@login_required
def order_history(request):
    # Displays a list of past orders for the currently logged-in user.
    orders = Order.objects.filter(user=request.user)
    return render(request, "orders/history.html", {"orders": orders})
