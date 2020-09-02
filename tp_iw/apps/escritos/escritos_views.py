from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse



def escritodetail(request):

    #aca tiene que traerse los dattos del escrito donde clickeo para mostrarlos en el "escritos_details"

    return render(request, 'escritos_details.html')