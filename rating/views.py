from django.shortcuts import render
from django.views import View
from .forms import SimpleForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from .models import Rating

class RatingsDetailView(DetailView):
    model = Rating

class RatingsListView(ListView):
    queryset = Rating.objects.all()
    context_object_name = 'rating_objects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['extra_context'] = 'Foo'
        return context

class RatingsEntryListView(ListView):
    template_name = 'rating/rating_by_name.html'
    context_object_name = 'rating_name_objects'

    def get_queryset(self):
        return Rating.objects.filter(name=self.kwargs['name'])

class SimpleFormView(View):
    form_class = SimpleForm
    initial = {'foo': 'pel`meni'}
    template_name = 'form_template.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("")
        
        return render(request, self.template_name, {'form': form})