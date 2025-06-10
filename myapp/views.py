from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth import login
from .models import FoodItem
from .forms import FoodItemForm, SignUpForm

@login_required
def food_list(request):
    today = timezone.now().date()
    food_items = FoodItem.objects.filter(
        user=request.user,
        date_added__date=today
    ).order_by('-date_added')
    
    total_calories = sum(item.calories for item in food_items)
    
    return render(request, 'food_list.html', {
        'food_items': food_items,
        'total_calories': total_calories,
        'today': today.strftime('%A, %B %d, %Y')
    })

@login_required
def add_food(request):
    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            food_item = form.save(commit=False)
            food_item.user = request.user
            food_item.save()
            messages.success(request, f'"{food_item.name}" added successfully!')
            return redirect('myapp:food_list')
    else:
        form = FoodItemForm()
    return render(request, 'add_food.html', {'form': form})

@login_required
def delete_food(request, pk):
    food_item = get_object_or_404(FoodItem, pk=pk, user=request.user)
    if request.method == 'POST':
        food_item.delete()
        messages.success(request, 'Food item deleted successfully!')
        return redirect('myapp:food_list')
    return render(request, 'delete_food.html', {'food_item': food_item})

@login_required
def reset_calories(request):
    if request.method == 'POST':
        today = timezone.now().date()
        FoodItem.objects.filter(user=request.user, date_added__date=today).delete()
        messages.success(request, 'All food items for today have been reset!')
        return redirect('myapp:food_list')
    return render(request, 'reset_confirmation.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('myapp:food_list')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})




#views

