from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    # request.GET will get the value for fulltext from fulltext form
    # theseare basically the parameters for the URL
    worldList = fulltext.split()
    wordDict = {}
    count = 1
    for i in worldList:
        if i not in wordDict.keys():
            wordDict[i] = 1
        else:
            wordDict[i] += 1

    sortedWords = sorted(wordDict.items(), key = operator.itemgetter(1), reverse=True)
    return render(request, 'count.html',
    context={"fulltext":fulltext, "count":len(worldList), "sortedWords":sortedWords})
