from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart


from accounts.models import SavedCard


def order_create(request):
    # GET: Displays the checkout form and cart summary.
    # POST: Saves the order to the database and clears the cart.
    cart = Cart(request)
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            # Save card info if requested and user is logged in
            if request.user.is_authenticated and form.cleaned_data.get("save_card"):
                SavedCard.objects.create(
                    user=request.user,
                    card_number=form.cleaned_data["card_number"],
                    expiry_date=form.cleaned_data["card_expiry"],
                    card_holder_name=form.cleaned_data["name_on_card"],
                )

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
                # Decrease stock
                product = item["product"]
                product.stock -= item["quantity"]
                product.save()

            # Clear the cart now that the order is saved
            cart.clear()

            # Digital Delivery Feature
            if order.email.endswith("@kean.edu"):
                from django.core.mail import send_mail

                subject = f"Digital Candy Voucher for Order #{order.order_id}"
                message = f"""
                Hi {order.customer_name},

                Thanks for your order at Keanu's Candy Store!
                
                Since you used a Kean University email, here is your digital candy voucher:
                
                CODE: KEAN-CANDY-{order.order_id}-2025
                
                Enjoy!
                """
                send_mail(
                    subject,
                    message,
                    "orders@keanucandystore.com",
                    [order.email],
                    fail_silently=False,
                )

            # Redirect to success page
            return render(request, "orders/created.html", {"order": order})
    else:
        form = OrderCreateForm()
    return render(request, "orders/create.html", {"cart": cart, "form": form})


@login_required
def order_history(request):
    # Displays a list of past orders for the currently logged-in user.
    orders = Order.objects.filter(user=request.user)

    # trigger automatic updates for demo purposes
    for order in orders:
        order.update_status_based_on_time()

    return render(request, "orders/history.html", {"orders": orders})


@login_required
def order_detail(request, order_id):
    # Displays the details of a single order
    order = get_object_or_404(Order, order_id=order_id, user=request.user)

    # trigger automatic update
    order.update_status_based_on_time()

    return render(request, "orders/detail.html", {"order": order})
