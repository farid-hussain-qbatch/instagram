from django.shortcuts import  render, redirect
from django.shortcuts import get_object_or_404, render
from .forms import NewUserForm
from django.contrib.auth import login, authenticate ,logout #add this#add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
from django.shortcuts import render
from .models import *
from django.urls import reverse
from django.db.models import *
from django.http import HttpResponseRedirect

# Create your views here.
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("instagram:homepage")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="instagram/register.html", context={"register_form":form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                current_user = UserStatus.objects.filter(users_id=user.id)
                if not current_user:
                    UserStatus.objects.create(users = user, active=True)
                else:
                    UserStatus.objects.filter(users_id=user.id).update(active=True)    
                    
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("instagram:homepage")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="instagram/login.html", context={"login_form":form})

def logout_request(request):
    user = request.user 
    UserStatus.objects.filter(users_id=user.id).update(active=False)  
    logout(request)            
    messages.info(request, "You have successfully logged out.") 
    return redirect("instagram:login")


def homepage(request):
    context = {
        'supermart_list':  'aa',
    }
    return render(request,'instagram/index.html',context)


def one_to_one_chat(request):
    
    user = request.user 
    user = get_object_or_404(User, pk=user.id)
    single_coversations = Conversation.objects.annotate(b = Count('member')).filter(b__lte=2, member = user.id)
    context = {
        'single_coversations':  single_coversations,
    }
    return render(request,'instagram/singlechat.html', context)
    

def group_chat(request):
    user = request.user 
    user = get_object_or_404(User, pk=user.id)
    single_coversations = Conversation.objects.annotate(b = Count('member')).filter(b__gt=2, member = user.id)
    context = {
        'single_coversations':  single_coversations,
    }
    return render(request,'instagram/singlechat.html', context)


def chat(request, single_coversations_id):
    user = request.user
    conversation_id = Conversation.objects.get(pk=single_coversations_id)
    with_user =  conversation_id.member.all().exclude(id=user.id)
    with_user_id = with_user[0].id 
    messages =  conversation_id.message_set.all()   
    context = {
        'with_user_id':  with_user_id,
        'messages': messages,
        'conversation_id': conversation_id,
    }
    return render(request,'instagram/userchats.html',context)


def send(request, conversation_id):
    user = request.user
    conversations = Conversation.objects.get(pk=conversation_id)
    message = request.POST['message']
    print(message)
    tag = request.POST['tag']
    if tag:
        message = "@" + tag + " " + message
  
    Message.objects.create(sender=user , conversation = conversations,   message_text = message )
    return HttpResponseRedirect(reverse('instagram:chat', args=(conversations.id,)))

def reply(request, message_id):
    message = Message.objects.get(pk=message_id)
    context = {
        'message': message,
    }
    return render(request,'instagram/userreply.html',context)

def replied(request, message_id):
    user = request.user
    message = Message.objects.get(pk=message_id)
    reply = request.POST['reply']
    conversations = message.conversation
    Reply.objects.create(sender=user , message = message, reply_text = reply )
    return HttpResponseRedirect(reverse('instagram:chat', args=(conversations.id,)))
    
    
    
   
    
    



