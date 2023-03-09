from django.http import HttpResponse
from django.template import loader

def home(request):
  username = request.GET.get("user", "Stranger")
  template = loader.get_template('home.html')
  context = {
    'username': username,
  }
  return HttpResponse(template.render(context, request))
  