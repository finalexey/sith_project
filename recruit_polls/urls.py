from django.urls import path

from recruit_polls.views import poll, polls_list

urlpatterns = [
    path('polls_list', polls_list, name='polls_list'),
    path('<int:id>/', poll, name='poll'),
]
