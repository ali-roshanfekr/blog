import logging

from django.contrib.auth import login, logout
from django.http import Http404
from django.shortcuts import render, redirect
from django.views import View
from .forms import *
from .models import UserModel
from django.utils.crypto import get_random_string
from utils.utils import *
from site_setting_module.models import BackGroundModel

from kavenegar import *

global_phone = global_username = None


class LogInView(View):
    def get(self, request):
        try:
            form = LogInForm()

            return render(request, 'login.html', {
                'form': form,
                'back_ground': BackGroundModel.objects.filter(is_active=True).first(),
            })

        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error(f'This is an error message: {e}')

            return redirect('error')

    def post(self, request):
        try:
            form = LogInForm(request.POST)
            if form.is_valid():
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = UserModel.objects.filter(username=username).first()
                if user is None:
                    user = UserModel.objects.filter(phone=username).first()

                if user is None:
                    form = LogInForm()

                    return render(request, 'login.html', {
                        'form': form,
                        'back_ground': BackGroundModel.objects.filter(is_active=True).first(),
                        'incorrect_username': True,
                    })

                else:
                    if user.check_password(raw_password=password):
                        login(request, user)

                        return redirect('index')

                    else:
                        form = LogInForm()

                        return render(request, 'login.html', {
                            'form': form,
                            'back_ground': BackGroundModel.objects.filter(is_active=True).first(),
                            'incorrect_password': True,
                        })

            else:
                form = LogInForm()

                return render(request, 'login.html', {
                    'form': form,
                    'back_ground': BackGroundModel.objects.filter(is_active=True).first(),
                    'incorrect_format': True,
                })

        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error(f'This is an error message: {e}')

            return redirect('error')


class RegisterView(View):
    def get(self, request):
        try:
            form = UserForm()

            return render(request, 'register.html', {
                'form': form,
                'back_ground': BackGroundModel.objects.filter(is_active=True).first(),
            })

        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error(f'This is an error message: {e}')

            return redirect('error')

    def post(self, request):
        try:
            form = UserForm(request.POST)
            if form.is_valid():
                username = form['username'].value()
                phone = form['phone'].value()
                password = form['password1'].value()
                active_code = creat_random_code(6)
                token = get_random_string(100)
                request.session['user_token'] = token
                user = UserModel.objects.create_user(username=username, phone=phone,
                                                     active_code=active_code, token=token)
                user.set_password(raw_password=str(password))
                user.save()

                api = KavenegarAPI(
                    '376C2F4B51734A3643366A655A714E7570465263614775394644333773537570644C5234666571566548673D')
                params = {
                    'sender': '2000660110',
                    'receptor': f'{phone}',
                    'message': f'Your OTP is: {active_code}',
                }
                api.sms_send(params)

                return redirect('activation')

            else:
                form = UserForm()

                return render(request, 'register.html', {
                    'form': form,
                    'back_ground': BackGroundModel.objects.filter(is_active=True).first(),
                })

        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error(f'This is an error message: {e}')

            return redirect('error')


class ActivationView(View):
    def get(self, request):
        try:
            try:
                token = request.session['user_token']

            except:
                token = None

            user = UserModel.objects.filter(token=token).first()
            if user is not None:

                return render(request, 'activation.html', {
                    'back_ground': BackGroundModel.objects.filter(is_active=True).first(),
                })

            else:

                raise Http404

        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error(f'This is an error message: {e}')

            return redirect('error')

    def post(self, request):
        try:
            try:
                token = request.session['user_token']

            except:
                token = None

            user = UserModel.objects.filter(token=token).first()
            if user is not None:
                active_code = request.POST.get('active_code')
                if user.active_code == active_code:
                    login(request, user)

                    return redirect('index')

                else:

                    return render(request, 'activation.html', {
                        'back_ground': BackGroundModel.objects.filter(is_active=True).first(),
                        'incorrect': True
                    })

            else:

                raise Http404

        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error(f'This is an error message: {e}')

            return redirect('error')


class ForgetPasswordView(View):
    def get(self, request):
        try:
            form = ForgetPassForm()

            return render(request, 'forget_pass.html', {
                'form': form,
                'back_ground': BackGroundModel.objects.filter(is_active=True).first(),
            })

        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error(f'This is an error message: {e}')

            return redirect('error')

    def post(self, request):
        try:
            form = ForgetPassForm(request.POST)
            if form.is_valid():
                phone = form.cleaned_data.get('phone')
                user = UserModel.objects.filter(phone=phone).first()

                if user is None:
                    form = ForgetPassForm()

                    return render(request, 'forget_pass.html', {
                        'form': form,
                        'back_ground': BackGroundModel.objects.filter(is_active=True).first(),
                        'incorrect_phone': True,
                    })

                else:
                    active_code = creat_random_code(6)
                    token = get_random_string(100)
                    user.active_code = active_code
                    user.token = token
                    request.session['user_token'] = token
                    user.save()

                    api = KavenegarAPI(
                        '376C2F4B51734A3643366A655A714E7570465263614775394644333773537570644C5234666571566548673D')
                    params = {
                        'sender': '2000660110',
                        'receptor': f'{phone}',
                        'message': f'Your OTP is: {active_code}',
                    }
                    api.sms_send(params)

                    return redirect('forget_pass_activation')


            else:
                form = ForgetPassForm()

                return render(request, 'forget_pass.html', {
                    'form': form,
                    'back_ground': BackGroundModel.objects.filter(is_active=True).first(),
                    'incorrect': True,
                })

        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error(f'This is an error message: {e}')

            return redirect('error')


