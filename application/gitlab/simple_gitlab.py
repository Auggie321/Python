# -*- coding:utf-8 -*-
## version: python 3.7

import gitlab

# url= 'http://172.16.0.204:10080/'
# token = 'xnztzE8KfT7rVgzkk_BG'
# gl = gitlab.Gitlab(url, token)

# 获取gitlab所有projects及对应id
def allprojects():
    projects = gl.projects.list(all=True)
    for project in projects:
        print(project.name, project.id)

# 获取gitlab所有groups的名称及id
def allgroups():
    groups = gl.groups.list(all=True)
    for group in groups:
        print(group.name, group.id)

# 获取gitlab所有user名称及id
def allusers():
    users = gl.users.list(all=True)
    for user in users:
        print(user.username, user.id, user.name, user.state)

# 获取gitlab指定分组内所有user及project名称，id信息
def assgroups():
    gid = int(input('Input the group ID:'))
    group = gl.groups.get(gid)
    print(group.name)
    projects = group.projects.list(all=True)
    for project in projects:
        #print(group.name,project.name)
        print(project)

# 获取gitlab指定id下的project及clone地址
def projectinfo():
    pid = int(input('Input the project ID:'))
    projects = gl.projects.get(pid)
    print(projects.name, projects.http_url_to_repo)

def projectid():
    pid = int(input(' Input the group ID:'))
    group = gl.groups.get(pid)
    repo = str(input('Input your repo name:'))
    project = gl.projects.get(group.name + '/' +repo)
    print(project.id)

# 获取gitlab指定user  
def assuer():
    uid = int(input('Input the user ID:'))
    user = gl.users.get(uid)
    print(user.name)

if __name__=='__main__':
    url= 'http://172.16.0.204:10080/'
    token = 'xnztzE8KfT7rVgzkk_BG'
    gl = gitlab.Gitlab(url, token)
    info = {
        1:'allprojects()',
        2:'allgroups()',
        3:'allusers()',
        4:'projectinfo()',
        5:'projectid()',
        6:'assusers()',
        7:'assgroups()'
        }
    serp = '-' * 20
    print('''%s
1. 列出所有的projects
2. 列出所有的groups
3. 列出所有的users 
4. 根据project的ID列出project及clone地址
5. 列出指定的project ID
6. 列出指定的user
7. 列出指定的组内的信息  
%s''' % (serp,serp))
    num = int(input('Input yout choice: '))
    exec(info[num])

## 获取gitlab上所有的项目
# all_projects = gl.projects.list(all=True)                          ##包含所有项目
# public_projects = gl.projects.list(all=True,visibility='public')   ##包含所有共有项目
# internal_projects = gl.projects.list(all=True,visibility='internal')   ##包含所有共有项目
# private_projects = gl.projects.list(all=True,visibility='private')     ##包含所有共有项目
# print("all_projects个数", len(all_projects))
# print("所有public proejct个数", len(public_projects))
# print("所有internal proejct个数", len(internal_projects))
# print("所有private proejct个数", len(private_projects))
# #for project in all_projects:    ## (type(project)) <class 'gitlab.v4.objects.Project'>
#     #print(len(project.__dict__['_attrs']))
#     #print(project.__dict__['_attrs'])

## 注意：不加all=True参数，默认只显示部分条数，不全显
#groups = gl.groups.list(all=True, as_list=False) ##gitlab所有组数据
#groups = gl.groups.get(2)                        ##获取指定id的group数据
#projects = gl.projects.list()                    ##gitlab项目，不加all=True参数，默认只显示部分项目，不全显
#users = gl.users.list()                          ##获取gitlab账户

## link https://python-gitlab.readthedocs.io/en/stable/api-usage.html  python-gitlab api tutorials