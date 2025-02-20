from django.shortcuts import render
from .models import store_collection
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from .models import Mobile,Cart

# Create your views here.
def index(request):
	return HttpResponse("<h1> App is running </h1>")

def home(request):
	mobiles = Mobile.objects.all()
	return render(request,'home.html',{'mobiles': mobiles})

def add_to_cart(request,mobile_id):
	mobile =get_object_or_404(Mobile,id=mobile_id)
	cart_item,created = Cart.objects.get_or_create(user=request.user.username,mobile=mobile)
	if not created:
		cart_item.quantity += 1
		cart_item.save()
	return redirect('cart')

def cart_veiw(request):
	cart_items = Cart.objects.filter(user=request.user.username)
	return render(request,'cart.html',{'cart_items':cart_items})
 