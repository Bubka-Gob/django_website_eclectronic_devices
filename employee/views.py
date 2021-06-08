from django.shortcuts import render, redirect
from orders.models import Order, EmployeeOrder
from .models import EmployeeModel
from orders.forms import OrderDocumentation, DeviceForm
from django.http import Http404
from django.contrib import messages


def orders_panel_view(request):
    if not request.user.is_staff: raise Http404()
    orders_current = Order.objects.raw("SELECT * FROM orders_order WHERE is_in_process = 1 AND id IN "
                                       "(SELECT order_id FROM orders_employeeorder "
                                       "WHERE is_operator = 1 AND employee_id = %s)",
                                       [request.user.employee.id])
    orders_new = Order.objects.filter(is_in_process=False, is_finished=False)
    orders_in_process = Order.objects.raw("SELECT * FROM orders_order WHERE is_in_process=1 AND id IN "
                                          "(SELECT order_id FROM orders_employeeorder WHERE is_operator=1) AND id NOT IN"
                                          "(SELECT order_id FROM orders_employeeorder WHERE employee_id = %s)",
                                          [request.user.employee.id])
    orders_finished = Order.objects.filter(is_finished=True)
    context = {'orders_current': orders_current,
               'orders_new': orders_new,
               'orders_in_process': orders_in_process,
               'orders_finished': orders_finished}

    return render(request, 'employee/orders_panel.html', context)


def employee_order_view(request, order_id):
    if not request.user.is_staff: raise Http404()
    try: order = Order.objects.get(id=order_id)
    except: raise Http404()

    if request.method == 'POST':
        form = OrderDocumentation(request.POST, request.FILES, instance=order)
        if form.is_valid():
            form.save()

    return render(request, 'employee/employee_order.html', {'order': order})


def device_redact_view(request, order_id):
    if not request.user.is_staff: raise Http404()
    try: order = Order.objects.get(id=order_id)
    except: raise Http404()
    form = DeviceForm(instance=order.device)
    return render(request, 'employee/device_redact.html', {'form': form})


def order_accept_view(request, order_id):
    if not request.user.is_staff: raise Http404()
    try: order = Order.objects.get(id=order_id)
    except: raise Http404()
    order.is_in_process = True
    order.save()

    connection = EmployeeOrder(employee=request.user.employee, order=order, is_operator=True)
    connection.save()
    return redirect('employee_order-page', order_id=order_id)


def order_finish_view(request, order_id):
    if not request.user.is_staff: raise Http404()
    try: order = Order.objects.get(id=order_id)
    except: raise Http404()
    if order.spec_document:
        order.is_in_process = False
        order.is_finished = True
        order.save()
    else:
        messages.warning(request, f'Техническое задание не сформировано')
    return redirect('orders_panel-page')


def employee_managing_view(request, order_id):
    if not request.user.is_staff: raise Http404()
    try: order = Order.objects.get(id=order_id)
    except: raise Http404()
    added_elements = []
    other_elements = []
    added = EmployeeModel.objects.raw('SELECT * FROM employee_employeemodel WHERE id IN '
                                      '(SELECT employee_id FROM orders_employeeorder WHERE '
                                      'order_id = %s)', [order.id])
    other = EmployeeModel.objects.raw('SELECT * FROM employee_employeemodel WHERE id NOT IN '
                                      '(SELECT employee_id FROM orders_employeeorder WHERE '
                                      'order_id = %s)', [order.id])
    for employee in added:
        works = Order.objects.raw('SELECT * FROM orders_order WHERE id IN'
                                  '(SELECT order_id FROM orders_employeeorder WHERE '
                                  'employee_id = %s)', [employee.id])
        added_elements.append([employee, works, True])
    for employee in other:
        works = Order.objects.raw('SELECT * FROM orders_order WHERE id IN'
                                  '(SELECT order_id FROM orders_employeeorder WHERE '
                                  'employee_id = %s)', [employee.id])
        other_elements.append([employee, works, False])

    context = {'order': order, 'added_elements': added_elements, 'other_elements': other_elements}
    return render(request, 'employee/employees_adding.html', context)


def employee_adding_view(request, order_id, employee_id):
    if not request.user.is_staff: raise Http404()
    order = Order.objects.get(id=order_id)
    employee = EmployeeModel.objects.get(id=employee_id)
    connection = EmployeeOrder(order=order, employee=employee)
    connection.save()
    return redirect('employee_managing-page', order_id=order_id)


def employee_removing_view(request, order_id, employee_id):
    if not request.user.is_staff: raise Http404()
    connection = EmployeeOrder.objects.get(order=order_id, employee=employee_id)
    connection.delete()
    return redirect('employee_managing-page', order_id=order_id)