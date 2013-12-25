from django.shortcuts import render

def root_view(request):
    return render(request, 'base_site.jade')