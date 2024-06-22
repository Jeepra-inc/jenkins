from django.shortcuts import render, get_object_or_404
from .models import Page

def page_detail(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    return render(request, 'blog/page_detail.html', {'page': page})
