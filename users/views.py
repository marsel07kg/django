from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView
from . import models, forms

class RegistrationView(CreateView):
    form_class = forms.CustomRegistrationsForm
    template_name = 'users/registration.html'
    success_url = '/login/'

    def form_valid(self, form):
        responce = super().form_valid(form)
        status_of_reader = form.cleaned_data['status_of_reader']
        if status_of_reader == 'not_readers':
            self.object.literary_club = 'not_readers'
        elif status_of_reader == 'beginner':
            self.object.literary_club = 'beginner'
        elif status_of_reader == 'amateur':
            self.object.literary_club = 'amateur'
        elif status_of_reader == 'veteran':
            self.object.literary_club = 'veteran'
        else:
            self.object.literary_club = 'Клуб не определен'
        self.object.save()
        return responce



class AuthLoginView(LoginView):
    template_name = "users/login.html"
    form_class = AuthenticationForm

    def get_success_url(self):
        return reverse("users:user_list")

class AuthLogoutView(LogoutView):
    next_page = reverse_lazy('users:login')

class UserListView(ListView):
    template_name = 'users/user_list.html'
    context_object_name = 'users'
    models = models.CustomUser

    def get_queryset(self):
        return self.models.objects.filter().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['literary_club'] = getattr(self.request.user, 'literary_club', 'Клуб не определен')
        return context

# Create your views here.
