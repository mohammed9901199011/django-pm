from audioop import reverse

from django.urls import reverse_lazy , reverse

from . import models
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from . import forms

# Create your views here.
class ProjectListView(ListView):
    model = models.Project
    template_name = 'project/list.html'
    paginate_by = 3

    # البحث
    def get_queryset(self):
        query_set = super().get_queryset()
        where= {}
        q = self.request.GET.get('q' , None)
        if q:
            where['title__icontains'] = q
        return query_set.filter(**where)


class ProjectCreateView(CreateView):
    model = models.Project
    form_class = forms.ProjectCreateForm
    template_name = 'project/create.html'
    success_url = reverse_lazy('project_list')


class ProjectUpdateView(UpdateView):
    model = models.Project
    form_class = forms.ProjectUpdateForm
    template_name = 'project/update.html'
    # success_url = reverse_lazy('project_list')

    def get_success_url(self):
        return reverse('project_update' , args=[self.object.id])

class ProjectDeleteView(DeleteView):
    model = models.Project
    template_name = 'project/delete.html'
    success_url = reverse_lazy('project_list')


class TaskCreateView(CreateView):
    model = models.Task
    fields = ['project','description' ]
    http_method_names = ['post']

    def get_success_url(self):
        return reverse('project_update' , args=[self.object.project.id])


class TaskUpdateView(UpdateView):
    model = models.Task
    fields = ['is_completed' ]
    http_method_names = ['post']

    def get_success_url(self):
        return reverse('project_update' , args=[self.object.project.id])


class TaskDeleteView(DeleteView):
    model = models.Task

    def get_success_url(self):
        return reverse('project_update' , args=[self.object.project.id])