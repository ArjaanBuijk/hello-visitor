"""Defines views"""
from django.shortcuts import get_object_or_404, render
from .models import VisitCounter


def index(request):
    """View for the main page of the app"""
    visit_counter = get_object_or_404(VisitCounter, pk=1)

    # increment the count
    visit_counter.count += 1
    visit_counter.save()

    context = {"visit_counter": visit_counter}
    return render(request, "homepage/index.html", context)
