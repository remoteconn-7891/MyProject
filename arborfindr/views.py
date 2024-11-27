from django.shortcuts import redirect

from django.contrib.auth import update_session_auth_hash

from django.contrib.auth.forms import PasswordChangeForm

from django.contrib.auth import login, authenticate

from .models import ArboristReview

from .forms import UserForm, HomeownerUserForm, ArboristCompanyForm

from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.decorators import login_required

from haystack.generic_views import SearchView

from .models import ArboristCompany

from django.shortcuts import render

from .forms import ReviewForm

from django.http import JsonResponse

from django.utils import timezone

from django.db.models import Prefetch

def review(request):
    return render(request, 'search_index/arborfindr/search_arborist.html')

@login_required
def arbor_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.reviewed_on = timezone.now()
            review.save()
            return redirect('arborfindr:search_arborist')
    else:
        form = ReviewForm()
    return render(request, 'search_index/arborfindr/arbor_review.html', {'form': form})
def autocomplete(request):
    if 'q' in request.GET:
        query = request.GET['q']
        results = ArboristCompany.objects.filter(company_name__icontains=query)
        suggestions = [result.company_name for result in results]
        return JsonResponse(suggestions, safe=False)
    return JsonResponse([], safe=False)


class ArboristSearchView(SearchView):
    template_name = 'search_index/arborfindr/search_arborist.html'

    def get_queryset(self):
        queryset = super().get_queryset().models(ArboristCompany)
        reviews = ArboristReview.objects.all()
        queryset = queryset.prefetch_related(Prefetch('arboristreview_set', queryset=reviews, to_attr='reviews'))

        return queryset


def index(request):
    return render(request, 'search_index/arborfindr/search_arborist.html', {})


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('search_index/arborfindr/search_arborist.html')  # index will be home page for now
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
                return redirect('search_index/arborfindr/search_arborist.html')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def update_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # To keep the user logged in
            return redirect('search_index/arborfindr/search_arborist.html')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/update_password.html', {'form': form})

@login_required
def homeowner_profile(request):
    profile = request.user.profile
    return render(request,'/profile/homeowner_profile.html', {'homeowner_profile': homeowner_profile})

@login_required
def company_profile(request):
    profile = request.user.profile
    return render(request, 'profile/company_profile.html', {'profile': profile})

@login_required
def edit_homeowner_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = HomeownerUserForm(request.POST, request.FILES, instance = profile)
        if form.is_valid():
            form.save()
            return redirect('search_index/arborfindr/search_arborist.html')

        else:
            form = HomeownerUserForm(instance = profile)
        return render(request, 'profile/edit_homeowner_profile', {'form': form})

@login_required
def edit_company_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ArboristCompanyForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('search_index/arborfindr/search_arborist.html')

        else:
            form = ArboristCompanyForm(instance=profile)
        return render(request, 'profile/edit_company_profile', {'form': form})
