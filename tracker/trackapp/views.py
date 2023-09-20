from django.shortcuts import render , redirect
from django.http import HttpResponse
from .forms import Form
from .models import Track
from django.contrib.auth.decorators import user_passes_test


# views.py

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('piechart.html')  # Redirect to the dashboard page after login
        else:
            # Handle invalid login
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})

    return render(request, 'login.html')

# Create your views here.
def index(request):

    return render(request, "index.html")



def create(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            # Save the form with the current date and time
            obj = form.save()
            return render( request , 'view.html')  # Redirect to a success page
    else:
        form = Form()
    
    return render(request, 'create.html', {'form': form})



# myapp/views.py

# myapp/views.py

import matplotlib.pyplot as plt
from io import BytesIO
import base64
from django.shortcuts import render
from .models import Track
from django.db.models import Sum

def pie_chart(request):
    if request.user.is_superuser:

     plt.ioff()

     # Query the data from the Track model for category distribution
     data = Track.objects.values('category').annotate(total=Sum('amount'))
     labels = [item['category'] for item in data]
     amounts = [item['total'] for item in data]
   
     # Create the category distribution pie chart
     plt.figure(figsize=(12, 5))  # Increase the figure size to accommodate both charts
     plt.subplot(121)  # Create the first subplot (1 row, 2 columns, first plot)
     plt.pie(amounts, labels=labels, autopct='%1.1f%%')
     plt.title('Category Distribution')
     plt.axis('equal')

    # Query income and expenditure data
     income = Track.objects.filter(type='Income').aggregate(total=Sum('amount'))['total']
     expenditure = Track.objects.filter(type='Expenditure').aggregate(total=Sum('amount'))['total']

    # Create the income and expenditure pie chart
     plt.subplot(122)  # Create the second subplot (1 row, 2 columns, second plot)
     labels = ['Income', 'Expenditure']
     amounts = [income, expenditure]
     plt.pie(amounts, labels=labels, autopct='%1.1f%%')
     plt.title('Income vs. Expenditure')
     plt.axis('equal')

    # Convert the plot to an image
     buffer = BytesIO()
     plt.savefig(buffer, format='png')
     plt.close()

     chart = base64.b64encode(buffer.getvalue()).decode('utf-8')
     buffer.close()

     return render(request, 'pie_chart.html', {'chart': chart})
    else: 
        return render(request, 'access_denied.html')


def is_regular_user(user):
    return user.groups.filter(name='Regular Users').exists()

@user_passes_test(is_regular_user)
def dashboard(request):
    pass

@user_passes_test(is_regular_user)
def data_display(request):
    pass

@user_passes_test(is_regular_user)
def pie_chart(request):
    plt.ioff()

     # Query the data from the Track model for category distribution
    data = Track.objects.values('category').annotate(total=Sum('amount'))
    labels = [item['category'] for item in data]
    amounts = [item['total'] for item in data]
   
     # Create the category distribution pie chart
    plt.figure(figsize=(12, 5))  # Increase the figure size to accommodate both charts
    plt.subplot(121)  # Create the first subplot (1 row, 2 columns, first plot)
    plt.pie(amounts, labels=labels, autopct='%1.1f%%')
    plt.title('Category Distribution')
    plt.axis('equal')

    # Query income and expenditure data
    income = Track.objects.filter(type='Income').aggregate(total=Sum('amount'))['total']
    expenditure = Track.objects.filter(type='Expenditure').aggregate(total=Sum('amount'))['total']

    # Create the income and expenditure pie chart
    plt.subplot(122)  # Create the second subplot (1 row, 2 columns, second plot)
    labels = ['Income', 'Expenditure']
    amounts = [income, expenditure]
    plt.pie(amounts, labels=labels, autopct='%1.1f%%')
    plt.title('Income vs. Expenditure')
    plt.axis('equal')

    # Convert the plot to an image
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()

    chart = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()

    return render(request, 'pie_chart.html', {'chart': chart})