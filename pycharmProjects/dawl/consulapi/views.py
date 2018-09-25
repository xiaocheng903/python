from django.shortcuts import render

from django.views.generic import TemplateView
from peppa import models as peppa_models
from django.http import HttpResponse
from django.shortcuts import render,render_to_response,redirect
from consulapi import consulapi
import datetime
import requests
import json
import base64
rs="1"
class consul_update(TemplateView):

    template_name = 'index_consul.html'

    def get_context_data(self, **kwargs):
        context = super(consul_update, self).get_context_data(**kwargs)
        result = []
        global_env = self.request.session.get('env')
        #获取项目名称
        x = peppa_models.consul_project.objects.filter(consul_env=global_env)
        for i in x:
            result.append({
                'project': i.project
            })
            print(i)
        #获取project渲染到前端
        context['prolist'] = result
        context['glo_env'] = global_env
        return context
#查看配置文件
class get_consul(TemplateView):

    template_name = 'getconsul.html'


    def get_context_data(self, **kwargs):
        global rs
        context = super(get_consul, self).get_context_data(**kwargs)
        nowdate = datetime.datetime.now().strftime("%Y-%m-%d")
        global_env = self.request.session.get('env')

        consul_pro = self.request.GET.get('consul_pro')


        if global_env == "test":
            rs = requests.get('http://192.168.1.216:8500/v1/kv/dianda/serviceConfig/%s' %( consul_pro ))
        if global_env == "pre":
            rs = requests.get('http://consulpre.diandainfo.com/v1/kv/dianda/serviceConfig/%s' %( consul_pro ))
        if global_env == "pro":
            rs = requests.get('http://consulpro.diandainfo.com/v1/kv/dianda/serviceConfig/%s' %( consul_pro ))

        if rs != "1" and rs.status_code == 200:
            #转list
            jsrs = json.loads(rs.text)
            #去出key 和values 值
            key = jsrs[0]['Key']
            values2 = jsrs[0]['Value']

            #base64 values 值转码
            values1 = str(base64.b64decode(values2.encode('utf-8')), 'utf-8')

            context['key_url'] = rs.url
            context['key'] = key
            context['value1'] = values1
        else:
            context['key_url'] = ''
            context['key'] = ''
            context['value1'] = ''


        context['glo_env'] = global_env

        return context


class update_consul(TemplateView):

    template_name = 'updateconsul.html'


    def post(self, request, *args, **kwargs):

        version = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        global_env = self.request.session.get('env')
        update_values = request.POST.get('update_value')
        update_keys = request.POST.get('update_key')
        update_project = request.POST.get('project')
        #判断是否为json格式
        js = consulapi.ifjson(update_values)

        if js is True:


            if global_env == "test":
                requests.put('http://192.168.1.216:8500/v1/kv/dianda/serviceConfig/%s' %( update_project ), update_values.encode('utf-8'))
            if global_env == "pre":
                requests.put('http://consulpre.diandainfo.com/v1/kv/dianda/serviceConfig/%s' %( update_project ), update_values.encode('utf-8'))
            if global_env == "pro":
                requests.put('http://consulpro.diandainfo.com/v1/kv/dianda/serviceConfig/%s' %( update_project ), update_values.encode('utf-8'))

            consulapp = peppa_models.consul_version.objects.create(
                project=update_project,
                consul_version=version,
                consul_key=update_keys,
                consul_values=update_values,
                consul_env=global_env,
            )
            consulapp.save()
            return redirect("/consulapi")

        else:
            return redirect("/consulapi/consul_error?project=%s" %(update_project))



    def get_context_data(self, **kwargs):

        context = super(update_consul, self).get_context_data(**kwargs)
        global_env = self.request.session.get('env')
        global rs

        consul_pro = self.request.GET.get('consul_pro')


        if global_env == "test":
            rs = requests.get('http://192.168.1.216:8500/v1/kv/dianda/serviceConfig/%s' %( consul_pro ))
        if global_env == "pre":
            rs = requests.get('http://consulpre.diandainfo.com/v1/kv/dianda/serviceConfig/%s' %( consul_pro ))
        if global_env == "pro":
            rs = requests.get('http://consulpro.diandainfo.com/v1/kv/dianda/serviceConfig/%s' %( consul_pro ))
        if rs != "1" and rs.status_code == 200:
            print(rs)
            #转list
            jsrs = json.loads(rs.text)
            #去出key 和values 值
            key = jsrs[0]['Key']
            values2 = jsrs[0]['Value']
            #base64 values 值转码
            values1 = str(base64.b64decode(values2.encode('utf-8')), 'utf-8')
            #split分割获取project
            consul_project = rs.url.split('/')[-1]
            context['consul_project'] = consul_project
            context['key'] = key
            context['value1'] = values1
        else:
            context['consul_project'] = consul_pro
            context['key'] = 'dianda/serviceConfig/%s' %(consul_pro)
            context['value1'] = ''
        context['glo_env'] = global_env

        return context


