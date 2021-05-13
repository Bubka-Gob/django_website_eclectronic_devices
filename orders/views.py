from django.shortcuts import render, redirect
from django.http import Http404
from .forms import OrderForm
from .models import Order
from django.contrib import messages

def order_creation_view(request):
    if request.method == 'GET':
        form = OrderForm()
    else:
        form = OrderForm(request.POST)
        form.data._mutable = True
        form.data['client'] = request.user.id
        form.data._mutable = False
        if form.is_valid():
            form.save()
            messages.success(request, f'Закаказ {form.data.get("name")} Создан')
            return redirect('profile-page')
    return render(request, 'orders/creation.html')

def order_list_view(request):
    user_orders_current = Order.objects.filter(client=request.user.id, is_finished=False)
    user_orders_history = Order.objects.filter(client=request.user.id, is_finished=True)
    context = {'orders_current': user_orders_current, 'orders_history': user_orders_history}
    return render(request, 'orders/order_list.html', context)

def examples_view(request):
    return render(request, 'orders/examples.html')

def order_detail_view(request, order_id):
    try: order = Order.objects.get(id=order_id)
    except: raise Http404()
    if order.client.id != request.user.id: raise Http404()

    return render(request, 'orders/order_detail.html', {'object': order})