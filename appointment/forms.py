from django import forms
from appointment.models import Appointment
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('speciality','date','start_time')