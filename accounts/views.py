"""
Account views for user authentication
"""

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages

User = get_user_model()

def register(request):
    """User registration: creates a real user in the database."""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        # checks if all fields are filled 
        if not username or not password or not password2:
            messages.error(request, "Please fill in all fields.")
        # check if passwords match
        elif password != password2:
            messages.error(request, "Passwords do not match.")
        # check if username is already taken
        elif User.objects.filter(username=username).exists():
            messages.error(request, "This username is already taken.")
        else:
            # create the user in the database
            user = User.objects.create_user(username=username, password=password)
            user.save()
            # registration successful
            messages.success(request, f"Account created for {username}! You can now log in.")
            return redirect("login")

    return render(request, "accounts/register.html")


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
