# Implementation Plan - Order History and Tracking

## Goal Description
Implement a system for users to view their past orders and track their status. This includes a list view of all orders, a detailed view for individual orders, and status tracking (e.g., Pending, Shipped, Delivered).

## User Review Required
> [!IMPORTANT]
> This plan assumes orders are created via the Django Admin for now, as there is currently no "Checkout" functionality. If Checkout is needed immediately, please let me know.

## Proposed Changes

### Store App

#### [MODIFY] [models.py](file:///c:/Users/chris/Documents/Fall%202025/Advance%20Software%20Engineering/finalproject-candy_crushers-main/store/models.py)
- Add `Order` model:
    - `user`: ForeignKey to User
    - `status`: CharField with choices:
        - `Created` (default)
        - `Shipped`
        - `Delivered`
    - `total_price`: DecimalField
    - `created_at`: DateTimeField
    - `tracking_number`: CharField (optional)
- Add `OrderItem` model:
    - `order`: ForeignKey to Order
    - `candy`: ForeignKey to Candy
    - `quantity`: IntegerField
    - `price`: DecimalField (snapshot)

#### [MODIFY] [admin.py](file:///c:/Users/chris/Documents/Fall%202025/Advance%20Software%20Engineering/finalproject-candy_crushers-main/store/admin.py)
- Register `Order` and `OrderItem` to allow admin management.

#### [NEW] [management/commands/simulate_orders.py](file:///c:/Users/chris/Documents/Fall%202025/Advance%20Software%20Engineering/finalproject-candy_crushers-main/store/management/commands/simulate_orders.py)
- Create a management command to simulate order progression (Created -> Shipped -> Delivered) with time delays, satisfying the "time delay simulation" requirement.

#### [MODIFY] [views.py](file:///c:/Users/chris/Documents/Fall%202025/Advance%20Software%20Engineering/finalproject-candy_crushers-main/store/views.py)
- Add `order_list(request)`: Lists orders for the logged-in user.
- Add `order_detail(request, order_id)`: Shows details if the order belongs to the user.

#### [MODIFY] [urls.py](file:///c:/Users/chris/Documents/Fall%202025/Advance%20Software%20Engineering/finalproject-candy_crushers-main/store/urls.py)
- Add paths for `orders/` and `orders/<int:order_id>/`.

#### [NEW] [order_list.html](file:///c:/Users/chris/Documents/Fall%202025/Advance%20Software%20Engineering/finalproject-candy_crushers-main/store/templates/store/order_list.html)
- Display table of orders with Date, Total, Status, and "View" link.

#### [NEW] [order_detail.html](file:///c:/Users/chris/Documents/Fall%202025/Advance%20Software%20Engineering/finalproject-candy_crushers-main/store/templates/store/order_detail.html)
- Display Order Info (Status, Tracking)
- Display List of Items (Candy, Qty, Price)

### Accounts App

#### [MODIFY] [account.html](file:///c:/Users/chris/Documents/Fall%202025/Advance%20Software%20Engineering/finalproject-candy_crushers-main/accounts/templates/accounts/account.html)
- Add a button/link to "My Orders".

## Verification Plan

### Manual Verification
1.  **Create Data**: Log in as Admin, create a few `Order` entries for a test user.
2.  **Simulation**: Run `python manage.py simulate_orders` to see statuses update.
3.  **List View**: Log in as the test user, navigate to `/orders/` and verify all orders are listed correctly.
4.  **Detail View**: Click on an order to verify item details and status are shown.
5.  **Security**: Try to access an order ID belonging to another user (should return 404).
