import secrets

from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from users.forms import UserRegisterForm
from users.models import User

from config.settings import EMAIL_HOST_USER


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = self.request.buid_absolute_uri(reverse('users:email-confirm', args=(user.token,)))
        # url = f'http://{host}/users/email.confirm/{token}'
        send_mail(
            subject='Подтверждение почты',
            message=f'Для подтверждения почты перейдите по ссылке: {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


class GeneratePasswordView(PasswordResetView):
    form_class = PasswordResetForm
    template_name = 'users/reset_password.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):

        user = User.objects.filter(email=form.cleaned_data['email']).first()
        if user:
            new_password = User.objects.make_random_password()
            user.set_password(new_password)
            user.save()
        user.email_user(
            subject='Смена пароля',
            message=f'Ваш новый пароль: {new_password}',
        )
        return redirect(reverse('users:login'))

        # email = form.cleaned_data['email']
        # user = User.objects.get(email=email)
        # if user:
        #     password = secrets.token_hex(10)
        #     user.set_password(password)
        #     user.save()
        # send_mail(
        #     subject='Смена пароля',
        #     message=f'Ваш новый пароль: {password}',
        #     from_email=EMAIL_HOST_USER,
        #     recipient_list=[user.email]
        # )
        # return redirect(reverse('users:login'))


# def recovery_pass(request):
#     chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
#     new_password = ''
#     for i in range(10):
#         new_password += random.choice(chars)
#
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         user = get_object_or_404(User, email=email)
#         password = new_password
#         user.set_password(password)
#         user.save()
#         send_mail(
#             subject='Восстановление пароля',
#             message=f'Сгенерирован новый пароль: {user.password}',
#             from_email=EMAIL_HOST_USER,
#             recipient_list=[user.email]
#         )
#         return redirect(reverse('users:login'))
#     return render(request, 'users/reset_password.html')


