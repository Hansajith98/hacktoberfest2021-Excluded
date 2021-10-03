# Create your views here.
from django.shortcuts import render, redirect
from .forms import HotelForm
from .models import Hotel

# Create your views here.


def hotel_list(request):
    context = {'hotel_list': Hotel.objects.all()}
    return render(request, "hotelcheckin_register/hotel_list.html", context)


def hotel_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = HotelForm()
        else:
            hotel = Hotel.objects.get(pk=id)
            form = HotelForm(instance=hotel)
        return render(request, "hotelcheckin_register/hotel_form.html", {'form': form})
    else:
        if id == 0:
            form = HotelForm(request.POST,request.FILES)
        else:
            hotel = Hotel.objects.get(pk=id)
            form = HotelForm(request.POST,request.FILES,instance= hotel)
        if form.is_valid():
            form.save()
        return redirect('/hotel/list')


def hotel_delete(request,id):
    hotel = Hotel.objects.get(pk=id)
    hotel.delete()
    return redirect('/hotel/list')
