from django.shortcuts import render, redirect

def employee_panel_view(request):
    if not request.user.is_staff: return redirect('home-page')

    return render(request, 'employee/employee_panel.html')
