from django import forms
from .models import Patients, PatientProba, Score, Prida, Person, PridaMutations
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class PreeclampsiaForm(forms.ModelForm):
    class Meta:
        model = Patients
        # fields = ['patient_id', 'name', 'years']
        fields = ['patient_id', 'name', 'years', 'probe_date', 'birth_date', 'arterial_pressure', 'gw', 'baby_weight',
                  'erythrocytes', 'hemoglobin']


class PatientProbaForm(forms.ModelForm):

    class Meta:
        model = PatientProba
        fields = ['patient_id', 'name', 'years']
        # fields = ['name', 'years']


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ['name', 'value']


class PridaForm(forms.ModelForm):
    class Meta:
        model = Prida
        fields = ['code', 'number', 'age', 'sex', 'fvl', 'prothr', 'pai', 'mthfr']


class PridaMutationsForm(forms.ModelForm):
    class Meta:
        model = PridaMutations
        # fields = ['code', 'birth_year', 'age', 'fvl_ng', 'fvl_hetero', 'fvl_homo', 'prothr_ng', 'prothr_hetero', \
        #           'prothr_homo', 'pai_ng', 'pai_hetero', 'pai_homo', 'mthfr_ng', 'mthfr_hetero', 'mthfr_homo']
        #
        fields = ['code', 'age', 'fvl_ng', 'fvl_hetero', 'fvl_homo', 'prothr_ng', 'prothr_hetero',
                  'prothr_homo', 'pai_ng', 'pai_hetero', 'pai_homo', 'mthfr_ng', 'mthfr_hetero', 'mthfr_homo',
                  'abort']



class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'email', 'location']



