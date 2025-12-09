from django.test import TestCase, Client
from django.urls import reverse
from django.conf import settings
from store.models import Candy
from decimal import Decimal
from .cart import Cart


class CartClassTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.candy1 = Candy.objects.create(
            name="Test Candy 1",
            description="Description 1",
            price=Decimal("1.99"),
            stock=100,
            category="Test",
        )
        self.candy2 = Candy.objects.create(
            name="Test Candy 2",
            description="Description 2",
            price=Decimal("2.99"),
            stock=50,
            category="Test",
        )
        # Create a session for the cart
        session = self.client.session
        session[settings.CART_SESSION_ID] = {}
        session.save()

        # Mock request with session
        class MockRequest:
            def __init__(self, session):
                self.session = session

        self.request = MockRequest(session)

    def test_add_new_item(self):
        cart = Cart(self.request)
        cart.add(self.candy1, quantity=2)
        self.assertEqual(len(cart), 2)
        self.assertEqual(cart.get_total_price(), Decimal("3.98"))

    def test_update_quantity(self):
        cart = Cart(self.request)
        cart.add(self.candy1, quantity=1)
        cart.add(self.candy1, quantity=2)  # Should add to existing
        self.assertEqual(len(cart), 3)

        cart.add(self.candy1, quantity=5, override_quantity=True)  # Should override
        self.assertEqual(len(cart), 5)

    def test_remove_item(self):
        cart = Cart(self.request)
        cart.add(self.candy1, quantity=1)
        cart.add(self.candy2, quantity=1)
        self.assertEqual(len(cart), 2)

        cart.remove(self.candy1)
        self.assertEqual(len(cart), 1)
        self.assertEqual(cart.get_total_price(), Decimal("2.99"))

    def test_clear_cart(self):
        cart = Cart(self.request)
        cart.add(self.candy1, quantity=1)
        cart.clear()
        self.assertEqual(len(cart), 0)


class CartViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.candy = Candy.objects.create(
            name="Test Candy",
            description="Description",
            price=Decimal("1.50"),
            stock=100,
            category="Test",
        )

    def test_cart_add_view(self):
        url = reverse("cart:cart_add", args=[self.candy.id])
        response = self.client.post(url, {"quantity": 2})
        self.assertRedirects(response, reverse("cart:cart_detail"))

        # Check session
        session = self.client.session
        cart = session[settings.CART_SESSION_ID]
        self.assertIn(str(self.candy.id), cart)
        self.assertEqual(cart[str(self.candy.id)]["quantity"], 2)

    def test_cart_remove_view(self):
        # Add item first
        session = self.client.session
        session[settings.CART_SESSION_ID] = {
            str(self.candy.id): {"quantity": 1, "price": str(self.candy.price)}
        }
        session.save()

        url = reverse("cart:cart_remove", args=[self.candy.id])
        response = self.client.post(url)
        self.assertRedirects(response, reverse("cart:cart_detail"))

        # Check session
        session = self.client.session
        cart = session[settings.CART_SESSION_ID]
        self.assertNotIn(str(self.candy.id), cart)

    def test_cart_detail_view(self):
        url = reverse("cart:cart_detail")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "cart/cart_detail.html")
