from django.shortcuts import render
from django.views.generic.base import TemplateView

def MainFunc(request):
    return render(request, 'index.html') # templates안의 index.html을 찾아간다.

class MyCallView(TemplateView):
    template_name = 'callget.html'
    
    
def InsertFunc(request):
    if request.method == 'GET':
        print('get 요청 처리')
        return render(request, 'insert.html')
    elif request.method == 'POST':
        print('post 요청 처리')
        print(request.POST.get('name')) # request.POST['name']으로 써도 됨
        irum = request.POST['name']
        return render(request, 'list.html', {'irum': irum})
    else:
        print('요청 에러')    