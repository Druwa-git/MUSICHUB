from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from common.forms import UserForm
# Create your views here.

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            #cleaned_data.get은 회원가입창에서 얻은 값들을 대입하기 위함.
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            #회원가입 완료후 자동으로 로그인이 되도록 만듦.
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})
