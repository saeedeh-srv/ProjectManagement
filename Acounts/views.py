from django.contrib.messages import success
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import views as auth_views, login, logout
from django.template.context_processors import request
from .forms import UserLoginForm, UserRegisterForm, UserprofileForm
from django.contrib import messages
from django.views.generic import View
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls.base import reverse_lazy


class RegisterUser(View):
    form_class = UserRegisterForm
    template_name = 'Acounts/register.html'

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name, {'form': self.form_class})

    def post(self, *args, **kwargs):
        form = self.form_class(self.request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            user = User.objects.create_user(username=data['username'], first_name=data['first_name'],
                                            last_name=data['last_name'], email=data['email'],
                                            password=data['password_1'])
            Profile.objects.create(user=user, phone=data['phone_number'], )
            login(self.request, user)
            messages.success(self.request, f"you are log in", 'success')
            return redirect('accounts:user_profile')
        return render(self.request, self.template_name, {'form': form})


class LoginUser(auth_views.LoginView):
    form_class = UserLoginForm
    template_name = 'Acounts/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('accounts:user_profile')
        return super().dispatch(request, *args, **kwargs)

    def form_invalid(self, form):
        remember = form.cleaned_data['remember']
        if remember:
            self.request.session.set_expiry(172000)
        else:
            self.request.session.set_expiry(0)
        self.request.session.modified = True
        messages.success(self.request, f"you log in", 'success')
        return super(LoginUser, self).form_invalid(form)


class LogoutUser(View):
    def get(self, request):
        logout(request)
        messages.success(self.request, f"you log out", 'success')
        return redirect("accounts:user_login")


class ProfileUser(View):
    def get(self, *args, **kwargs):
        request = self.request
        profile = get_object_or_404(Profile, user=request.user)
        return render(self.request, 'Acounts/profile.html', {'profile': profile})


class ChangePassword(SuccessMessageMixin, PasswordChangeView):
    template_name = 'Acounts/change_password.html'
    success_message = "your password changed"
    success_url = reverse_lazy('accounts:user_profile')


class UpdateProfile(View):
    template_name = 'Acounts/updateprofile.html'

    def get(self, request, *args, **kwargs):
        form = UserprofileForm(instance=request.user)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = UserprofileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'your profile updated')
            return redirect('accounts:user_profile')
        return render(request, self.template_name, {"form": form})
