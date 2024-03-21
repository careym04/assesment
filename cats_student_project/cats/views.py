from django.shortcuts import render
from django.http import HttpResponse
from cats.models import Student, cat

# Create your views here.
def index(request):
    student_list = Student.objects.order_by('lastName')
    cat_list = cat.objects.order_by('catName')
    
    context_dict = {}
    context_dict['students'] = student_list
    context_dict['cats'] = cat_list
    
    
    return render(request, 'cats/index.html', context=context_dict)



def pets(request):
  cat_list = cat.objects.order_by('catName')
  context_dict = {}
  context_dict['cats'] = cat_list
  return render(request, 'cats/pets.html', context=context_dict)