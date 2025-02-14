from django.urls import path
from .views import *

urlpatterns = [
    path('', NewsView.as_view(), name='news'),
    path('fw/', NewsFWView.as_view(), name='news_fw'),
    path('details/<id>/', NewsDetailsView.as_view(), name='news_details'),
    path('n_p_delete/<id>/', delete_news_paragraph, name='delete_news_paragraph'),
    path('n_i_delete/<id>/', delete_news_image, name='delete_news_image'),
    path('n_p_update/<id>/', update_news_paragraph, name='update_news_paragraph'),
    path('n_i_update/<id>/', update_news_image, name='update_news_image'),
    path('n_p_add/<id>/', add_news_paragraph, name='add_news_paragraph'),
    path('n_i_add/<id>/', add_news_image, name='add_news_image'),
]
