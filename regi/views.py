from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect,HttpResponsePermanentRedirect, redirect
from django.contrib.auth.forms import UserCreationForm
# from .forms import SignUpForm, LoginForm, PostForm
# from .forms import SignUpForm, LoginForm,EditUserProfileForm
from .forms import SignUpForm, LoginForm
from django.contrib import messages
from django.contrib.auth import  authenticate,login,logout
from django import forms
from django.contrib.auth.models import Group
# from .forms import NewCommentForm, PostSearchForm
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
# import math
# from itertools import chain
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
# from math import random
from django.contrib.auth.decorators import login_required
# import time
# Create your views here.
from .forms import SignUpForm, UserForm, ProfileForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Profile, User
from django.views.generic import TemplateView, CreateView

from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import UserForm, ProfileForm
from django.contrib.auth.models import User
from django.dispatch import receiver

#logout________________________________________________________________________________________________
def user_logout(request):
    logout(request)
    # return HttpResponsePermanentRedirect('/')
    return HttpResponsePermanentRedirect(request.META.get('HTTP_REFERER', '/'))


#login________________________________________________________________________________________________
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request = request,data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname,password = upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in Successfully')
                    # return HttpResponsePermanentRedirect(request.META.get('HTTP_REFERER', '/'))
                    return HttpResponsePermanentRedirect(request.META.get('HTTP_REFERER', '/'))
                    # return redirect(request.META.get('HTTP_REFERER'))
        else:
            form = LoginForm()
        return render(request,'regi/login.html',{'form':form})
    else:
        return HttpResponseRedirect('/')


#signup________________________________________________________________________________________________
def user_signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                messages.success(request,'Signed Up successfully')
                user = form.save()
                return HttpResponseRedirect('/login/')
                # group = Group.objects.get(name ='Author')
                # user.groups.add(group)
        else:
            form = SignUpForm()
        return render(request,'regi/signup.html',{'form':form})
    else:
        return HttpResponseRedirect('/')

# def profile_view(request):
    
    
# user profile________________________________________________________________________________________________
# def user_profile(request):\
    
#     if request.user.is_authenticated:
#         if request.method == "POST":
#             fm  = EditUserProfileForm(request.POST, instance = request.user)
#             if fm.is_valid():
#                 messages.success(request,'Profile has been updated')
#                 fm.save()
#         else:
#             fm = EditUserProfileForm(instance= request.user)
#         return render(request,'regi/profile.html',{'name':request.user,'form':fm})
#     else:
#         return HttpResponseRedirect('/login/')

# change password________________________________________________________________________________________________
def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = PasswordChangeForm(user=request.user,data= request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,'Password changed successfully')
                return HttpResponseRedirect('/profile/')
        else:
            fm = PasswordChangeForm(user = request.user)
        return render(request,'regi/change_pass.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')




class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'regi/profile.html'

class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    user_form = UserForm
    profile_form = ProfileForm
    template_name = 'regi/profile-update.html'

    def post(self, request):

        post_data = request.POST or None
        file_data = request.FILES or None

        user_form = UserForm(post_data, instance=request.user)
        profile_form = ProfileForm(post_data, file_data, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return HttpResponseRedirect(reverse_lazy('profile'))

        context = self.get_context_data(
                                        user_form=user_form,
                                        profile_form=profile_form
                                    )

        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)