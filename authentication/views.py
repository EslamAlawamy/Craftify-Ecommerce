from django.shortcuts import render
from authentication.forms import UserRegistrationForm
from django.contrib.auth import login as  auth_login, authenticate
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

# Create your views here.

def signup(request):
    form = UserRegistrationForm(request.POST)
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            User = get_user_model()
            username = form.cleaned_data['email'].split('@')[0]  # Get the part of the email before the '@'
            User.objects.create(username=username, email=form.cleaned_data['email'], password=make_password(form.cleaned_data['password']))
            new_user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if new_user is not None:
                auth_login(request, new_user)
                messages.success(request, f'Account created for {form.cleaned_data["email"]}!')
                return redirect('core:index')
    else:
        form = UserRegistrationForm()

    context = {
        'form': form,
    }

    return render(request , 'pages/signup.html', context)