# forms.py
from django import forms
from .models import Schedule, Minister, Ministry

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['ministry', 'minister', 'start_time', 'end_time', 'notes']
class AssignMinisterForm(forms.ModelForm):
    minister = forms.ModelChoiceField(queryset=Minister.objects.all())
    ministry = forms.ModelChoiceField(queryset=Ministry.objects.all())


    class Meta:
        model = Ministry
        fields = ['minister', 'ministry']

class MinisterForm(forms.ModelForm):
    class Meta:
        model = Minister
        fields = ['first_name', 'last_name', 'age', 'is_youth_minister', 'position', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_youth_minister': forms.CheckboxInput(),  # Removed 'form-control' class
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
