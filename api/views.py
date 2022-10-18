from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from .forms import EntryForm
from .models import Entry
import matplotlib.pyplot as plt



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


def plot(others, you, title):
    try:
        plt.close()
    except:
        pass

    _ = plt.hist(others, bins='auto')
    plt.title(title)
    plt.annotate("",
            xy=(you, 0), xycoords='data',
            xytext=(you, 5), textcoords='data',
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"),
            )

    response = HttpResponse(content_type="image/png")
    plt.savefig(response, format="png")
    plt.close()
    return response


def histogram_time(request, id):
    record = Entry.objects.get(id=id)
    you = record.time
    others = Entry.objects.filter(name=record.name).values('time')
    others = [x['time'] for x in others]
    return plot(others, you, f"Histogram of {record.name} execution time")


def histogram_complexity(request, id):
    record = Entry.objects.get(id=id)
    you = record.complexity
    others = Entry.objects.filter(name=record.name).values('complexity')
    others = [x['complexity'] for x in others]
    return plot(others, you, f"Histogram of {record.name} complexity")
