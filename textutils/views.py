#I have created views -anzar
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def analyze(request):
    # sourcery skip: remove-unnecessary-else, swap-if-else-branches

    #get text 
    djtext=request.POST.get('text','default')

    #check checkbox values
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremove=request.POST.get('newlineremove','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')

    print(removepunc)
    print(djtext)
    #check  which checkbox is on
    if removepunc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext=analyzed

    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'Change to Uppercase','analyzed_text':analyzed}
        djtext=analyzed
        
    if(extraspaceremover=="on"):
        analyzed=""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" "and djtext[index+1]==" "):
                analyzed=analyzed+char
        params={'purpose':'Remove space','analyzed_text':analyzed}
        djtext=analyzed
        
    if(newlineremove=="on"):
        analyzed=""
        for char in djtext:
            if char!='\n' and char!='\r':
                analyzed=analyzed+char
        params={'purpose':'Remove newline','analyzed_text':analyzed}

    if(removepunc!="on" and fullcaps!="on"and extraspaceremover!="on"and newlineremove!="on"):
        return HttpResponse("Please select any switch and Try again")
    
    return render(request,"analyze.html",params)

