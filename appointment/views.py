from datetime import time
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from account.models import Profile
from appointment.models import Appointment
from appointment.decoraters import allowed_user
from appointment.forms import AppointmentForm

# Create your views here.
@allowed_user(allowed_roles=["Patient"])
def doctors(request):
    context = {"doctor_list":[]}
    users = User.objects.all()
    for user in  users:
        if user.groups.all()[0].name == "Doctor":
            doctor = []
            doctor.append(user.first_name + " " + user.last_name)
            doctor.append(Profile.objects.get(username=user.username).image)
            doctor.append(user.id)
            context["doctor_list"].append(doctor)
    return render(request,'appointment/doctors.html',context)

@allowed_user(allowed_roles=["Patient"])
def book_appointment(request,pk):
    context = {}
    user = User.objects.get(id=pk)
    context["doctor"] = user.first_name + " " + user.last_name
    context["form"] = AppointmentForm()
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        context["form"] = form
        if form.is_valid():
            appointment = Appointment()
            appointment.name = context["doctor"]
            appointment.speciality = form.cleaned_data.get("speciality")
            appointment.date = form.cleaned_data.get("date")
            appointment.start_time = form.cleaned_data.get("start_time")
            temp = form.cleaned_data.get("start_time")
            if temp.minute+45 > 59:
                if temp.hour+1 > 23:
                    appointment.end_time = time(00,temp.minute-15)
                else:
                    appointment.end_time = time(temp.hour+1,temp.minute-15)
            else:
                appointment.end_time = time(temp.hour,temp.minute+45)
            appointment.save()
            detail = {"name":appointment.name,
                      "date":appointment.date,
                      "s_time":appointment.start_time,
                      "e_time":appointment.end_time}
            return render(request,"appointment/appointments.html",detail)
        else:
            return render(request,"appointment/book_appointment.html",context)
    return render(request,"appointment/book_appointment.html",context)