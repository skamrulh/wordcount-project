

from django.http import HttpResponse as res
from django.shortcuts import render
import operator

def one(request):
    return render(request, 'homepage.html')

def two(request):
    text = request.GET['texts']
    #wr = text.split()
    word_dic = {}
    for w in text:
        if w in word_dic:
            word_dic[w] += 1
        else:
            word_dic[w] = 1
            
    sortedw = sorted(word_dic.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html',  {'worf':sortedw})

def about(request):
    return render(request, 'about.html')