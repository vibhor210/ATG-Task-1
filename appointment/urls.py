from . import views
from django.urls import path

urlpatterns = [
    path('doctors',views.doctors,name='doctors'),
    path('book-appointment/<str:pk>/',views.book_appointment,name='BookAppointment'),
]