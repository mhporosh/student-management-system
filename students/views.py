from django.urls import reverse_lazy
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView, DetailView
)
from .models import Student
from .forms import StudentForm
from django.contrib.messages.views import SuccessMessageMixin

class StudentListView(ListView):
    model = Student
    template_name = './student_list.html'
    context_object_name = 'students'

class StudentCreateView(SuccessMessageMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = './student_form.html'
    success_url = reverse_lazy('student_list')
    success_message = "Student added successfully!"

class StudentUpdateView(SuccessMessageMixin, UpdateView):
    model = Student
    form_class = StudentForm
    template_name = './student_form.html'
    success_url = reverse_lazy('student_list')
    success_message = "Student updated successfully!"

class StudentDeleteView(DeleteView):
    model = Student
    template_name = './student_confirm_delete.html'
    success_url = reverse_lazy('student_list')
    
    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        from django.contrib import messages
        messages.success(request, "Student deleted successfully!")
        return response

class StudentDetailView(DetailView):
    model = Student
    template_name = './student_detail.html'