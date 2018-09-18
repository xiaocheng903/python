
from peppa.models import *
import datetime
import os
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
def get_applyuser(id):
    row = User_Grpup.objects.get(id=id)
    name = row.username
    return name

def get_sqlproject(id):
    sqlrow = sqlapply.objects.get(id=id)
    sqlres=[]
    sqlres.append({
        'title': sqlrow.title,
        'sql': sqlrow.applysql,
        'sql2': sqlrow.applysql2,
        'appdate': sqlrow.applydate,
        'dbname': sqlrow.dbname,
        'beizhu': sqlrow.beizhu,
        'status': sqlrow.get_status_display(),
        'applyuser': get_applyuser(sqlrow.applyuserId),
        'cjdate': sqlrow.nowdate,
        'dbname1': sqlrow.dbname1

    })
    return sqlres

def get_applyproject(id):

    row = Apply.objects.get(id=id)
    res=[]
    res.append({
        'project': row.project,
        'sql': row.applysql,
        'tags': row.tags,
        'applyconfig': row.applyconfig,
        'appdate': row.applydate,
        'cjdate': row.nowdate,
        'status': row.get_status_display(),
        'cpleader': row.cpleader,
        'csleader': row.csleader,
        'jsleader': row.jsleader,
        'applyuserId': get_applyuser(row.applyuserId),
        'beizhu': row.beizhu,
        'repertory': row.repertory,
        'dbname': row.dbname,
        'version': row.version,
        'dbname1': row.dbname1,
        'applysql1': row.applysql1,
        'branchname': row.branchname
    })
    return res

def get_applystatus(id,status):

    row = Apply.objects.get(id=id)

    row.status = status
    row.type = status
    row.save()

def get_sqlstatus(id,status):

    row = sqlapply.objects.get(id=id)
    sqlversion = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

    row.status = status
    row.type = status
    print(row.status)
    if row.type == "2":
        row.version = sqlversion
    row.save()
    print(row.version)
def get_machine(project,env):
    machine = []
    envmachine = projectToMachine.objects.filter(applyEnv=env)
    row = envmachine.filter(project=project)
    for i in row:
        machine.append(i.machine)
    return machine

def save_version(id,version):
    row = Apply.objects.filter(id=id)
    print("helloceshi")
    print(id)
    print(version)
    row.update(version=version)
#    row.version = version
#    row.save()

def get_version(id):
    row = Apply.objects.get(id=id)
    version = row.version
    return version

def get_project(id):
    row = Apply.objects.get(id=id)
    project=row.project
    return project

def get_port(machine,project):
    row = projectToMachine.objects.filter(machine=machine)
    port = row.get(project=project).port
    return port

def get_project_name(project):
    row = project_gitaddress.objects.get(project=project)
    project_name = row.name
    return project_name
#推送git代码
def push_git(project,id):
    row = Apply.objects.get(id = id)
    status = os.system('cd /tmp/peppa/%s && tar -zcvf %s.tar.gz ./*' % (project, project))
    if status == 0:
        row.release_status = 1
        row.save()
    status1 = os.system('scp  /tmp/peppa/%s/%s.tar.gz root@192.168.1.105:/data/node_package' % (project, project))
    if status1 == 0:
        row.release_status = 2
        row.save()
    os.system('rm -f /tmp/peppa/%s/%s.tar.gz' % (project, project))



# Create your views here.
def send_mail(subject,content,to_addr):
    from_email = settings.DEFAULT_FROM_EMAIL
    # subject 主题 content 内容 to_addr 是一个列表，发送给哪些人
    # subject = '王乐大傻逼111'
    # content = '测试内容'
    # to_addr = ['jiaxhs@diandainfo.com']

    msg = EmailMultiAlternatives(subject, content, from_email, [to_addr])

    msg.content_subtype = "html"

    # 添加附件（可选）
    # msg.attach_file('./twz.pdf')

    # 发送
    msg.send()


def get_session_env(request):
    global_env = request.session.get('env')

    if global_env:

        request.session['env'] = global_env
        print(global_env)
    else:
        request.session['env'] = 'test'
    return global_env
