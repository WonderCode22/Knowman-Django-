from django.shortcuts import render
from django.db import models
from django.views.generic import TemplateView, View
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
import json
from .models import Tblescalation, Case
from .forms import SuggestionForm, TblescalationForm, SearchForm
# from haystack.query import SearchQuerySet
from .forms import SignUpForm, SuggestionForm
# from search.models import Case


@login_required
def pcomplete(request):
    if request.method == 'POST':
        form = TblescalationForm(request.POST)
        if form.is_valid():
            case_item = form.save(commit=False)
            case_item.user = request.user
            case_item.save()
            return render(request, 'interact/post_complete.html', {'saved_case': case_item})
        else:
            return render(request, 'interact/posting.html', {'form': form})

@login_required
def posting(request):
    form = TblescalationForm()
    return render(request, 'interact/posting.html', {'form': form})


# @login_required
# def searching_db(request):
#     if request.method == 'GET':
#         form = SearchForm(request.GET)
#         if form.is_valid():
#             case_item = form.get
#         return render(request, 'interact/searching.html', {'form': form})


@login_required
def searching(request):
    form = SearchForm()
    return render(request, 'interact/searching.html', {'form': form})


# @login_required
# def search_box(request):
#     form = CaseForm()
#     return render(request, 'search_box.html', {'form': form})


@login_required
def search(request):
    count = Tblescalation.objects.all().count()
    context1 = {
    'count': count,
    }
    return render(request, 'base.html', context1)

@login_required
def case_details(request):
    queryset = Case.objects.filter(case_number=1234)
    # case = Case.objects.all()
    context = {
        "object_list": queryset,
        # 'case': case,
    }
    return render(request, 'details/detail.html', context)


# @login_required
# def search_titles(request):
#     articles = SearchQuerySet().autocomplete(content_auto=request.POST.get('search_text', ''))
#     return render_to_response('search_results.html', {'articles' : articles})
