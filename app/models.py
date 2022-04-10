from django.db import models
from django.conf import settings


class iCategory(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self) -> str:
        return self.name


class Photo(models.Model):
    icategory = models.ForeignKey(
        iCategory, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='images', null=False, blank=False)
    topic = models.CharField(max_length=30, default='Add topic here')

    def __str__(self) -> str:
        return self.topic


class Room(models.Model):
    Room_categories = (
        ('NAC', 'NON-AC'),
        ('YAC', 'AC'),
        ('DEL', 'DELUXE'),
        ('KIN', 'KING'),
        ('QUE', 'QUEEN'),
    )
    number = models.IntegerField()
    category = models.CharField(max_length=3, choices=Room_categories)
    beds = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return f'{self.number}. {self.category} of {self.beds} beds with {self.capacity} people'


class Booking(models.Model):
    # foreignkey ra tesko parenthesis vitra vako sabai ko barema herna xa hai aru sab bujexas taile
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f'{self.user} booked {self.room} in {self.check_in} to {self.check_out}.'

    def get_room_category(self):
        room_categories = dict(self.room.Room_categories)
        room_category = room_categories.get(self.room.category)
        return room_category

    # def get_cancel_booking_url(self):
