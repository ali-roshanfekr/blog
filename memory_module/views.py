import logging

from django.http import Http404
from django.shortcuts import render, redirect
from django.views import View

from .forms import *
from .models import *


class MemoryView(View):
    def get(self, request):
        try:
            memory_list = MemoryModel.objects.all()

            return render(request, 'memory.html', {
                'memory_list': memory_list,
            })

        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error(f'This is an error message: {e}')

            return redirect('error')


class MemoryFWView(View):
    def get(self, request):
        try:
            memory_list = MemoryModel.objects.all()

            return render(request, 'memory_fw.html', {
                'memory_list': memory_list,
            })

        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error(f'This is an error message: {e}')

            return redirect('error')


class MemoryDetailsView(View):
    def get(self, request, id):
        try:
            if not request.user.has_perm('memory_module.can_add_memorymodel'):
                memory_list = MemoryModel.objects.all()
                my_memory = memory_list.filter(id=id).first()
                last_memory = None
                next_memory = None

                for i, memory in enumerate(memory_list):
                    if memory.id == my_memory.id:
                        if i > 0:
                            last_memory = memory_list[i - 1]

                        if i < len(memory_list) - 1:
                            print(f'{len(memory_list)} / {i}')
                            next_memory = memory_list[i + 1]

                return render(request, 'memory_details.html', {
                    'memory': my_memory,
                    'last_memory': last_memory,
                    'next_memory': next_memory,

                })

            else:
                memory = MemoryModel.objects.filter(id=id).first()
                memory_form = MemoryForm(instance=memory)
                paragraph_form = MemoryParagraphForm()
                paragraph_form_list = []
                image_form_list = []

                for paragraph in memory.paragraph.all():
                    form = MemoryParagraphForm(instance=paragraph)
                    paragraph_form_list.append(form)
                    for image in paragraph.images.all():
                        form = MemoryRelatedImageForm(instance=image)
                        image_form_list.append(form)

                return render(request, 'memory_details.html', {
                    'memory': memory,
                    'memory_form': memory_form,
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
            memory = MemoryModel.objects.filter(id=id).first()
            memory_form = MemoryForm(request.POST or None, request.FILES or None, instance=memory)

            if memory_form.is_valid():
                memory_form.save()

                return redirect('memory_details', id)

            else:

                return redirect('memory_details', id)

        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error(f'This is an error message: {e}')

            return redirect('error')


def delete_memory_paragraph(request, id):
    try:
        if request.user.has_perm('memory_module.can_add_memorymodel'):
            paragraph = MemoryParagraphModel.objects.get(id=id)
            memory_id = paragraph.memory.id
            paragraph.delete()

            return redirect('memory_details', memory_id)

        else:
            raise Http404

    except Exception as e:
        error_logger = logging.getLogger('error_logger')
        error_logger.error(f'This is an error message: {e}')

        return redirect('error')


def delete_memory_image(request, id):
    try:
        if request.user.has_perm('memory_module.can_add_memorymodel'):
            image = MemoryRelatedImageModel.objects.get(id=id)
            paragraph = image.paragraph
            memory_id = paragraph.memory.id
            image.delete()

            return redirect('memory_details', memory_id)

        else:
            raise Http404

    except Exception as e:
        error_logger = logging.getLogger('error_logger')
        error_logger.error(f'This is an error message: {e}')

        return redirect('error')


def update_memory_paragraph(request, id):
    try:
        if request.user.has_perm('memory_module.can_add_memorymodel'):
            paragraph = MemoryParagraphModel.objects.filter(id=id).first()
            form = MemoryParagraphForm(request.POST or None, instance=paragraph)
            if form.is_valid():
                form.save()

            return redirect('memory_details', paragraph.memory.id)

        else:
            raise Http404

    except Exception as e:
        error_logger = logging.getLogger('error_logger')
        error_logger.error(f'This is an error message: {e}')

        return redirect('error')


def update_memory_image(request, id):
    try:
        if request.user.has_perm('memory_module.can_add_memorymodel'):
            image = MemoryRelatedImageModel.objects.filter(id=id).first()
            form = MemoryRelatedImageForm(request.POST or None, request.FILES or None, instance=image)
            if form.is_valid():
                form.save()

            return redirect('memory_details', image.paragraph.memory.id)

        else:
            raise Http404

    except Exception as e:
        error_logger = logging.getLogger('error_logger')
        error_logger.error(f'This is an error message: {e}')

        return redirect('error')


def add_memory_paragraph(request, id):
    try:
        if request.user.has_perm('memory_module.can_add_memorymodel'):
            memory = MemoryModel.objects.filter(id=id).first()
            form = MemoryParagraphForm(request.POST)
            if form.is_valid():
                title = form['title'].value()
                text = form['text'].value()
                quote = form['quote'].value()
                MemoryParagraphModel.objects.create(memory=memory, title=title, text=text, quote=quote)

            return redirect('memory_details', id)

        else:
            raise Http404

    except Exception as e:
        error_logger = logging.getLogger('error_logger')
        error_logger.error(f'This is an error message: {e}')

        return redirect('error')


def add_memory_image(request, id):
    try:
        if request.user.has_perm('memory_module.can_add_memorymodel'):
            paragraph = MemoryParagraphModel.objects.filter(id=id).first()
            image = request.FILES.get('img' + str(id))
            MemoryRelatedImageModel.objects.create(paragraph=paragraph, image=image)

            return redirect('memory_details', paragraph.memory.id)

        else:
            raise Http404

    except Exception as e:
        error_logger = logging.getLogger('error_logger')
        error_logger.error(f'This is an error message: {e}')

        return redirect('error')
