from django.shortcuts import render, HttpResponse
from . models import iCategory, Photo, Room, Booking
from django.views.generic import ListView, FormView, View, DeleteView
from django.urls import reverse, reverse_lazy
from .forms import Availability_rooms
from app.Booking_functions.availability import check_availability


def index(request):

    icategory = request.GET.get('category')
    if icategory == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(icategory__name=icategory)

    icategories = iCategory.objects.all()

    context = {'icategories': icategories, 'photos': photos}

    return render(request, 'gallery.html', context)


def gallery(request):

    icategory = request.GET.get('category')
    if icategory == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(icategory__name=icategory)

    icategories = iCategory.objects.all()

    context = {'icategories': icategories, 'photos': photos}

    return render(request, 'home.html', context)


def RoomListView(request):
    room = Room.objects.all()[0]
    room_categories = dict(room.Room_categories)
    print('categories=', room_categories)

    room_values = room_categories.values()
    print('categories=', room_categories)
    room_list = []

    for room_category in room_categories:
        room = room_categories.get(room_category)
        room_url = reverse('RoomDetailView', kwargs={
                           'category': room_category})
        # print(room, room_url)
        room_list.append((room, room_url))
    context = {
        "room_list": room_list,
    }

    return render(request, 'room_list_view.html', context,)


class BookingList(ListView):
    model = Booking
    template_name = "booking_list_view.html"

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            booking_list = Booking.objects.all()
            return booking_list
        else:
            booking_list = Booking.objects.filter(user=self.request.user)
            return booking_list


class RoomDetailView(View):
    def get(self, request, *args, **kwargs):
        category = self.kwargs.get('category', None)
        form = Availability_rooms()
        room_list = Room.objects.filter(category=category)
        if len(room_list) > 0:
            room = room_list[0]
            room_category = dict(room.Room_categories).get(room.category)
            context = {
                'room_category': room_category,
                'form': form,
            }
            return render(request, 'room_detail_view.html', context)
        else:
            return HttpResponse('Category does not exist')

    def post(self, request, *args, **kwargs):
        category = self.kwargs.get('category', None)
        room_list = Room.objects.filter(category=category)
        form = Availability_rooms(request.POST)

        if form.is_valid():
            data = form.cleaned_data

        available_rooms = []
        for room in room_list:  # it is for running check availability function in each and every room of this list
            # we used check_in to extract check_in from the dictionary, data is already mentioned above. may be it used data cause check_in data is in date format, its just the theory tho
            # if its true then its gonna append the room may be from the available_room list
            if check_availability(room, data['check_in'], data['check_out']):
                available_rooms.append(room)
        if len(available_rooms) > 0:  # available rooms is greater than 0 means, if the room is available, in this case we gonna run this code else we gonna redirect the http response message as mentioned below
            # its the first room that is available from the list
            room = available_rooms[0]
            booking = Booking.objects.create(
                user=self.request.user,  # passing everything that the booking needs its using self.request may be cause we gonna choose the user or sign up as the new user or something going around there, its just the theory tho
                room=room,  # same as from line 40
                check_in=data['check_in'],  # same as mentionde in the line 36
                check_out=data['check_out']
            )  # this all data is returned only the if function is true or the room is empty or available else if the room is not available we gonna redirect the page to something else as mentionde in line 50
            booking.save()
            return(HttpResponse(booking))
        else:
            return(HttpResponse('All of this category of the rooms are already booked !! Try to book by choosing other room category '))
            # after completing this linking this entire Booking_view in our urls.py of app/ creating template to view everything that is going around in it
            # to do that we have to import Booking view from the views.py


class CancelBookingView(DeleteView):
    model = Booking
    success_url = reverse_lazy('BookingListView')
