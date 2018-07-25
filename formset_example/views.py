# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import DetailView
from django.shortcuts import render
from .models import Student
from django.http import HttpResponseRedirect
from .forms import StudentForm

# Create your views here.
class FormsetView(DetailView):
    # model = Student
    form_class = StudentForm
    initial = {
        'name': 'somename',
        'mark': '50'
        }
    model = Student
    success_url = '/formset/'
    success_message = "Mark pushed successfully"

    template_name = "formset_example/formset_temp.html"

    def get(self, request, **kwargs):
        form = self.form_class(initial=self.initial)

        

        return render(request, self.template_name, {'form': form})
        # return self.render_to_response(context)

    def post(self,request,**kwargs):
        pass 
    

