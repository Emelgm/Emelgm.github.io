from django.shortcuts import render, get_object_or_404
from .models import Project, Category
from django.views.generic import ListView
from django.urls import reverse
from django.http import HttpResponseRedirect

class CategoryView(ListView):
    template_name = 'home.html'
    context_object_name = 'category_list'

    def get_queryset(self):
        return Category.objects.order_by("name")


class ProjectView(ListView):
    template_name = 'projects.html'
    context_object_name = 'project_list'

    def get_queryset(self):
        return Project.objects.order_by("name")


def project_detail(request, id_project):
    project = get_object_or_404(Project, pk=id_project)
    content = {
        'project': project
    }
    return render(request, 'project_detail.html', content)


def get_projects_by_category(request, id_category):
    categories = Category.objects.all()[id_category-1]
    projects = Project.objects.filter(id_category_id=id_category)
    content = {
        'projects': projects,
        'categories': categories
    }
    return render(request, 'projects.html', content)