from django.shortcuts import render
from django.http import HttpResponse
from .models import Armor, Review
from django.shortcuts import get_object_or_404, redirect
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

def home(request):
    searchTerm = request.GET.get('searchArmor')    
    if searchTerm:        
        armors = Armor.objects.filter(title__icontains=searchTerm)
    else:
        armors = Armor.objects.all()
    return render(request, 'home.html',	{'searchTerm':searchTerm, 'armors': armors})

def about(request):
    return HttpResponse('<h1>Welcome to About Page</h1>')

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email':email})

def detail(request, armor_id):
    armor = get_object_or_404(Armor,pk=armor_id)
    reviews = Review.objects.filter(armor = armor)
    return render(request, 'detail.html', {'armor':armor, 'reviews': reviews})

@login_required
def createreview(request, armor_id):   
    armor = get_object_or_404(Armor,pk=armor_id) 
    if request.method == 'GET':
        return render(request, 'createreview.html', 
                      {'form':ReviewForm(), 'armor': armor})
    else:
        try:
            form = ReviewForm(request.POST)
            newReview = form.save(commit=False)
            newReview.user = request.user
            newReview.armor = armor
            newReview.save()
            return redirect('detail', newReview.armor.id)
        except ValueError:
            return render(request, 'createreview.html', 
              {'form':ReviewForm(),'error':'bad data passed in'})

@login_required
def updatereview(request, review_id):
    review = get_object_or_404(Review,pk=review_id,user=request.user) 
    if request.method =='GET':
        form = ReviewForm(instance=review)
        return render(request, 'updatereview.html', 
                      {'review': review,'form':form})
    else:
        try:
            form = ReviewForm(request.POST, instance=review)
            form.save()
            return redirect('detail', review.armor.id)            
        except ValueError:
            return render(request, 'updatereview.html',
             {'review': review,'form':form,'error':'Bad data in form'})

@login_required
def deletereview(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    review.delete()
    return redirect('detail', review.armor.id)      