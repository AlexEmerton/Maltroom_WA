from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^notes/$', views.NoteList.as_view()),
    url(r'^notes_list', views.NotesList.as_view()),
    url(r'^name_list', views.NameList.as_view()),
    url(r'^nose_list', views.NoseList.as_view()),
    url(r'^palate_list', views.PalateList.as_view()),
    url(r'^finish_list', views.FinishList.as_view()),
]
