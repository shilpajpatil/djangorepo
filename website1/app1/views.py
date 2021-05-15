from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    senderdata ={
        'name': 'Shilpa',
        'surname': 'patil'
    }
    return render(request,'index.html',senderdata)

def about(request):


    return render(request,'about.html')
def contact(request):
    senderdata ={
        'contact_number':'8149129655'
    }
    return render(request, 'contact.html', senderdata)

def careers(request):
    return render(request,'careers.html')