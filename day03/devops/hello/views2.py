from django.http import HttpRequest
from django.views.generic import View, ListView, TemplateView, CreateView, UpdateView, DeleteView
from .models import User
from django.shortcuts import reverse


class managementView(ListView):
    model = User
    template_name = "cbvmanagement.html"

    def get_keyword(self):
        self.keyword = self.request.GET.get('keyword', "")
        return self.keyword

    def get_queryset(self):
        queryset = super().get_queryset()
        keyword = self.get_keyword()
        if keyword:
            queryset = queryset.filter(name__icontains=keyword)
            print(queryset)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['keyword'] = self.get_keyword()
        return context


class addView(CreateView):
    model = User
    template_name = "add.html"
    fields = ['name', 'password', 'sex']

    def get_success_url(self):
        return reverse('hello:cbvmanagement')


class delView(DeleteView):
    template_name = "dele.html"
    model = User

    def get_success_url(self):
        return reverse('hello:cbvmanagement')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class modView(UpdateView):
    model = User
    template_name = "mod.html"
    fields = ['name', 'password', 'sex']

    def get_success_url(self):
        return reverse('hello:cbvmanagement')
