from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.http import HttpResponse


#https://swarf00.github.io/2018/12/10/login.html
def sign_in(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'account/sign_in.html', {'form' : form})

class UserLoginView(LoginView):
    template_name = 'account/login.html'
    def from_invalid(self, form):
        message.error(self.request, '로그인에 실패했습니다.', extra_tage='danger')
        return super().form_invalid(form)

        