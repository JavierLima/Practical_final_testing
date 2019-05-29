from django.conf.urls import url
from django.http import HttpResponse
from .forms import NameForm
from django.shortcuts import render
import sys
from .top_20_tweets_counter import *
import nltk


def home(request):
	# if this is a POST request we need to process the form data
    result = []
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            #nltk.download()
            print(form.cleaned_data)
#            model = twitter_word_counter(form.cleaned_data['your_name'], 'spanish')
#            result = model.top_20_repetitive_word_counter()
            
            
            twitter_counter = twitter_word_counter()
            result = twitter_counter.get_final_data(form.cleaned_data['your_name'])
            
            print(result)

            # html = render_to_string('about.html', {'title': title, 'author': author})
            # return HttpResponse(html)

            # redirect to a new URL:
            #return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form , 'data':result})

    # return HttpResponse('Welcome to the Tinyapp\'s Homepage!')
