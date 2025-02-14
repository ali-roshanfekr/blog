import logging

from django.http import Http404
from django.shortcuts import render, redirect
from django.views import View
from site_setting_module.models import *


class IndexView(View):
    def get(self, request):
        try:
            return render(request, 'index.html', {})

        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error(f'This is an error message: {e}')

            return redirect('error')


def menu_component(request):
    try:
        logo = LogoModel.objects.first()

        return render(request, 'menu.html', {
            'logo': logo,
        })

    except Exception as e:
        error_logger = logging.getLogger('error_logger')
        error_logger.error(f'This is an error message: {e}')

        return redirect('error')


def main_component(request):
    try:
        return render(request, 'main.html', {
            'main': MainModel.objects.first(),
            'dailies': DailyModel.objects.filter(is_active=True),
            'services': ServiceModel.objects.all(),
            'works': WorkModel.objects.all(),
            'educations': EducationModel.objects.all(),
            'links': LinkModel.objects.filter(is_active=True),
            'logo': LogoModel.objects.first(),
            'back_ground': BackGroundModel.objects.filter(is_active=True).first(),
        })

    except Exception as e:
        error_logger = logging.getLogger('error_logger')
        error_logger.error(f'This is an error message: {e}')

        return redirect('error')


def bottom_panel(request):
    try:
        return render(request, 'bottom_panel.html', {
            'links': LinkModel.objects.filter(is_active=True),
        })

    except Exception as e:
        error_logger = logging.getLogger('error_logger')
        error_logger.error(f'This is an error message: {e}')

        return redirect('error')


def links(request):
    try:
        return render(request, 'link.html', {
            'logo': LogoModel.objects.first(),
        })

    except Exception as e:
        error_logger = logging.getLogger('error_logger')
        error_logger.error(f'This is an error message: {e}')

        return redirect('error')


class ErrorView(View):
    def get(self, request):
        raise Http404
