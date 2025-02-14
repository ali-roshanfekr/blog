from django.urls import path
from .views import *

urlpatterns = [
    path('', ProjectView.as_view(), name='project'),
    path('fw/', ProjectFWView.as_view(), name='project_fw'),
    path('details/<id>/', ProjectDetailsView.as_view(), name='project_details'),
    path('p_p_delete/<id>/', delete_project_paragraph, name='delete_project_paragraph'),
    path('p_i_delete/<id>/', delete_project_image, name='delete_project_image'),
    path('p_p_update/<id>/', update_project_paragraph, name='update_project_paragraph'),
    path('p_i_update/<id>/', update_project_image, name='update_project_image'),
    path('p_p_add/<id>/', add_project_paragraph, name='add_project_paragraph'),
    path('p_i_add/<id>/', add_project_image, name='add_project_image'),
]
