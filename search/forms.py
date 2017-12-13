from django import forms
from search.models import Post, Tblescalation, Case


class loginForm(forms.Form):
    log = forms.CharField(label='Your Name', max_length=None)


class SignUpForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('post',)

class SuggestionForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    suggestion = forms.CharField(widget=forms.Textarea)


class TblescalationForm(forms.ModelForm):
    class Meta:
        model = Tblescalation
        # exclude = ['user', 'seven_step']
        fields = ('utid','fab_code', 'case_id', 'tse_owner', 'problem_statement', 'case_description', 'system', 'subsystem', 'fault', 'fix_rca', 'rca_detail', 'poa', 'passdown', 'tse_analysis')


class SearchForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ('case_number', 'utid',)
