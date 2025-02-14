import logging

from django.shortcuts import render, redirect
from django.views import View

from .forms import *
from .models import *


class ProjectView(View):
    def get(self, request):
        try:
            projects = ProjectModel.objects.all()
            project_number = 6
            tags = TagModel.objects.all()

            return render(request, 'project.html', {
                'projects': projects[0:project_number],
                'tags': tags,
            })

        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error(f'This is an error message: {e}')

            return redirect('error')


class ProjectFWView(View):
    def get(self, request):
        try:
            projects = ProjectModel.objects.all()
            tags = TagModel.objects.all()

            return render(request, 'project_fw.html', {
                'projects': projects,
                'tags': tags,
            })

        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error(f'This is an error message: {e}')

            return redirect('error')


class ProjectDetailsView(View):
    def get(self, request, id):
        try:
            if not request.user.has_perm('project_module.can_add_projectmodel'):
                project_list = ProjectModel.objects.all()
                my_project = project_list.filter(id=id).first()
                last_project = None
                next_project = None

                for i, project in enumerate(project_list):
                    if project.id == my_project.id:
                        if i > 0:
                            last_project = project_list[i - 1]

                        if i < len(project_list) - 1:
                            next_project = project_list[i + 1]

                return render(request, 'project_details.html', {
                    'project': my_project,
                    'last_project': last_project,
                    'next_project': next_project,

                })

            else:
                project = ProjectModel.objects.filter(id=id).first()
                project_form = ProjectForm(instance=project)
                paragraph_form = ProjectParagraphForm()
                paragraph_form_list = []
                image_form_list = []

                for paragraph in project.paragraph.all():
                    form = ProjectParagraphForm(instance=paragraph)
                    paragraph_form_list.append(form)
                    for image in paragraph.images.all():
                        form = ProjectRelatedImageForm(instance=image)
                        image_form_list.append(form)

                return render(request, 'project_details.html', {
                    'project': project,
                    'project_form': project_form,
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
            project = ProjectModel.objects.filter(id=id).first()
            project_form = ProjectForm(request.POST or None, request.FILES or None, instance=project)

            if project_form.is_valid():
                project_form.save()

                return redirect('project_details', id)

            else:

                return redirect('project_details', id)

        except Exception as e:
            error_logger = logging.getLogger('error_logger')
            error_logger.error(f'This is an error message: {e}')

            return redirect('error')


def delete_project_paragraph(request, id):
    try:
        paragraph = ParagraphModel.objects.get(id=id)
        project_id = paragraph.project.id
        paragraph.delete()

        return redirect('project_details', project_id)

    except Exception as e:
        error_logger = logging.getLogger('error_logger')
        error_logger.error(f'This is an error message: {e}')

        return redirect('error')


def delete_project_image(request, id):
    try:
        image = RelatedImageModel.objects.get(id=id)
        paragraph = image.paragraph
        project_id = paragraph.project.id
        image.delete()

        return redirect('project_details', project_id)

    except Exception as e:
        error_logger = logging.getLogger('error_logger')
        error_logger.error(f'This is an error message: {e}')

        return redirect('error')


def update_project_paragraph(request, id):
    try:
        paragraph = ParagraphModel.objects.filter(id=id).first()
        form = ProjectParagraphForm(request.POST or None, instance=paragraph)
        if form.is_valid():
            form.save()

        return redirect('project_details', paragraph.project.id)

    except Exception as e:
        error_logger = logging.getLogger('error_logger')
        error_logger.error(f'This is an error message: {e}')

        return redirect('error')


def update_project_image(request, id):
    try:
        image = RelatedImageModel.objects.filter(id=id).first()
        form = ProjectRelatedImageForm(request.POST or None, request.FILES or None, instance=image)
        if form.is_valid():
            form.save()

        return redirect('project_details', image.paragraph.project.id)

    except Exception as e:
        error_logger = logging.getLogger('error_logger')
        error_logger.error(f'This is an error message: {e}')

        return redirect('error')


def add_project_paragraph(request, id):
    try:
        project = ProjectModel.objects.filter(id=id).first()
        form = ProjectParagraphForm(request.POST)
        if form.is_valid():
            title = form['title'].value()
            text = form['text'].value()
            ParagraphModel.objects.create(project=project, title=title, text=text)

        return redirect('project_details', id)

    except Exception as e:
        error_logger = logging.getLogger('error_logger')
        error_logger.error(f'This is an error message: {e}')

        return redirect('error')


def add_project_image(request, id):
    try:
        paragraph = ParagraphModel.objects.filter(id=id).first()
        image = request.FILES.get('img' + str(id))
        RelatedImageModel.objects.create(paragraph=paragraph, image=image)

        return redirect('project_details', paragraph.project.id)

    except Exception as e:
        error_logger = logging.getLogger('error_logger')
        error_logger.error(f'This is an error message: {e}')

        return redirect('error')
