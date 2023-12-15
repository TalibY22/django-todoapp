from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import todo,item
from .form import create_list


# Create your views here.
def index(response, id):
    ls = todo.objects.get(id=id)

    if response.method == "POST":
        print(response.POST)
        if response.POST.get("save"):
            for item in ls.item_set.all():  # Corrected typo in item_set
                checkbox_name = "c" + str(item.id)
                completion_status = response.POST.get(checkbox_name) == "on"
                item.complete = completion_status
                item.save()

        elif response.POST.get("newitem"):
            txt = response.POST.get("new")

            if len(txt) > 2:
                ls.item_set.create(text=txt, complete=False)

    return render(response, "main/base.html", {"ls": ls})


#Home page 
def home(response):
    return render(response,"main/Home.html",{})

#Page to create new task
def create(response):
    if response.method == "POST":
        form = create_list(response.POST)
        if form.is_valid():
            task_name = form.cleaned_data["name"]
            t = todo(name=task_name)
            t.save()
            response.user.Todo.add(t)
        return HttpResponseRedirect("/view")  # Redirect to the home page or any other desired page after successful form submission
    else:
        form = create_list()

    return render(response, "main/create.html", {"form": form})


#page to view current tasks
def view(response):
    return render(response,"main/view.html")