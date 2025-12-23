"""
Account views for user authentication
"""

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages

User = get_user_model()


from django.contrib.auth.forms import UserCreationForm


def register(request):
    """User registration: creates a real user in the database."""
    print("DEBUG: Register view called")
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Account created for {username}! You can now log in."
            )
            return redirect("login")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserCreationForm()

    return render(request, "accounts/register.html", {"form": form})


def login_view(request):
    """Login view: supports admin/cps5301 and all registered users."""
    # redirect authenticated users to home
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # ensure the template's admin account exists
        if username == "admin" and password == "cps5301":
            # create or fix admin user (if needed)
            admin_user, created = User.objects.get_or_create(username="admin")
            if created or not admin_user.check_password(password):
                admin_user.set_password(password)
                admin_user.is_staff = True
                admin_user.is_superuser = True
                admin_user.save()

        # try to authenticate ANY user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # successful login
            login(request, user)
            messages.success(request, f"Welcome back, {username}!")
            next_url = request.POST.get("next") or request.GET.get("next") or "home"
            return redirect(next_url)
        else:
            # failed login
            messages.error(request, "Invalid username or password.")

    return render(request, "accounts/login.html")


def logout_view(request):
    """Custom logout view"""
    # Store logout message before clearing session
    messages.success(request, "You have been successfully logged out.")

    # Logout user (this clears auth-related session data)
    logout(request)

    return redirect("login")


@login_required
def account_page(request):
    """User account page"""
    context = {
        "user": request.user,
    }
    return render(request, "accounts/account.html", context)


from .forms import SavedCardForm
from .models import SavedCard


@login_required
def add_card(request):
    if request.method == "POST":
        form = SavedCardForm(request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.user = request.user
            card.save()
            messages.success(request, "Card added successfully.")
            return redirect("account")
    else:
        form = SavedCardForm()

    return render(request, "accounts/add_card.html", {"form": form})


@login_required
def remove_card(request, card_id):
    if request.method == "POST":
        card = SavedCard.objects.filter(id=card_id, user=request.user).first()
        if card:
            card.delete()
            messages.success(request, "Card removed.")
        else:
            messages.error(request, "Card not found.")
    return redirect("account")


from .forms import UserUpdateForm, ProfileUpdateForm
from .models import Profile


@login_required
def edit_profile(request):
    # Ensure profile exists (for old users)
    if not hasattr(request.user, "profile"):
        Profile.objects.create(user=request.user)

    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your account has been updated!")
            return redirect("account")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {"u_form": u_form, "p_form": p_form}

    return render(request, "accounts/edit_profile.html", context)
