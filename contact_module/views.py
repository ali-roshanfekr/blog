import logging

from django.shortcuts import render, redirect
from django.views import View

from site_setting_module.models import BackGroundModel
from .models import *


class ContactView(View):
    def get(self, request):
        try:
            user = request.user
            if user.is_authenticated:
                messages = MessageModel.objects.filter(user=user).order_by('sent_at')

            else:
                messages = None

            return render(request, 'contact.html', {
                'messages': messages,
                'back_ground': BackGroundModel.objects.filter(is_active=True).first(),
            })

        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error(f'This is an error message: {e}')

            return redirect('error')

    def post(self, request):
        try:
            text = request.POST.get('text')
            user = request.user
            if text is not None:
                MessageModel.objects.create(user=user, text=text, reply=False)

                return redirect('contact')

            else:

                return redirect('contact')

        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error(f'This is an error message: {e}')

            return redirect('error')
