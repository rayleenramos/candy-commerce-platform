# Walkthrough - Order History and Tracking

I have implemented the Order History and Tracking features, allowing users to view their past orders and track their status.

## Changes

### Backend
- **Models**: Added `Order` and `OrderItem` models to `store/models.py`.
- **Admin**: Registered these models in `store/admin.py` for management.
- **Simulation**: Created `simulate_orders` management command to simulate status updates.

### Frontend
- **Views**: Added `order_list` and `order_detail` views in `store/views.py`.
- **Templates**: Created `store/order_list.html` and `store/order_detail.html`.
- **URLs**: Added routes `orders/` and `orders/<int:order_id>/`.
- **Navigation**: Added "My Orders" button to the Account page.

## Verification Results

### Automated Simulation
I created a test order and ran the simulation command. The order status successfully updated from `Created` to `Shipped` and then to `Delivered`.

```bash
$ python manage.py simulate_orders
Starting order simulation...
Order #1: Created -> Shipped
Waiting 10 seconds before next update...
Order #1: Shipped -> Delivered
Waiting 10 seconds before next update...
```

### Manual Verification Steps
1.  **Login**: Log in with your user account.
2.  **Navigate**: Go to the "Account" page.
3.  **View Orders**: Click "My Orders" to see the list of your orders.
4.  **View Details**: Click "View" on an order to see the details and current status.
5.  **Simulate Updates**:
    - Open a terminal.
    - Run `.\venv\Scripts\python manage.py simulate_orders`.
    - Refresh the order details page to see the status change in real-time (every 10 seconds).
