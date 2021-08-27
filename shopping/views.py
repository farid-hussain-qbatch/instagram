from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.template import loader
from django.http import HttpResponse
from .models import SuperMart,Customer
from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .forms import CreatecustomerForm
from django.views import View
from django.views.generic import DetailView

from shopping import models


class IndexView(generic.ListView):
    template_name = 'shopping/index.html'
    context_object_name = 'supermart_list'

    def get_queryset(self):
        return SuperMart.objects.order_by('id')


class DetailView(DetailView):
    model = SuperMart
    template_name = 'shopping/detail.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        print("Context",context)
        context['customer_list'] = Customer.objects.all()
        print("Context Details: ", context)
        return context

    def get_queryset(self):
        a =SuperMart.objects.order_by('id')
        print(a)
        return a
    
class ResultsView(generic.DetailView):
    model = SuperMart
    template_name = 'shopping/results.html'
    
class CustomerCreateView(View):
    form_class = CreatecustomerForm
    
    def post(self, request, *args, **kwargs):
    
        form = self.form_class(request.POST)
        if form.is_valid():
            name_cus = request.POST['customer_name']
            phone_cus = request.POST['customer_phone']
            address_cus = request.POST['customer_address']
            mart = request.POST['supermart_id']
            mart = SuperMart.objects.get(pk=mart)
            print("Helloooooooooo",mart)
            added_customer = Customer.objects.create(name= name_cus, phone_no=phone_cus, address= address_cus, super_marts=mart )
            return redirect('http://127.0.0.1:8000/shopping/1/')
    
   
    
   
            
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')
        
    
def create(request, supermart_id):
    return render(request, 'shopping/create.html', {'supermart_id': supermart_id})
    

    

# Create your views here.
# def detail(request, supermart_id):
#     supermart_list = get_object_or_404(SuperMart, pk=supermart_id)
#     context = {
#         'supermart_list':  supermart_list,
#     }
#     return render(request,'shopping/detail.html', context)


def show(request, customer_id):
    customer_detail = Customer.objects.get(pk=customer_id)
    customer_detail = "\n Name ", customer_detail.name , "\n Phone: ", customer_detail.phone_no ,"\n Address: ", customer_detail.address 
    return HttpResponse(customer_detail)
  

# def index(request):
#     supermart_list = SuperMart.objects.order_by('id')
#     context = {
#         'supermart_list':  supermart_list,
#     }
#     return render(request,'shopping/index.html',context)

def delete(request, customer_id):
    customer_detail = Customer.objects.get(pk=customer_id)
    customer_detail.delete()
    return redirect('http://127.0.0.1:8000/shopping/')


# def results(request, supermart_id):
#     supermart_list = get_object_or_404(SuperMart, pk=supermart_id)
#     return render(request, 'shopping/results.html', {'supermart_list': supermart_list})

def save(request , supermart_id):
    supermart_list = get_object_or_404(SuperMart, pk=supermart_id)
    
    name_cus = request.POST['customer_name']
    phone_cus = request.POST['customer_phone']
    address_cus = request.POST['customer_address']
    mart = SuperMart.objects.get(pk=supermart_id)
    added_customer = Customer.objects.create(name= name_cus, phone_no=phone_cus, address= address_cus, super_marts=mart )
    return redirect('http://127.0.0.1:8000/shopping/1/')
   
    

def vote(request, supermart_id):
    supermart_list = get_object_or_404(SuperMart, pk=supermart_id)
    try:
        selected_customer = supermart_list.customer_set.get(pk=request.POST['customer'])
    except (KeyError, Customer.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'shopping/detail.html', {
            'supermart_list': supermart_list,
            'error_message': "You didn't select a choice.",
        })
    else:
        # selected_customer.votes += 1
        # selected_customer.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('shopping:results', args=(supermart_list.id,)))
    

    
    

    
  


