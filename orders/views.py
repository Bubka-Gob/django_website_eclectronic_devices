from django.shortcuts import render, redirect
from django.http import Http404
from .forms import OrderForm, DeviceForm
from .models import Order, Device
from django.contrib import messages


def device_creation_view(request):
    if request.method == 'GET':
        form = DeviceForm()
    else:
        form = DeviceForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            if (request.POST['areaOptions'] == 'is_room'): form.is_room = True
            elif (request.POST['areaOptions'] == 'is_street'): form.is_street = True
            form.save()
            return redirect('order_creation-page', device_id = form.id)

    return render(request, 'orders/creation.html', {'form': form})


def device_from_example_view(request, device_id):
    if request.method == 'GET':
        device = Device.objects.get(id=device_id)
        form = DeviceForm(instance=device)
    else:
        form = DeviceForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            if (request.POST['areaOptions'] == 'is_room'):
                form.is_room = True
            elif (request.POST['areaOptions'] == 'is_street'):
                form.is_street = True
            form.save()
            return redirect('order_creation-page', device_id=form.id)

    return render(request, 'orders/creation.html', {'form': form})


def order_creation_view(request, device_id):
    if request.method == 'GET':
        form = OrderForm()
    else:
        form = OrderForm(request.POST)
        device = Device.objects.get(id=device_id)
        order = Order(address=form.data['address'], client=request.user, device=device)
        order.save()
        messages.success(request, f'Закаказ успешно оформлен, ожидайте звонка оператора')
        return redirect('profile-page')

    return render(request, 'orders/order_creation.html', {'form': form})


def order_list_view(request):
    user_orders_current = Order.objects.filter(client=request.user.id, is_finished=False)
    user_orders_history = Order.objects.filter(client=request.user.id, is_finished=True)
    context = {'orders_current': user_orders_current, 'orders_history': user_orders_history}
    return render(request, 'orders/order_list.html', context)


def examples_view(request):
    devices = Device.objects.filter(is_example=True)
    return render(request, 'orders/examples.html', {'devices': devices})


def order_detail_view(request, order_id):
    try: order = Order.objects.get(id=order_id)
    except: raise Http404()
    if order.client.id != request.user.id: raise Http404()

    return render(request, 'orders/order_detail.html', {'order': order})