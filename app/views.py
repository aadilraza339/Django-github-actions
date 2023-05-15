from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
# Create your views here.
from django.template import loader

def contact_list_view(request):
    contact = Contact.objects.order_by()
    template = loader.get_template("app/contact_list.html")
    context = {
        "contact": contact,
    }
    return HttpResponse(template.render(context, request))