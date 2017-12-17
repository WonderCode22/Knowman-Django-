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
from .search import *
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
def search_tblinstallbase(request):
    utid = ""
    context = {}
    render_template = ""
    if request.method == "POST":
        form_value = SearchForm(request.POST)

    if form_value.is_valid():
        utid = form_value.cleaned_data['utid']
        symptoms = form_value.cleaned_data['symptoms']

        if  symptoms and not utid:
            render_template = 'details/tblescalation.html'
            tblescalation_result = search_tblescalation_symptoms(symptoms)
            context = {
                    'symptoms': symptoms, 
                    'tblescalations':tblescalation_result
            }
        elif not symptoms and utid:
            render_template = 'details/tblinstallbase.html'
            tblinstallbase_result = search_tblinstallbase_utid(utid)
            if not tblinstallbase_result:
                tblinstallbase = None
            else:
                tblinstallbase = tblinstallbase_result[0]
            
            tblescalation_result = search_tblescalation_utid(utid)

            context = {
                    'utid': utid, 
                    'tblinstallbase': tblinstallbase, 
                    'tblescalations':tblescalation_result
            }

        elif symptoms and utid:
            render_template = 'details/tblinstallbase.html'
            tblinstallbase_result = search_tblinstallbase_utid(utid)
            if not tblinstallbase_result:
                tblinstallbase = None
            else:
                tblinstallbase = tblinstallbase_result[0]
            
            tblescalation_result = search_tblescalation(utid, symptoms)

            context = {
                    'utid': utid, 
                    'tblinstallbase': tblinstallbase, 
                    'tblescalations':tblescalation_result
            }
        
        else:
            form = SearchForm()
            return render(request, 'interact/searching.html', {'form': form})
    return  render(request, render_template, context)

@login_required
def tblescalation_by_case(request, case_id):
    if request.method == 'POST':
        caseId = request.POST['case_id']

        value = Tblescalation.objects.filter(case_id = caseId)
        value1 = {
            "system": value[0].system,
            "subsystem": value[0].subsystem,
            "fault": value[0].fault,
            "symptoms": value[0].symptoms,
            "fix_rca": value[0].fix_rca,
            "poa": value[0].poa,
            "tse_analysis": value[0].tse_analysis,
            "rca_detail": value[0].rca_detail,
            "passdown": value[0].passdown
        }
        return HttpResponse(json.dumps(value1))
    else: return HttpResponse("No Submit")

@login_required
def search(request):
    count = Tblescalation.objects.all().count()
    context1 = {
    'count': count,
    }
    return render(request, 'base.html', context1)

@login_required
def case_details(request, number):
    queryset = Case.objects.filter(case_number=number)
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
