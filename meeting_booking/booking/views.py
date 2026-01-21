from django.shortcuts import render, redirect
from .models import MeetingRoom, Booking
from django.contrib import messages
from datetime import datetime

def home(request):
    return render(request, "home.html")

def booking_view(request):
    rooms = MeetingRoom.objects.all()
    available = None  # None: not checked yet, True: available, False: not available

    if request.method == "POST":
        room_id = request.POST.get("room")
        date = request.POST.get("date")
        start_time = request.POST.get("start_time")
        end_time = request.POST.get("end_time")

        room = MeetingRoom.objects.get(id=room_id)

        start_t = datetime.strptime(start_time, "%H:%M").time()
        end_t = datetime.strptime(end_time, "%H:%M").time()

        # Check availability
        bookings = Booking.objects.filter(room=room, date=date)
        overlap = False
        for b in bookings:
            if not (end_t <= b.start_time or start_t >= b.end_time):
                overlap = True
                break

        if "check" in request.POST:  # Check availability button clicked
            available = not overlap

        elif "book" in request.POST:  # Book button clicked
            if not overlap:
                Booking.objects.create(
                    room=room,
                    user=request.user,
                    date=date,
                    start_time=start_t,
                    end_time=end_t
                )
                messages.success(request, "Room booked successfully!")
                available = True  # booking successful
            else:
                messages.error(request, "Selected slot is not available!")
                available = False

    return render(request, "booking.html", {
        "rooms": rooms,
        "available": available
    })

def register(request):
    return render(request, "register.html")

def login(request):
    return render(request, "login.html")

def about(request):
    return render(request, "about.html")

