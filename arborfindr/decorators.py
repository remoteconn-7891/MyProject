from django.shortcuts import redirect


def homeowner_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.role_choices == 'homeowner':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('access-denied')


def company_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.role_choices == 'company':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('access-denied')

