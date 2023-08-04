from django.urls import path
from .views import CategoryView, project_detail, get_projects_by_category, ProjectView

app_name = 'project'
urlpatterns = [
    path('', CategoryView.as_view(), name='project'),
    path('project/<int:id_project>', project_detail, name='project_detail'),
    path('category/<int:id_category>', get_projects_by_category, name='category'),
    path('all-projects/', ProjectView.as_view(), name='all-projects')
]
