from django.shortcuts import redirect

def check_login_and_redirect(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/ams/dashboard/')
        else:
            return view_func(request, *args, **kwargs)
    return _wrapped_view


def check_user_client_redirect(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_superuser and request.user.is_staff:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('/')
            
    return _wrapped_view