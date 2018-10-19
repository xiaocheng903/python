from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse
import json

class home(TemplateView):

    template_name="home.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(home,self).get_context_data(**kwargs)
        context['pag_title']=u'学习templateview'
        # global_env = testapi(self.request)
        # context['global_env'] = global_env
        return context

class index(TemplateView):

    template_name="index.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(home,self).get_context_data(**kwargs)
        context['pag_title']=u'学习templateview'
        a =12345
        print(a)
        # global_env = testapi(self.request)
        # context['global_env'] = global_env
        return context

# def testapi(request):
#     env_global = request.GET.get('env')
#     print(env_global)
#     env_global = request.GET.get('env')
#     a={}
#     a['envselect'] = env_global
#     print(json.dumps(a))
#     return HttpResponse(json.dumps(a), content_type='application/json')
