from django.contrib.auth import get_user_model

User = get_user_model()

try:
    user, created = User.objects.get_or_create(username="admin")
    user.set_password("cps5301")
    user.is_staff = True
    user.is_superuser = True
    user.is_active = True
    user.save()
    print(f"Successfully configured admin user. Password set to 'cps5301'.")
except Exception as e:
    print(f"Error: {e}")
