'''
메인 urls에 의해 위임된 각 application의 urls 중 하나
'''
from django.urls.conf import path
from gpapp import views

urlpatterns = [
    path('insert/', views.InsertFunc, name="InsertFunc"),

]