#错误页面
class  consul_error(TemplateView):
    template_name = 'error.html'

    def get_context_data(self, **kwargs):
        global_env = self.request.session.get('env')


        context = super(consul_error, self).get_context_data(**kwargs)
        project = self.request.GET.get('project')
        context['project'] = project
        context['glo_env'] = global_env
        return  context

class rollback_consul(TemplateView):
    template_name = 'consul_rollback.html'

    def get_context_data(self, **kwargs):

        context = super(rollback_consul, self).get_context_data(**kwargs)
        global_env = self.request.session.get('env')
        version_result = []
        consul_pro = self.request.GET.get('consul_pro')
        x = peppa_models.consul_version.objects.filter(project=consul_pro)
        v = x.filter(consul_env=global_env).order_by('-id')

        print(v)
        for i in v:
            print(i.consul_values)
            version_result.append({
                'id': i.id,
                'project': i.project,
                'version': i.consul_version,
                'values': i.consul_values

            })
        context['versioninfo'] = version_result
        context['glo_env'] = global_env

        return context


def roll_update(request):

    id = request.GET.get('id')
    global_env = request.session.get('env')
    rollrow = peppa_models.consul_version.objects.get(id=id)
    rollval = rollrow.consul_values
    rollpro = rollrow.project
    print(id)
    print(rollval)

    if global_env == "test":
        requests.put('http://192.168.1.216:8500/v1/kv/dianda/serviceConfig/%s' %( rollpro ), rollval.encode('utf-8'))
    if global_env == "pre":
        requests.put('http://consulpre.diandainfo.com/v1/kv/dianda/serviceConfig/%s' %( rollpro ), rollval.encode('utf-8'))
    if global_env == "pro":

        requests.put('http://consulpro.diandainfo.com/v1/kv/dianda/serviceConfig/%s' %( rollpro ), rollval.encode('utf-8'))
    return redirect('/consulapi/get_consul?consul_pro=%s' %(rollpro))


def get_consul_ajax(request):
    project = request.GET.get('project')
    a = {}
    url = 'http://peppa.diandainfo.com/consulapi/get_consul?consul_pro=%s' %(project)

    a['url'] = url

    return HttpResponse(json.dumps(a), content_type='application/json')

#update ajax配置文件

def update_consul_ajax(request):
    project = request.GET.get('project')
    a = {}
    url = 'http://peppa.diandainfo.com/consulapi/update_consul?consul_pro=%s' %(project)

    a['url'] = url

    return HttpResponse(json.dumps(a), content_type='application/json')



def rollback_consul_ajax(request):
    project = request.GET.get('project')
    a = {}
    url = 'http://peppa.diandainfo.com/consulapi/rollback_consul?consul_pro=%s' %(project)

    a['url'] = url

    return HttpResponse(json.dumps(a), content_type='application/json')
