
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm, UserLoginForm, AdminLoginForm, AppForm

from .models import User, Admin, App
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserLoginForm, AdminLoginForm, ScreenshotUploadForm
from django.db import connections



def home(request):
    return render(request, './home.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Hash the password before saving
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save(using='user_db')  # Save user in 'user_db'
            messages.success(request, 'Registration successful! Please log in.')
            return redirect('user_login')
        else:
            messages.error(request, 'Error during registration. Please try again.')
    else:
        form = RegistrationForm()
    
    return render(request, './register.html', {'form': form})

def user_login(request):
    error = None
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            user = User.objects.using('user_db').get(email=email)
            if check_password(password, user.password):
                # Store username in session
                request.session['username'] = user.username
                messages.success(request, 'Login successful!')
                return redirect('dashboard')
            else:
                error = 'Invalid Credentials'
        except User.DoesNotExist:
            error = 'Invalid Credentials'

    return render(request, './home.html', {'error': error})


def dashboard(request):
    # Get the username from session, default to 'Guest' if not set
    username = request.session.get('username', 'Guest')
    
    # Fetch all app data from the App table
    apps = App.objects.all()
    
    return render(request, './dashboard.html', {
        'username': username,
        'apps': apps
    })

def logout_user(request):
    # Clear the session
    request.session.flush()
    # Redirect to the main page (assuming your main page is named 'home')
    return redirect('home')


def upload_screenshot(request, app_id):
    app = get_object_or_404(App, id=app_id)

    if request.method == 'POST':
        form = ScreenshotUploadForm(request.POST, request.FILES, instance=app)
        if form.is_valid():
            form.save()  # Save to the correct DB
            messages.success(request, 'Screenshot uploaded successfully!')
        else:
            messages.error(request, 'Failed to upload screenshot. Please try again.')
    
    return redirect('dashboard')
# def admin_login(request):
    # if request.method == 'POST':
    #     form = AdminLoginForm(request.POST)
    #     if form.is_valid():
    #         username = form.cleaned_data['username']
    #         password = form.cleaned_data['password']
    #         try:
    #             admin = Admin.objects.using('admin_db').get(username=username)
    #             if admin.password == password:
    #                 return redirect('admin_dashboard')  # Define an admin dashboard
    #             else:
    #                 messages.error(request, 'Invalid password')
    #         except Admin.DoesNotExist:
    #             messages.error(request, 'Admin not found')
    # else:
    #     form = AdminLoginForm()

    # return render(request, 'accounts/login.html', {'form': form})


def admin_login(request):
    error = None
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        if email == "durgesh@gmail.com" and password == "123456":
            messages.success(request, 'Admin Login successful!')
            return redirect('admin_dashboard')  # Redirect to admin dashboard or home
        else:
            error = 'Invalid Admin Credentials'

    return render(request, 'home.html', {'error': error})


# def admin_dashboard(request):
#     if request.method == 'POST':
#         form = AppForm(request.POST, request.FILES)
#         if form.is_valid():
#             app_instance = form.save(commit=False)  # Create object but don't save yet
#             app_instance.save(using='admin_db')     # Save to admin_db
#             messages.success(request, 'App added successfully!')
#             return redirect('admin_dashboard')
#         else:
#             messages.error(request, 'Error adding app. Please try again.')
#     else:
#         form = AppForm()
#     return render(request, './admin_dashboard.html', {'form': form})



def admin_dashboard(request):
    if request.method == 'POST':
        app_name = request.POST['app_name']
        app_link = request.POST['app_link']
        category = request.POST['category']
        sub_category = request.POST['sub_category']
        points = request.POST['points']
        app_image = request.FILES.get('app_image')  # Handle file upload

        # Create App object and save to admin_db
        app = App(
            app_name=app_name,
            app_link=app_link,
            category=category,
            sub_category=sub_category,
            points=points,
            app_image=app_image
        )
        app.save()  # Explicitly save to admin_db
        messages.success(request, 'App added successfully!')
        return redirect('admin_dashboard')
    
    return render(request, './admin_dashboard.html')

