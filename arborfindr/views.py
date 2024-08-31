import json

from django.core.paginator import Paginator

from django.core.serializers import serialize

from django.http import JsonResponse

from django.shortcuts import render, redirect

from django.views import View

from django.contrib.auth import update_session_auth_hash

from django.contrib.auth.forms import PasswordChangeForm

from django.http import HttpResponse

from django.contrib.auth import login, authenticate

from .forms import UserForm

from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .forms import UpdateProfilePic

from .models import Arborist


def index(request):
    return render(request, "index.html", {})

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

class ListTopArborists(View):
    # page limit set to 10
    page_limit = 10

    '''
    Methods that get pagination context
    from queryset of the page number
    queryset: Filter the object from the model Arborist
    page: page with page number
    limit: the list of results per page
    '''

    def get_paginated_context(self, queryset, page, limit):
        if not page:
            page = 1  # set default page to 1

        # set specified limit page
        if limit:
            self.page_limit = limit

        # instantiate the paginator object with queryset
        paginator = Paginator(queryset, self.page_limit)
        # get the page object
        page_obj = paginator.get_page(page)
        # serialize the objects to json
        serialized_page = serialize("json", page_obj.object_list)
        # get only required fields from the serialized_page
        serialized_page = [obj["fields"] for obj in json.loads(serialized_page)]

        # return the context
        return {
            "data": serialized_page,
            "pagination": {
                "page": page,
                "limit": limit,
                "has_next": page_obj.has_next(),
                "has_prev": page_obj.has_previous(),
                "total": queryset.count()
            }
        }
    
    # GET method to queryset parameters from model
    def get(self, request, *args, **kwargs):
        # parameters for queryset
        page = request.GET.get('page')
        limit = request.GET.get('limit')
        business = request.GET.get('business')
        location = request.GET.get('location')
        services_type = request.GET.get('services_type')
        reviews = request.GET.get('reviews')
        years_experience = request.GET.get('years_experience')
        price = request.GET.get('price')
        sort_by = request.GET.get('sort_by')

        # query the whole db
        queryset = Arborist.objects.all()

        # start to filter out queryset based on object parameters
        # filter out business params
        if business and business != "all":
            queryset = queryset.filter(business=business)

        if location and location != "all":
            queryset = queryset.filter(location=location)

        if services_type and services_type != "all":
            queryset = queryset.filter(services_type=services_type)

        if reviews and reviews != "all":
            queryset = queryset.filter(reviews=reviews)

        if years_experience and years_experience != "all":
            queryset = queryset.filter(years_experience=years_experience)

        if price and price != "all":
            queryset = queryset.filter(price=price)

        # sorting queryset
        if sort_by and sort_by != "0":
            queryset = queryset.order_by(sort_by)

        to_return = self.get_paginated_context(queryset, page, limit)
        return JsonResponse(to_return, status=200)
    
    
def profile(request):
    profile = request.user.profile
    return render(request, 'profile/user_profile.html', {'profile': profile})


@login_required

def profile(request):
    if request.method == 'POST':
        p_form = UpdateProfilePic(request.POST,
                                  request.FILES,
                                  instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your profile has been updated!')
            # Redirects to profile page
            return redirect('profile')
        

    return render(request, 'profile/user_profile.html')
