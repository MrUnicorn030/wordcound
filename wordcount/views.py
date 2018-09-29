#這個是自己創的 
from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
        return render(request,'home.html')
	#return HttpResponse("Hello django world!")
        
def here(request):
	return HttpResponse("<h1>Dad i am here</h1>")

def count(request):
      fulltext1 = request.GET['fulltext']
      wordlist = fulltext1.split()
      return render(request,'count.html',{'fulltext':fulltext1,'count':len(wordlist)})
    

               
