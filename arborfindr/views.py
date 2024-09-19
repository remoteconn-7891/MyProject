

from django.shortcuts import render, redirect

from django.views import View

from django.contrib.auth import update_session_auth_hash

from django.contrib.auth.forms import PasswordChangeForm

from django.contrib.auth import login, authenticate

from .forms import UserForm

from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .forms import UpdateProfilePic

from .models import Arborist

from haystack.generic_views import SearchView

from haystack.query import SearchQuerySet


def index(request):
    return render(request, "arborist_search.html", {})

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('register.html')  # index will be home page for now
    else:
        form = UserForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index.html') 
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

# View class for changing password

def update_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # To keep the user logged in
            return redirect('index.html')        
    else:
         form = PasswordChangeForm(request.user)
    return render(request, 'registration/update_password.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        p_form = UpdateProfilePic(request.POST,
                                  request.FILES,
                                  instance=request.user.homeowner)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your profile has been updated!')
            # Redirects to profile page
            return redirect('profile')
        

    return render(request, 'profile/user_profile.html')


class ArboristSearchView(SearchView):
    template_name = 'arborist_search.html'
    # Custom search view for the queryset
    queryset = SearchQuerySet().filter(arborist_city='Denver')
    