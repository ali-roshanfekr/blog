import logging

from django.http import Http404
from django.shortcuts import render, redirect
from django.views import View
from .models import *
from .forms import *


class NewsView(View):
    def get(self, request):
        try:
            news_list = NewsModel.objects.all()

            return render(request, 'news.html', {
                'news_list': news_list,
            })

        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error(f'This is an error message: {e}')

            return redirect('error')


class NewsFWView(View):
    def get(self, request):
        try:
            news_list = NewsModel.objects.all()

            return render(request, 'news_fw.html', {
                'news_list': news_list,
            })

        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error(f'This is an error message: {e}')

            return redirect('error')


class NewsDetailsView(View):
    def get(self, request, id):
        try:
            if not request.user.has_perm('news_module.can_add_newsmodel'):
                news_list = NewsModel.objects.all()
                current_news = news_list.filter(id=id).first()
                last_news = None
                next_news = None

                for i, news in enumerate(news_list):
                    if news.id == current_news.id:
                        if i > 0:
                            last_news = news_list[i - 1]

                        if i < len(news_list) - 1:
                            next_news = news_list[i + 1]

                return render(request, 'news_details.html', {
                    'news': current_news,
                    'last_news': last_news,
                    'next_news': next_news,

                })

            else:
                news = NewsModel.objects.filter(id=id).first()
                news_form = NewsForm(instance=news)
                paragraph_form = NewsParagraphForm()
                paragraph_form_list = []
                image_form_list = []

                for paragraph in news.paragraph.all():
                    form = NewsParagraphForm(instance=paragraph)
                    paragraph_form_list.append(form)
                    for image in paragraph.images.all():
                        form = NewsRelatedImageForm(instance=image)
                        image_form_list.append(form)

                return render(request, 'news_details.html', {
                    'news': news,
                    'news_form': news_form,
                    'paragraph_form': paragraph_form,
                    'paragraph_form_list': paragraph_form_list,
                    'image_form_list': image_form_list,
                })

        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error(f'This is an error message: {e}')

            return redirect('error')

    def post(self, request, id):
        try:
            news = NewsModel.objects.filter(id=id).first()
            news_form = NewsForm(request.POST or None, request.FILES or None, instance=news)

            if news_form.is_valid():
                news_form.save()

                return redirect('news_details', id)

            else:

                return redirect('news_details', id)

        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error(f'This is an error message: {e}')

            return redirect('error')


def delete_news_paragraph(request, id):
    try:
        if request.user.has_perm('news_module.can_add_newsmodel'):
            paragraph = NewsParagraphModel.objects.get(id=id)
            news_id = paragraph.news.id
            paragraph.delete()

            return redirect('news_details', news_id)

        else:
            raise Http404

    except Exception as e:
        error_logger = logging.getLogger('error_logger')
        error_logger.error(f'This is an error message: {e}')

        return redirect('error')


def delete_news_image(request, id):
    try:
        if request.user.has_perm('news_module.can_add_newsmodel'):
            image = NewsRelatedImageModel.objects.get(id=id)
            paragraph = image.paragraph
            news_id = paragraph.news.id
            image.delete()

            return redirect('news_details', news_id)

        else:
            raise Http404

    except Exception as e:
        error_logger = logging.getLogger('error_logger')
        error_logger.error(f'This is an error message: {e}')

        return redirect('error')


def update_news_paragraph(request, id):
    try:
        if request.user.has_perm('news_module.can_add_newsmodel'):
            paragraph = NewsParagraphModel.objects.filter(id=id).first()
            form = NewsParagraphForm(request.POST or None, instance=paragraph)
            if form.is_valid():
                form.save()

            return redirect('news_details', paragraph.news.id)

        else:
            raise Http404

    except Exception as e:
        error_logger = logging.getLogger('error_logger')
        error_logger.error(f'This is an error message: {e}')

        return redirect('error')


def update_news_image(request, id):
    try:
        if request.user.has_perm('news_module.can_add_newsmodel'):
            image = NewsRelatedImageModel.objects.filter(id=id).first()
            form = NewsRelatedImageForm(request.POST or None, request.FILES or None, instance=image)
            if form.is_valid():
                form.save()

            return redirect('news_details', image.paragraph.news.id)

        else:
            raise Http404

    except Exception as e:
        error_logger = logging.getLogger('error_logger')
        error_logger.error(f'This is an error message: {e}')

        return redirect('error')


def add_news_paragraph(request, id):
    try:
        if request.user.has_perm('news_module.can_add_newsmodel'):
            news = NewsModel.objects.filter(id=id).first()
            form = NewsParagraphForm(request.POST)
            if form.is_valid():
                title = form['title'].value()
                text = form['text'].value()
                quote = form['quote'].value()
                NewsParagraphModel.objects.create(news=news, title=title, text=text, quote=quote)

            return redirect('news_details', id)

        else:
            raise Http404

    except Exception as e:
        error_logger = logging.getLogger('error_logger')
        error_logger.error(f'This is an error message: {e}')

        return redirect('error')


def add_news_image(request, id):
    try:
        if request.user.has_perm('news_module.can_add_newsmodel'):
            paragraph = NewsParagraphModel.objects.filter(id=id).first()
            image = request.FILES.get('img' + str(id))
            NewsRelatedImageModel.objects.create(paragraph=paragraph, image=image)

            return redirect('news_details', paragraph.news.id)

        else:
            raise Http404

    except Exception as e:
        error_logger = logging.getLogger('error_logger')
        error_logger.error(f'This is an error message: {e}')

        return redirect('error')
