from django.shortcuts import render
from app.forms import NewUser

# Create your views here.


def index(request):
    return render(request, 'project/index.html')


def task(request):

    form = NewUser()

    if request.method == "POST":
        form = NewUser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            print("Error")

    return render(request, 'project/task.html', {'form': form})