class ForgetPassActivationView(View):
    def get(self, request):
        try:
            try:
                token = request.session['user_token']

            except:
                token = None

            user = UserModel.objects.filter(token=token).first()
            if user is not None:

                return render(request, 'activation.html', {
                    'back_ground': BackGroundModel.objects.filter(is_active=True).first(),
                })

            else:

                raise Http404

        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error(f'This is an error message: {e}')

            return redirect('error')

    def post(self, request):
        try:
            try:
                token = request.session['user_token']

            except:
                token = None

            user = UserModel.objects.filter(token=token).first()
            if user is not None:
                active_code = request.POST.get('active_code')
                if user.active_code == active_code:

                    return redirect('change_password')

                else:

                    return render(request, 'activation.html', {
                        'back_ground': BackGroundModel.objects.filter(is_active=True).first(),
                        'incorrect': True
                    })

            else:

                raise Http404

        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error(f'This is an error message: {e}')

            return redirect('error')


class ChangePasswordView(View):
    def get(self, request):
        try:
            try:
                token = request.session['user_token']

            except:
                token = None

            user = UserModel.objects.filter(token=token).first()
            if user is not None:
                form = ChangePassForm()

                return render(request, 'change_password.html', {
                    'form': form,
                    'back_ground': BackGroundModel.objects.filter(is_active=True).first(),
                })

            else:

                raise Http404

        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error(f'This is an error message: {e}')

            return redirect('error')

    def post(self, request):
        try:
            try:
                token = request.session['user_token']

            except:
                token = None

            user = UserModel.objects.filter(token=token).first()
            if user is not None:
                form = ChangePassForm(request.POST)
                if form.is_valid():
                    password1 = form['password1'].value()
                    user.set_password(raw_password=password1)
                    user.save()
                    login(request, user)

                    return redirect('index')

                else:
                    form = ChangePassForm()

                    return render(request, 'change_password.html', {
                        'form': form,
                        'back_ground': BackGroundModel.objects.filter(is_active=True).first(),
                        'incorrect': True,
                    })

            else:

                raise Http404

        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error(f'This is an error message: {e}')

            return redirect('error')


def log_out(request):
    try:
        logout(request)

        return redirect('index')

    except Exception as e:
        error_logger = logging.getLogger('error_logger')
        error_logger.error(f'This is an error message: {e}')

        return redirect('error')


class ProfileView(View):
    def get(self, request):
        try:
            user = request.user
            if user.is_authenticated:
                form = ProfileForm(instance=user)

                return render(request, 'profile.html', {
                    'form': form,
                    'back_ground': BackGroundModel.objects.filter(is_active=True).first(),
                })

            else:

                raise Http404

        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error(f'This is an error message: {e}')

            return redirect('error')

    def post(self, request):
        try:
            global global_username, global_phone

            user = request.user
            phone = user.phone
            if user.is_authenticated:
                form = ProfileForm(request.POST or None, instance=user)
                if form.is_valid():
                    if form['phone'].value() == phone:
                        user.username = form['username'].value()
                        user.save()

                        return redirect('profile')

                    else:
                        global_phone = form['phone'].value()
                        global_username = form['username'].value()
                        active_code = creat_random_code(6)
                        token = get_random_string(100)
                        user.active_code = active_code
                        user.token = token
                        user.phone = phone
                        request.session['user_token'] = token
                        user.save()

                        api = KavenegarAPI(
                            '376C2F4B51734A3643366A655A714E7570465263614775394644333773537570644C5234666571566548673D')
                        params = {
                            'sender': '2000660110',
                            'receptor': f'{global_phone}',
                            'message': f'Your OTP is: {active_code}',
                        }
                        api.sms_send(params)

                        return redirect('profile_activation')

                else:
                    form = ProfileForm(instance=user)

                    return render(request, 'profile.html', {
                        'form': form,
                        'back_ground': BackGroundModel.objects.filter(is_active=True).first(),
                        'error': True
                    })

            else:

                raise Http404

        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error(f'This is an error message: {e}')

            return redirect('error')


class ProfileActivationView(View):
    def get(self, request):
        try:
            try:
                token = request.session['user_token']

            except:
                token = None

            user = UserModel.objects.filter(token=token).first()
            if user is not None:

                return render(request, 'activation.html', {
                    'back_ground': BackGroundModel.objects.filter(is_active=True).first(),
                })

            else:

                raise Http404

        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error(f'This is an error message: {e}')

            return redirect('error')

    def post(self, request):
        try:
            try:
                token = request.session['user_token']

            except:
                token = None

            user = UserModel.objects.filter(token=token).first()
            if user is not None:
                active_code = request.POST.get('active_code')
                if user.active_code == active_code:
                    user.phone = global_phone
                    user.username = global_username
                    user.save()

                    return redirect('profile')

                else:

                    return render(request, 'activation.html', {
                        'back_ground': BackGroundModel.objects.filter(is_active=True).first(),
                        'incorrect': True
                    })

            else:

                raise Http404

        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error(f'This is an error message: {e}')

            return redirect('error')


class NewCodeView(View):
    def get(self, request):
        try:
            try:
                token = request.session['user_token']

            except:
                token = None

            user = UserModel.objects.filter(token=token).first()
            if user is not None:
                user.active_code = creat_random_code(6)
                user.token = get_random_string(100)
                request.session['user_token'] = user.token

                api = KavenegarAPI(
                    '376C2F4B51734A3643366A655A714E7570465263614775394644333773537570644C5234666571566548673D')
                params = {
                    'sender': '2000660110',
                    'receptor': f'{user.phone}',
                    'message': f'Your OTP is: {user.active_code}',
                }
                api.sms_send(params)

                return render(request, 'activation.html', {

                })

            else:
                raise Http404

        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error(f'This is an error message: {e}')
            return redirect('error')
