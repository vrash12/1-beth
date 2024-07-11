from django import forms
from .models import Member, Attendance, Service

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'middle_name', 'birthday', 'age', 'fb_name']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control', 'optional': True}),
            'birthday': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'fb_name': forms.TextInput(attrs={'class': 'form-control', 'optional': True}),
        }

        
class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['service', 'member', 'status', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'service': forms.Select(),
            'member': forms.CheckboxSelectMultiple(),
            'status': forms.HiddenInput()
        }

    def __init__(self, *args, **kwargs):
        super(AttendanceForm, self).__init__(*args, **kwargs)
        self.fields['member'].queryset = Member.objects.all()
        self.fields['service'].queryset = Service.objects.all()
        self.fields['status'].initial = True  # Assuming marking presence
