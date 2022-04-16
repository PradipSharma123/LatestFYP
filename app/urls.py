from django.urls import path
from .views import RoomListView, BookingListView, RoomDetailView, CancelBookingView, KhaltiRequestView, KhaltiVerifyView
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('gallery/', views.gallery, name='gallery'),
    path('aboute/', views.aboute, name='aboute'),
    path('khalti-request/', KhaltiRequestView.as_view(), name="khaltirequest"),
    path('khalti-verify/', KhaltiVerifyView.as_view(), name="khaltiverify"),
    path('room_list/', RoomListView, name='RoomListView'),  # 3   5:30
    path('booking_list/', BookingListView.as_view(), name='BookingListView'),
    path('room/<category>', RoomDetailView.as_view(), name='RoomDetailView'),
    path('booking/cancel/<pk>', CancelBookingView.as_view(),
         name='CancelBookingView')
]
