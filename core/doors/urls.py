from django.urls import path
from .views import *

app_name = 'doors'
urlpatterns = [
    path('', main, name='main'),
    path('doors/ct<int:pk>', category, name='category'),
    path('doors/sct<int:pk>', subcategory, name='subcategory'),
    path('doors/door<int:pk>', doortype, name='doortype'),
    path('catalog/', catalog, name='catalog'),
    path('news<int:pk>/', news_dtl, name='news_dtl'),
    path('pol-conf/', conf, name='conf'),
    path('doors/search_doors/', search_doors, name="search_doors"),
]