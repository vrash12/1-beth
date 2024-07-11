from django.shortcuts import render, redirect
from .forms import MemberForm, AttendanceForm
from .models import Member
from ministry.models import Ministry
from django.views import View
from ministry.forms import AssignMinisterForm, AssignMinisterForm
from .models import Attendance
from django.utils import timezone
from django.db.models import Count
from django.http import JsonResponse
from datetime import datetime

def home(request):
    return render(request, 'attendance/home.html')

def add_member(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url') 
    else:
        form = MemberForm()
    return render(request, 'attendance/add_member.html', {'form': form})

def mark_attendance(request):
    if request.method == 'POST':
        # Process the submitted form
        form = AttendanceForm(request.POST)
        if form.is_valid():
            attendance = form.save(commit=False)
            # Additional processing or adjustments to the attendance instance
            attendance.save()

            # Assuming you want to handle multiple members here,
            # you'll need to adjust your form or processing logic accordingly.
            present_members_ids = request.POST.getlist('present_members')
            absent_members_ids = request.POST.getlist('absent_members')
            attendance_date = form.cleaned_data['date']
            
            # Update or create attendance records for present members
            for member_id in present_members_ids:
                member = Member.objects.get(id=member_id)
                Attendance.objects.update_or_create(
                    member=member,
                    date=attendance_date,
                    defaults={'status': True, 'service': attendance.service}
                )

            # Update or create attendance records for absent members
            for member_id in absent_members_ids:
                member = Member.objects.get(id=member_id)
                Attendance.objects.update_or_create(
                    member=member,
                    date=attendance_date,
                    defaults={'status': False, 'service': attendance.service}
                )

            return redirect('attendance_success')
    else:
        # Prepare an empty form for GET request
        form = AttendanceForm()
        filter_date = timezone.now().date()  # Default to today if no date is selected
        members = Member.objects.all()

        return render(request, 'attendance/attendance.html', {
            'form': form,
            'members': members,
            'today': timezone.now().date(),
            'filter_date': filter_date  # Pass this to allow the template to know the current filter
        })


def filter_date(request):
    filter_date_str = request.GET.get('filter_date', None)
    if filter_date_str:
        filter_date = datetime.strptime(filter_date_str, '%Y-%m-%d').date()
    else:
        filter_date = timezone.now().date()  # Default to today if no date is selected

    attendance_records = Attendance.objects.filter(date=filter_date)
    members = Member.objects.all()  # Assuming you need this for other parts of the page

    return render(request, 'attendance/attendance.html', {
        'attendance_records': attendance_records,
        'members': members,
        'today': timezone.now().date(),
        'filter_date': filter_date
    })


def add_member_success(request):
    return render(request, 'attendance/add_member_success.html')

def attendance_success(request):
    return render(request, 'attendance/attendance_success.html')

def ministry_list(request):
    ministries = Ministry.objects.all()  # Retrieves all Ministry instances
    return render(request, 'ministries/ministry_list.html', {'ministries': ministries})

class AssignMinisterView(View):
    def get(self, request):
        form = AssignMinisterForm()
        return render(request, 'ministries/assign_minister.html', {'form': form})
    
    def post(self, request):
        form = AssignMinisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ministry_list')
        
        return render(request, 'ministries/assign_minister.html', {'form': form})



def get_member_details(request, member_id):
    try:
        member = Member.objects.values('first_name', 'last_name', 'birthday','age').get(id=member_id)
        return JsonResponse(member)
    except Member.DoesNotExist:
        return JsonResponse({'error': 'Member not found'}, status=404)
