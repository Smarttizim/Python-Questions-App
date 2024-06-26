from django.urls import path
from .views import ThemeView, QuestView, themes_quest, ContactListView,UploadFileView, upload_file
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', ThemeView.as_view(), name='theme'),
    path('theme/<int:id>',themes_quest),
    path('about/', QuestView.as_view(), name='about'),
    path('contacts/', ContactListView.as_view(), name='contact_list'),
    path('upload/<int:contact_id>/', UploadFileView.as_view(), name='upload_file_view'),
    path('contact/<int:contact_id>/upload/', upload_file, name='upload_file'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)