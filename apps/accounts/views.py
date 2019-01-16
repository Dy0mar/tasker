# -*- coding: utf-8 -*-

from django.contrib.auth import (
    authenticate, login, login as auth_login, logout as auth_logout
)
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from accounts.forms import RegistrationForm, UserLoginForm


class AccountLoginView(LoginView):
    """ User login view """
    form_class = UserLoginForm
    template_name = 'account/login.html'
    redirect_authenticated_user = True

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        auth_login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(AccountLoginView, self).get_context_data(**kwargs)
        return context


def logout(request):
    """ User logout view """
    auth_logout(request)
    response = redirect('login')
    response['Cache-Control'] = 'no-cache'

    return response


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'account/register.html', {'form': form})
