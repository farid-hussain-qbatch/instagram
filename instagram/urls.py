from django.urls import path
from . import views

app_name = "instagram"   


urlpatterns = [
    # path(" ", views.homepage, name="homepage"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path('', views.homepage, name='homepage'),
    path("logout", views.logout_request, name= "logout"),
    path("one_to_one_chat", views.one_to_one_chat, name= "one_to_one_chat"),
    path("group_chat", views.group_chat, name= "group_chat"),
    path('<int:single_coversations_id>/chat/', views.chat, name='chat'),
    path('<int:conversation_id>/send/', views.send, name='send'),
    path('<int:message_id>/reply/', views.reply, name='reply'),
    path('<int:message_id>/replied/', views.replied, name='replied'),
 

]