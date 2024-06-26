from django.shortcuts import render,redirect
from django.db.models import Count
# Create your views here.
from django.views.generic import ListView

from app.forms import ContactFileForm
from .models import *
from django.views import View
from django.shortcuts import render, get_object_or_404


class ThemeView(ListView):
    model = Theme
    context_object_name = 'Theme'
    template_name = 'index.html'
    def get_queryset(self):
        queryset = super().get_queryset().annotate(num_questions=Count('quests'))
        return queryset

def themes_quest(request, id):
    theme = get_object_or_404(Theme, id=id)
    quests = theme.quests.all()
    num_questions = quests.count()
    return render(request, "about.html", {"theme": theme, "num_questions": num_questions, "quests": quests})


class QuestView(ListView):
    model = Quest
    context_object_name = 'quests'
    template_name = 'about.html'

class ContactListView(ListView):
    model = Contact
    context_object_name = 'contacts'
    template_name = 'contact.html'


class UploadFileView(View):
    def post(self, request, contact_id):
        contact = get_object_or_404(Contact, id=contact_id)
        file = request.FILES['file']
        contact.file = file
        contact.save()
        return redirect('contact_list') 


def upload_file(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    if request.method == 'POST':
        form = ContactFileForm(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_detail', contact_id=contact.id)  # Redirect to contact detail page
    else:
        form = ContactFileForm(instance=contact)
    return render(request, 'upload_file.html', {'form': form, 'contact': contact})



