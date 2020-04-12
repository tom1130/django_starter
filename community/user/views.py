from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import User
from .forms import LoginForm
# Create your views here.
# 로그아웃은 user_id를 지우면 된다;;
def home(request):
    # user_id = request.session.get('user')
    # if user_id:
    #     my_user = User.objects.get(pk=user_id)

    return render(request,'home.html')


def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    
    return redirect('/')

def login(request):
    # if request.method=='GET':
    #     return render(request,'login.html')
    # elif request.method=='POST':
    #     username = request.POST.get('username',None)
    #     password = request.POST.get('password',None)

    #     response_data = {}
    #     if not (username and password):
    #         response_data['error']='모든 값을 입력해야합니다'
    #     else:
    #         my_user = User.objects.get(username=username)
    #         if check_password(password,my_user.password):
    #             # 비밀번호 인식 후의 공간
    #             request.session['user']=my_user.id
    #             return redirect('/') # 만드는 사이트의 root로 이동
                
    #         else:
    #             response_data['error']='비밀번호가 틀렸습니다'
    #     return render(request,'login.html',response_data)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/')
    else:
        form = LoginForm()
    return render(request,'login.html',{'form':form})

def register(request):
    if request.method =='GET':
        return render(request,'register.html')
    elif request.method =='POST':
        username = request.POST.get('username',None)
        useremail= request.POST.get('useremail',None)
        password = request.POST.get('password',None)
        re_password = request.POST.get('re-password',None)

        response_data = {}
        # 비밀번호 확인
        if not (username and useremail and password and re_password):
            response_data['error']='모든 값을 입력해야합니다'
        if password != re_password: # true이면 에러 메시지 반환
            response_data['error']='비밀번호가 다릅니다'
        else:
            my_user = User(
                username = username,
                useremail = useremail,
                password = make_password(password)
            )

            my_user.save()

        return render(request,'register.html',response_data)
        