from django.shortcuts import render,redirect

from foodexpress import settings



# Create your views here.
from .models import Address, Restaurant, MenuItem, Cart, Order
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import razorpay


def home(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'home.html', {'restaurants': restaurants})


def restaurant_menu(request, id):
    restaurant = Restaurant.objects.get(id=id)
    menu = MenuItem.objects.filter(restaurant=restaurant)
    return render(request, 'restaurant_menu.html', {
        'menu': menu,
        'restaurant': restaurant
    })


@login_required
def add_to_cart(request, item_id):
    item = MenuItem.objects.get(id=item_id)
    Cart.objects.create(user=request.user, item=item)
    return redirect('cart')


@login_required
def cart(request):
    items = Cart.objects.filter(user=request.user)
    total = sum(i.item.price * i.quantity for i in items)

    return render(request, 'cart.html', {
        'items': items,
        'total': total
    })
def signup(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')

    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})
def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember')

        # check email login
        try:
            user_obj = User.objects.get(email=username)
            username = user_obj.username
        except:
            pass

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if not remember:
                request.session.set_expiry(0)

            return redirect('profile')

    return render(request, 'login.html')
def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def profile(request):

    orders = Order.objects.filter(user=request.user)
   
    # ✅ get restaurants from ordered items
    restaurants = Restaurant.objects.filter(
        menuitem__order__user=request.user
    ).distinct()
    addresses = Address.objects.filter(user=request.user)
    return render(request, 'profile.html', {
        'orders': orders,
        'restaurants': restaurants,
        'addresses': addresses
    })

def account(request):

    if request.method == "POST" and "login_btn" in request.POST:

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("profile")

        else:
            return render(request, "account.html", {
                "error": "Invalid username or password"
            })

    return render(request, "account.html")
def search(request):

    query = request.GET.get('q')

    restaurants = []

    if query:
        restaurants = Restaurant.objects.filter(name__icontains=query)

    return render(request, 'search.html', {
        'restaurants': restaurants,
        'query': query
    })
def increase_quantity(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.quantity += 1
    cart.save()
    return redirect('cart')
def remove_item(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    return redirect('cart')

def decrease_quantity(request, cart_id):
    cart = Cart.objects.get(id=cart_id)

    if cart.quantity > 1:
        cart.quantity -= 1
        cart.save()

    return redirect('cart')
@login_required
def checkout(request):
    items = Cart.objects.filter(user=request.user)
    total = sum(i.item.price for i in items)

    if request.method == "POST":
        payment_method = request.POST.get("payment_method")

        # ✅ CASH ON DELIVERY
        if payment_method == "cod":
            for i in items:
                Order.objects.create(
                    user=request.user,
                    item=i.item,
                    total_price=i.item.price,
                    payment_method="COD"
                )

            items.delete()
            return redirect('profile')

        # ✅ ONLINE PAYMENT (RAZORPAY)
        elif payment_method == "online":
            client = razorpay.Client(
                auth=(settings.RAZORPAY_KEY, settings.RAZORPAY_SECRET)
            )

            payment = client.order.create({
                "amount": int(total * 100),  # ₹ → paise
                "currency": "INR",
                "payment_capture": 1
            })

            # store cart temporarily (session)
            request.session['cart_items'] = list(items.values_list('id', flat=True))

            return render(request, "payment.html", {
                "payment": payment,
                "razorpay_key": settings.RAZORPAY_KEY,
                "total": total
            })

    return render(request, 'checkout.html', {
        'items': items,
        'total': total
    })

def payment_success(request):
    item_ids = request.session.get('cart_items', [])
    items = Cart.objects.filter(id__in=item_ids)

    for i in items:
        Order.objects.create(
            user=request.user,
            item=i.item,
            total_price=i.item.price,
            payment_method="ONLINE"
        )

    items.delete()
    return redirect('profile')

def add_address(request):
    if request.method == "POST":
        address = request.POST.get('address')

        Address.objects.create(
            user=request.user,
            full_address=address
        )

        return redirect('profile')
    
def edit_address(request, address_id):
    address = Address.objects.get(id=address_id, user=request.user)

    if request.method == "POST":
        new_address = request.POST.get('address')
        address.full_address = new_address
        address.save()
        return redirect('profile')

    return render(request, 'edit_address.html', {'address': address})

def delete_address(request, address_id):
    address = Address.objects.get(id=address_id, user=request.user)
    address.delete()
    return redirect('profile')


def place_order(request):
    payment_method = request.POST.get('payment_method')

    if payment_method == 'cod':
        # Save order directly
        Order.objects.create(user=request.user, status="Placed")
        return redirect('success')

    elif payment_method == 'online':
        return redirect('razorpay_payment')
    

def razorpay_payment(request):
    client = razorpay.Client(
        auth=(settings.RAZORPAY_KEY, settings.RAZORPAY_SECRET)
    )

    payment = client.order.create({
        "amount": 50000,  # ₹500
        "currency": "INR",
        "payment_capture": 1
    })

    return render(request, "payment.html", {
        "payment": payment,
        "razorpay_key": settings.RAZORPAY_KEY
    })