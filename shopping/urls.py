from django.urls import path

from . import views

app_name = 'shopping'
urlpatterns = [
    # ex: /polls/
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    # path('<int:supermart_id>/', views.detail, name='detail'),
    
    path('detail/<int:customer_id>/', views.show, name='show'),
    
    path('delete/<int:customer_id>/', views.delete, name='delete'),
    
    # path('<int:supermart_id>/vote/', views.vote, name='vote'),
    
    # path('<int:supermart_id>/results/', views.results, name='results'),
    
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:supermart_id>/vote/', views.vote, name='vote'),
    path('add/<int:supermart_id>', views.create, name='create'),
    path('<int:supermart_id>/save', views.CustomerCreateView.as_view, name='save'),
    
   
]