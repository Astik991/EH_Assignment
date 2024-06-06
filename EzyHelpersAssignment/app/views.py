from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Helper, Customer, Assignment
from .forms import HelperForm, CustomerForm, AssignmentForm

def add_helper(request):
    if request.method == 'POST':
        form = HelperForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Helper added successfully!')
            return redirect('list_helpers')
        else:
            messages.error(request, 'Failed to add helper. Please correct the errors below.')
    else:
        form = HelperForm()
    return render(request, 'app/add_helper.html', {'form': form})

def list_helpers(request):
    helpers = Helper.objects.all()
    return render(request, 'app/list_helpers.html', {'helpers': helpers})

def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer added successfully!')
            return redirect('list_customers')
        else:
            messages.error(request, 'Failed to add customer. Please correct the errors below.')
    else:
        form = CustomerForm()
    return render(request, 'app/add_customer.html', {'form': form})

def list_customers(request):
    customers = Customer.objects.all()
    return render(request, 'app/list_customers.html', {'customers': customers})

def add_assignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Assigned successfully!')
            return redirect('list_helpers')
        else:
            messages.error(request, 'Failed to add assignment. Please correct the errors below.')
    else:
        form = AssignmentForm()
    return render(request, 'app/add_assignment.html', {'form': form})

def list_free_helpers(request):
    assigned_helpers = Assignment.objects.values_list('helper', flat=True)
    free_helpers = Helper.objects.exclude(id__in=assigned_helpers)
    return render(request, 'app/list_free_helpers.html', {'helpers': free_helpers})
