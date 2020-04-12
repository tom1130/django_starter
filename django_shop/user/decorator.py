from django.shortcuts import redirect
from .models import User

def login_required(function):
    def wrap(request,*args,**kwargs):
        my_user = request.session.get('user')
        if my_user is None or not my_user:
            return redirect('/login')
        return function(request,*args,**kwargs)
    
    return wrap

def admin_required(function):
    def wrap(request,*args,**kwargs):
        my_user = request.session.get('user')
        if my_user is None or not my_user:
            return redirect('/login')

        my_user = User.objects.get(email=my_user)
        if my_user.level != 'admin':
            return redirect('/')            
        return function(request,*args,**kwargs)
    
    return wrap