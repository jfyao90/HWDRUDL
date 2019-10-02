from django.shortcuts import render
from django.http import HttpResponse
from .imageutility import processNpredict

def home(request):
    if request.method == 'POST':
        img = request.POST.get('canvasData')
        #print(img)
        prediction = processNpredict(img)
        return render(request, 'digitrecognise/home.html',{'prediction':prediction})
    else:
        return render(request, 'digitrecognise/home.html')

    
