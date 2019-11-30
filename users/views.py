# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
#sadsaddsadsa

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, ("%s account has been created!" % username))
            return redirect('Main-main')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
