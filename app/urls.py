from django.urls import path
from .views import ThemeView, QuestView, themes_quest, ContactListView,UploadFileView
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', ThemeView.as_view(), name='theme'),
    path('theme/<int:id>',themes_quest),
    path('about/', QuestView.as_view(), name='about'),
    path('contact/', ContactListView.as_view(), name='contact'),
    path('contact/<int:contact_id>/upload/', UploadFileView.as_view(), name='upload_file'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)