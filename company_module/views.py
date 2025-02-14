import logging

from django.shortcuts import render, redirect
from django.views import View
from .models import *


class CompanyView(View):
    def get(self, request):
        try:
            companies = CompanyModel.objects.all()
            company_number = 6

            return render(request, 'Company.html', {
                'companies': companies[0:company_number],
            })

        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error(f'This is an error message: {e}')

            return redirect('error')


class CompanyFWView(View):
    def get(self, request):
        try:
            companies = CompanyModel.objects.all()

            return render(request, 'company_fw.html', {
                'companies': companies,
            })

        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error(f'This is an error message: {e}')

            return redirect('error')


class CompanyDetailsView(View):
    def get(self, request, id):
        try:
            company_list = CompanyModel.objects.all()
            my_company = company_list.filter(id=id).first()
            last_company = None
            next_company = None

            for i, company in enumerate(company_list):
                if company.id == my_company.id:
                    if i > 0:
                        last_company = company_list[i - 1]

                    if i < len(company_list) - 1:
                        next_company = company_list[i + 1]

            return render(request, 'company_details.html', {
                'company': my_company,
                'last_company': last_company,
                'next_company': next_company,
            })

        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error(f'This is an error message: {e}')

            return redirect('error')
