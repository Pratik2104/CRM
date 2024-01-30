from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages
from .filters import OrderFilter
from users.decorators import *
from django.contrib.auth.decorators import *

# Create your views here.

@login_required
def home(request):
    groups = request.user.groups.all()
    for group in groups:
        if group.name=='Admin':
            return redirect('home_admin')
    return redirect('home_customer')

@login_required
@allowed_users(['Admin'])
def home_admin(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_orders = orders.count()
    orders_delivered = orders.filter(status='Delivered').count()
    orders_pending = orders.exclude(status='Delivered').count()
    context = {
            'customers' : customers,
            'orders' : orders,
            'total_orders_count' : total_orders,
            'orders_delivered_count' : orders_delivered,
            'orders_pending_count' : orders_pending,
            'user_is_admin' : True,
    }
    return render(request,'accounts/dashboard.html',context)

@login_required
@allowed_users(['Customer'])
def home_customer(request):
    orders = []
    orders = Order.objects.filter(customer__user=request.user)

    total_orders = orders.count()
    orders_delivered = orders.filter(status='Delivered').count()
    orders_pending = orders.exclude(status='Delivered').count()

    context = {
            'orders' : orders,
            'total_orders_count' : total_orders,
            'orders_delivered_count' : orders_delivered,
            'orders_pending_count' : orders_pending,
    }
    return render(request,'accounts/customer_dashboard.html',context)


@login_required
@allowed_users(['Admin'])
def products(request):
    products = Product.objects.all()
    context = {
            'products':products,
    }
    return render(request,'accounts/products.html',context)



@login_required
@allowed_users(['Admin'])
def customer(request,customer_id):
    customer = Customer.objects.get(pk=customer_id)
    customer_orders = customer.order_set.all()
    customer_orders_count = customer_orders.count()
    my_filter = OrderFilter(request.GET,queryset=customer_orders)
    customer_orders = my_filter.qs

    context = {
            'customer' : customer,
            'customer_orders' : customer_orders,
            'customer_orders_count' : customer_orders_count,
            'my_filter' : my_filter,
    }
    return render(request,'accounts/customer.html',context)



@login_required
@allowed_users(['Admin'])
def createOrder(request,customer_id):
    customer = Customer.objects.get(pk=customer_id)
    if request.method=='POST' :
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'New Order Created Sucessfully!')
            return redirect('customer',customer_id=customer_id)
    else :
        form = OrderForm(initial={'customer':customer})
        context = {
                'form' : form,
                'method' : 'Create',
        }
        return render(request,'accounts/order_form.html',context)



@login_required
@allowed_users(['Admin'])
def updateOrder(request,order_id):
    order = Order.objects.get(pk=order_id)

    if request.method=='POST' :
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            messages.success(request,'Order Updated Sucessfully!')
            return redirect('home')
    else :
        form = OrderForm(instance=order)
        context = {
                'form' : form,
                'method' : 'Update',
        }
        return render(request,'accounts/order_form.html',context)


@login_required
@allowed_users(['Admin'])
def deleteOrder(request,order_id):
    order = Order.objects.get(pk=order_id)
    if request.method == "POST":
        order.delete()
        messages.warning(request,'Order deleted Successfully!')
        return redirect('home')
    else :
        context = {
                'order' : order,
        }
        return render(request,'accounts/delete_order.html',context)


@login_required
@allowed_users(['Customer'])
def customerProfile(request):
    customer = request.user.customer
    if request.method == 'POST':
        profile_form = customerForm(request.POST,request.FILES,instance=customer)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request,"Your Profile have been Updated Successfully.")
            return redirect('customer_profile')
        else :
            messages.error(request,"Could not update your Profile. Please try again.")
    profile_form = customerForm(instance=customer)
    context = {
            'customer': customer,
            'profile_form' : profile_form,
    }
    return render(request,'accounts/customer_profile.html',context)
