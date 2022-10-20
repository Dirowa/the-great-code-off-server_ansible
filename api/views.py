from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .forms import EntryForm
from .models import Entry
import matplotlib
import matplotlib.pyplot as plt
import os
import matplotlib.font_manager as font_manager
fpath = os.path.join(os.path.dirname(__file__), "ComicNeue-Regular.ttf")
fe = font_manager.FontEntry(
    fname=fpath,
    name='Comic Neue')
font_manager.fontManager.ttflist.insert(0, fe) # or append is fine
matplotlib.rcParams['font.family'] = 'Comic Neue'

@csrf_exempt
# Create your views here.
def submit(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        print(request.POST)
        form = EntryForm(request.POST)
        if form.is_valid():
            res = form.save()
            return render(request, "results.html", {"id": res.id})
    return HttpResponse("hi", content_type="text/plain")


@csrf_exempt
# Create your views here.
def winner(request):
    if request.method == "POST":
        return HttpResponse("You win! You figured it out! Tell your teacher, maybe they'll be impressed!", content_type="text/plain")
    return HttpResponse("hi", content_type="text/plain")


def plot(others, you, title, xlab):
    try:
        plt.close()
    except:
        pass

    _ = plt.hist(others, bins='auto')
    with plt.xkcd():
        plt.title(title, fontname='Comic Neue')
        plt.annotate("You\nare\nhere",
                xy=(you, 0), xycoords='data',
                xytext=(you, 5), textcoords='data',
                arrowprops=dict(arrowstyle="->",
                                connectionstyle="arc3"),
                )

        plt.xlabel(xlab)
        plt.ylabel('# of Solutions')
        response = HttpResponse(content_type="image/png")
        plt.savefig(response, format="png")
        plt.close()
    return response


def histogram_time(request, id):
    record = Entry.objects.get(id=id)
    you = record.time
    others = Entry.objects.filter(name=record.name).values('time')
    others = [x['time'] for x in others]
    return plot(others, you, f"Histogram of '{record.name}' execution time", "time (ms)")


def histogram_complexity(request, id):
    record = Entry.objects.get(id=id)
    you = record.complexity
    others = Entry.objects.filter(name=record.name).values('complexity')
    others = [x['complexity'] for x in others]
    return plot(others, you, f"Histogram of '{record.name}' complexity", "complexity")


def histogram_memory(request, id):
    record = Entry.objects.get(id=id)
    you = record.memory
    others = Entry.objects.filter(name=record.name).values('memory')
    others = [x['memory'] for x in others]
    return plot(others, you, f"Histogram of '{record.name}' memory", "memory (bytes)")
