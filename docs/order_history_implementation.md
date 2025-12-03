# Order History and Tracking Implementation

## Overview
Implemented a system for users to view their past orders and track their status (Created -> Shipped -> Delivered).

## New Files
- `store/templates/store/order_list.html`: Template for the "My Orders" page.
- `store/templates/store/order_detail.html`: Template for the individual order details page.
- `store/management/commands/simulate_orders.py`: Management command to simulate order status updates.

## Modified Files & Methods Added

### `store/models.py`
- **Class `Order`**: Represents a customer order.
    - Fields: `user`, `status`, `total_price`, `created_at`, `tracking_number`.
    - Status Choices: `Created`, `Shipped`, `Delivered`.
- **Class `OrderItem`**: Represents an item within an order.
    - Fields: `order`, `candy`, `quantity`, `price`.

### `store/views.py`
- **Function `order_list(request)`**:
    - Retrieves all orders for the logged-in user.
    - Renders `store/order_list.html`.
- **Function `order_detail(request, order_id)`**:
    - Retrieves a specific order for the logged-in user (returns 404 if not found or not owned).
    - Renders `store/order_detail.html`.

### `store/urls.py`
- Added URL patterns:
    - `orders/` -> `views.order_list`
    - `orders/<int:order_id>/` -> `views.order_detail`

### `store/admin.py`
- Registered `Order` and `OrderItem` (via `OrderItemInline`) to allow management in the Django Admin.

### `accounts/templates/accounts/account.html`
- Added a "My Orders" button to link to the order history list.

## Simulation
A management command was added to simulate the progression of order statuses.
- **Command**: `python manage.py simulate_orders`
- **Logic**: Updates `Created` orders to `Shipped` (assigning a tracking number), and `Shipped` orders to `Delivered`, with a time delay.
