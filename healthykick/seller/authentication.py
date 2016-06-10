from functools import wraps
from django.utils.decorators import available_attrs
from django.shortcuts import get_object_or_404, render


def user_passes_test(login_url=None, redirect_field_name=None):
    """
    Decorator for views that checks that the user passes the given test,
    redirecting to the log-in page if necessary. The test should be a callable
    that takes the user object and returns True if the user passes.
    """

    def decorator(view_func):
        @wraps(view_func, assigned=available_attrs(view_func))
        def _wrapped_view(request, *args, **kwargs):
            if request.session.get('email', False):
                return view_func(request, *args, **kwargs)
            else:
                return render(request, 'seller/home.html')
        return _wrapped_view
    return decorator


def login_required(function=None, login_url=None):
    """
    Decorator for views that checks that the user is logged in, redirecting
    to the log-in page if necessary.
    """
    actual_decorator = user_passes_test(
        login_url=login_url,
        redirect_field_name='/seller/'
    )
    if function:
        return actual_decorator(function)
    return actual_decorator