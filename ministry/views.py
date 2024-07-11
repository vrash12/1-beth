from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import AssignMinisterForm, MinisterForm
from .models import Schedule, Ministry, Minister
from django.shortcuts import render

def ministry_list(request):
    ministries = Ministry.objects.all()  # Retrieves all Ministry instances
    return render(request, 'ministries/ministry_list.html', {'ministries': ministries})


class AssignMinisterView(CreateView):
    model = Schedule
    form_class = AssignMinisterForm
    template_name = 'ministries/assign_minister.html'
    success_url = reverse_lazy('ministry_list')  # Adjust this to your actual success URL

    def form_valid(self, form):
        # You can add any custom validation or processing here
        return super().form_valid(form)
    
class MinisterCreateView(CreateView):
    model = Minister
    form_class = MinisterForm
    template_name = 'ministries/add_minister.html'
    success_url = reverse_lazy('ministers_list')  # Update 'ministers_list' to the name of your target URL after form submission

