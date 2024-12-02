from django.shortcuts import render, HttpResponse
from .models import Spotlight, CustomerReview
# from teams.models import team
from .forms import ContactForm
from products.models import Product


def index(request):
    spotlights = Spotlight.objects.all().order_by('order_id')
    products = Product.objects.all().order_by('order_id')[:3]
    
    context = {
       'spotlights' : spotlights, 
       'products' : products,
    }
    return render(request, 'index.html', context)

def about(request):
    customer_reviews = CustomerReview.objects.all()
    
    context = {
        'customer_reviews' : customer_reviews,
    }    
    return render(request, 'about.html', context)

def contact(request):
    form = ContactForm(request.POST)
    
    context = {
        'form' : form,
    }
    return render(request, 'contact.html', context)

def faq(request):
    return render(request, 'faq.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)  # Bind data to form
        if form.is_valid():  # Validate form data
            form.save()        #  to save database            
            # return HttpResponse("Thank you for contacting us!")   # Redirect after successful submission
    else:
        form = ContactForm()  # Empty form for GET request

    return render(request, 'contact.html', {'form': form})