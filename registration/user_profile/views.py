from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from registration.views import LoginView
from registration.forms import RegisterForm
from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


# Create your views here.
class ProfileView(View):
    form_class = RegisterForm
    template_name = 'registration/profile.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        user = request.user
        if request.user.is_authenticated:
            if form.is_valid:
                return render(request, self.template_name, {'profile': user, 'form': form})
