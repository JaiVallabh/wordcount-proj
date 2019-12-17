from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def count(request):
    txt=request.GET['txt']
    list=txt.split()
    dict={}
    for word in list:
        if word in dict:
            dict[word]+=1
        else:
            dict[word]=1
    return render(request,'count.html',{'txt':txt,'count':len(list),'dict':dict.items()})
