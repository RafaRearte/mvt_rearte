from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import time
from mvt_app.models import Family

def familiares(request):
    template = loader.get_template('template_one.html')
    familiares = Family.objects.all()
    
    context = {
        'familiares': familiares,
    }
    
    render = template.render(context)
    return HttpResponse(render)



 