from django.shortcuts import redirect,render
from django.contrib import messages
from django.http import HttpResponse

def unauthenticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated :
            messages.error(request,"You are already logged in!")
            return redirect('home')
        else :
            return view_func(request,*args,**kwargs)
    return wrapper_func



def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request,*args,**kwargs):
            groups = request.user.groups.all()
            for group in groups :
                if group.name in allowed_roles :
                    return view_func(request,*args,**kwargs)

            return HttpResponse(render(request,'users/unauthorised.html'),status=401)
        return wrapper_func
    return decorator


# def admin_only(view_func):
#     def wrapper_func(request,*args,**kwargs):
#         groups = request.user.groups.all()
#         for group in groups :
#             if group=='Admin':
#                 return view_func(request,*args,**kwargs)
#
#         return redirect('home_customer')
#     return wrapper_func
