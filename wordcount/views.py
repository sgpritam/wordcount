from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'home.html')

def count(request):
    data=request.GET['fulltextarea']
    word_list = data.split()
    list_length = len(word_list)


    worddictionary = {}

    for word in word_list:
        if word in worddictionary:
            #increse value by 1
               worddictionary[word] += 1
        else:
            #add to the dictionary and set value to 1
              worddictionary[word] = 1
    sorted_list = sorted(worddictionary.items(),key = operator.itemgetter(1), reverse=True)
    return render(request,'count.html',{'fulltext':data,'words':list_length,'worddictionary':sorted_list})


