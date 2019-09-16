from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import LostItem
from .forms import LostItemForm

@login_required()
def home(request):
    items_found = LostItem.objects.filter(isLost=False, isAccepted=True)
    items_lost = LostItem.objects.filter(isLost=True, isAccepted=True)

    context = {
        'items_found': items_found,
        'items_lost': items_lost,
    }
    return render(request, 'biuro/home.html', context)

@login_required()
def add_lost_item(request):
    if request.method == 'POST':
        form = LostItemForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            contact = form.cleaned_data['contact']
            img = request.FILES.get('image', 'default.jpg') 
            lost_item = LostItem(title=title,description=description,contact=contact, image=img, isLost=True, user=request.user)
            lost_item.save()
            return redirect('biuro-home')
    else:
        form=LostItemForm()
    return render(request, 'biuro/add_lost_item.html', {'form':form})

@login_required()
def add_found_item(request):
    if request.method == 'POST':
        form = LostItemForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            contact = form.cleaned_data['contact']
            img = request.FILES.get('image', 'default.jpg')
            lost_item = LostItem(title=title,description=description,contact=contact, image=img, isLost=False, user=request.user)
            lost_item.save()        
            return redirect('biuro-home')      
    else:
        form=LostItemForm()
    return render(request, 'biuro/add_found_item.html', {'form':form})


@login_required()
def waiting_for_acceptation(request):
    if request.user.is_superuser:       
        items_waiting = LostItem.objects.filter(isAccepted=False)
        context= { 
            'items': items_waiting,
        }
        return render(request, 'biuro/acceptation_list.html', context)
    else:
        return redirect('biuro-home')

@login_required()
def acceptation_item_detail(request, id):
    try:
        if request.user.is_superuser:
            item = get_object_or_404(LostItem, pk=id)
            if request.method == 'POST':
                item.title = request.POST['title']
                item.description = request.POST['description']
                item.contact = request.POST['contact']
                item.isAccepted = True
                item.acceptedBy = request.user
                item.save()
                return redirect('biuro-waiting')
            else:
                context={
                    'item': item,
                }
                return render(request, 'biuro/acceptation_item.html', context)
    except:
        return redirect('biuro-home')
    

@login_required()
def item_detail(request, id):
    try:
        item = LostItem.objects.get(id=id, isAccepted=True)
        context={
            'item': item,
        }
        return render(request, 'biuro/item.html', context)
    except:
        return redirect('biuro-home')

@login_required()
def item_delete(request, id):
    try:
        item = LostItem.objects.get(id=id)
        if request.user == item.user or request.user.is_superuser:
            item.delete()
        return redirect('biuro-home')
    except:
        return redirect('biuro-home')

@login_required()
def items_accepted(request):
    if request.user.is_superuser:
        items = LostItem.objects.filter(isAccepted=True, acceptedBy=request.user)
        context = {
            'items': items,
        }
        return render(request, 'biuro/accepted.html', context)
        
    else:
        return redirect('biuro-home')