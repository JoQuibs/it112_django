from django.http import HttpResponse
from django.template import loader
from .models import Name

def django_project(request):
  mynames = Name.objects.all().values()
  template = loader.get_template('all_names.html')
  context = {
    'mynames': mynames,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  myname = Name.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'myname': myname,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())