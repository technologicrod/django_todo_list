from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm,EditForm

def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_items = List.objects.all()
            context = {'all_items':all_items, "user":"rmatchon"}
            return render(request, 'home.html', context)
    else:
        all_items = List.objects.all()
        context = {'all_items': all_items, "user":"rmatchon"}
        return render(request, 'home.html', context)

def about(request):
    my_name = "Rodwell Matchon"
    return render(request, 'about.html', {"myname": my_name})

def contact(request):
    return render(request, 'contact-us.html', {})

def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    return redirect('home')
def strike(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('home')
def unstrike(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('home')
def edit(request, list_id):
    if request.method == 'POST':
        list_item = List.objects.get(pk=list_id)
        form = EditForm(request.POST or None)
        if form.is_valid():
            updated_item = form.cleaned_data.get("item")
            list_item.item = updated_item
            list_item.save()
            return redirect('home')
    else:
        list_item = List.objects.get(pk=list_id)
        context = {"list_id": list_id, "list_item": list_item}
        return render(request, 'edit.html', context)