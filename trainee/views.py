from django.shortcuts import render, redirect, get_object_or_404
from .models import Trainee

def list_trainees(request):
    trainees = Trainee.objects.all()
    return render(request,'list.html', {'trainees':trainees})

def add_trainee(request):
    if request.method == "POST":
        name_from_form = request.POST.get('trainee_name')
        Trainee.objects.create(name=name_from_form)
        return redirect('trainee_list')
    return render(request, 'add.html')

def update_trainee(request, id):
    trainee = get_object_or_404(Trainee, id=id)
    if request.method == "POST":
        trainee.name = request.POST.get('trainee_name')
        trainee.save()
        return redirect('trainee_list')
    return render(request, 'update.html', {'trainee': trainee})

def delete_trainee(request, id):
    trainee = get_object_or_404(Trainee, id=id)
    trainee.delete()
    return redirect('trainee_list')

def trainee_details(request, id):
    trainee = get_object_or_404(Trainee, id=id)
    return render(request, 'details.html', {'trainee': trainee})
