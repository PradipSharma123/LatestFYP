from django.urls import path
from .views import RoomListView, BookingList, RoomDetailView, CancelBookingView, KhaltiRequestView

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('gallery/', views.gallery, name='gallery'),
    path('aboute/', views.aboute, name='aboute'),
    path('khalti-request/', KhaltiRequestView.as_view(), name="khaltirequest"),
    path('room_list/', RoomListView, name='RoomListView'),  # 3   5:30
    path('booking_list/', BookingList.as_view(), name='BookingList'),
    path('room/<category>', RoomDetailView.as_view(), name='RoomDetailView'),
    path('booking/cancel/<pk>', CancelBookingView.as_view(),
         name='CancelBookingView')
]
