from django.urls import path
from . import views
from django.views.generic import TemplateView



urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('json/', views.json_view, name='json'),
    path('tabling_js/', (TemplateView.as_view(template_name="tabling.js", content_type='text/javascript', )), name='tabling_js'),
    path('coinmarket_js/', (TemplateView.as_view(template_name="coinmarket.js", content_type='text/javascript', )), name='coinmarket_js'),
    path('json2/', (TemplateView.as_view(template_name="data.json", content_type='application/json', )), name='json2'),
    path('test/', views.TestView.as_view(), name='test'),
    path('restart/', views.RestartList.as_view(), name='restart'),
]








