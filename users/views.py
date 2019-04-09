from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, CreateView

from users.models import Client


class SignUpView(CreateView):
    template_name = 'signup.html'
    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name)

    def post(self, request, *args, **kwargs):
        data = request.POST
        d = {}
        for key, value in data.items():
            d[key] = value


        del d['csrfmiddlewaretoken']
        del d['confirm_password']
        # d['username'] = d['email']
        if User.objects.filter(username= d['username']).count() or User.objects.filter(email=d['email']).count():
            error_data = {
                'error': 'Username or Email is already in use'
            }
            return render(request, self.template_name, context=error_data)
        else:
            user = Client.objects.create(**d)
            success = {
                'success': 'Successfully registered'
            }
            # email = EmailMessage(
            #             'hiii' , 'Please confirm', to=[d['username']]
            # )
            # email.send()
            return render(request, self.template_name, context=success)

class UserLoginView(LoginView):
    template_name = 'login_form.html'

    def get_success_url(self):
        return '/foods/home'


class UserLogoutView(LogoutView):

    def get_next_page(self):
        return '/foods/home'
