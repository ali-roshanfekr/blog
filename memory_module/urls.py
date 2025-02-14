from django.urls import path
from .views import *

urlpatterns = [
    path('', MemoryView.as_view(), name='memory'),
    path('fw/', MemoryFWView.as_view(), name='memory_fw'),
    path('details/<id>/', MemoryDetailsView.as_view(), name='memory_details'),
    path('m_p_delete/<id>/', delete_memory_paragraph, name='delete_memory_paragraph'),
    path('m_i_delete/<id>/', delete_memory_image, name='delete_memory_image'),
    path('m_p_update/<id>/', update_memory_paragraph, name='update_memory_paragraph'),
    path('m_i_update/<id>/', update_memory_image, name='update_memory_image'),
    path('m_p_add/<id>/', add_memory_paragraph, name='add_memory_paragraph'),
    path('m_i_add/<id>/', add_memory_image, name='add_memory_image'),
]
