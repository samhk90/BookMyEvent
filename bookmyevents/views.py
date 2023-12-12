from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User,Booking,Events
# Create your views here.
def index(request):
    username = request.GET.get('username')
    return render(request,'index.html',{'user':username})

def landing2(request):
    username = request.GET.get('username')
    return render(request,'landing2.html',{'user':username})
def landing2(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        name = request.POST.get('name')
        phoneNumber = request.POST.get('phoneNumber')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User(username=username, name=name, password=password,phoneNumber=phoneNumber,email=email)
        user.save()
        events = Events.objects.all()
        events1 = Events.objects.filter(eventgenre='Movie')
        events2 = Events.objects.filter(eventgenre='Online Event')
        events3 = Events.objects.filter(eventgenre='comedy')
        return render(request, 'main.html',{'events':events,'events1':events1,'events2':events2,'events3':events3,'user':username})
    else:  
     return render(request, 'landing2.html')
def index(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            if User.objects.filter(username=username, password=password).exists():
                events = Events.objects.all()
                events1 = Events.objects.filter(eventgenre='Movie')
                events2 = Events.objects.filter(eventgenre='Online Event')
                events3 = Events.objects.filter(eventgenre='comedy')
                return render(request, 'main.html',{'events':events,'events1':events1,'events2':events2,'events3':events3,'user':username})
            else:
                return render(request, 'landing2.html')
        return render(request,'index.html')
def main(request):  
    username = request.GET.get('username')
    events = Events.objects.all()
    events1 = Events.objects.filter(eventgenre='Movie')
    events2 = Events.objects.filter(eventgenre='Online Event')
    events3 = Events.objects.filter(eventgenre='comedy')
    return render(request, 'main.html',{'events':events,'events1':events1,'events2':events2,'events3':events3,'user':username})
def book(request):
     username = request.GET.get('username')
     event = request.GET.get('eventName')
     events = Events.objects.filter(eventName=event)
     return render(request,'book.html',{'events':events,'user':username})
 
def bookingform(request):
        if request.method == 'POST':
            username = request.GET.get('username')
            eventname = request.POST.get('eventename')
            bookedDate = request.POST.get('bookedDate')
            numberOfTickets = request.POST.get('numberOftickets')
            price = request.GET.get('eventprice')
            booking = Booking(bookedEvent=eventname, bookedDate=bookedDate, bookedtickets=numberOfTickets, bookedprice=price, bookedBy=username)
            booking.save()
            user = User.objects.get(username=username)
            bookedevents = Booking.objects.filter(bookedBy=username)
            return render(request,'profile.html',{'user':user,'bookedevents': bookedevents})
        else:
            username=request.GET.get('username')
            eventname = request.GET.get('eventName')
            event = Events.objects.get(eventName=eventname)
            eventprice = event.eventPrice
            return render(request,'bookingform.html',{'events':eventname,'eventprice':eventprice,'user':username})
def profile(request):
    username = request.GET.get('username')
    
    if User.objects.filter(username=username).exists():
         user = User.objects.get(username=username)
         bookedevents = Booking.objects.filter(bookedBy=username)
         return render(request,'profile.html',{'user':user,'bookedevents':bookedevents})
    else:
     return render(request,'profile.html',{'user':user})