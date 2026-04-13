from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/<int:id>/', views.restaurant_menu, name='menu'),
    path('cart/', views.cart, name='cart'),
    path('add/<int:item_id>/', views.add_to_cart, name='add_cart'),

    # 👉 NEW (Cart controls)
    path('increase/<int:cart_id>/', views.increase_quantity, name='increase'),
    path('decrease/<int:cart_id>/', views.decrease_quantity, name='decrease'),
    path('remove/<int:cart_id>/', views.remove_item, name='remove'),

    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('account/', views.account, name='account'),
    path('search/', views.search, name='search'),
    path('checkout/', views.checkout, name='checkout'),
    path('add_address/', views.add_address, name='add_address'),
    path('edit_address/<int:address_id>/', views.edit_address, name='edit_address'),
    path('delete_address/<int:address_id>/', views.delete_address, name='delete_address'),
    path('payment_success/', views.payment_success, name='payment_success'),
]
