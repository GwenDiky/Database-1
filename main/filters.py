import django_filters
from django_filters import DateFilter
from .models import *
from django import forms 



class CardFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date", lookup_expr='gte', label="Дата вынесения с",  widget=forms.DateInput(attrs={'class': 'form-control', 'style': 'width:350px'}))
    end_date = DateFilter(field_name="date", lookup_expr='lte', label="по",  widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width:350px'}))
    proceeding = django_filters.MultipleChoiceFilter(choices=Card.PROCEEDING_CHOICES, label="Вид судопроизводства (выберите подходящее значение)", widget=forms.CheckboxSelectMultiple())
    trial = django_filters.MultipleChoiceFilter(choices=Card.TRIALS,label="Наименование суда (выберите подходящее значение)", widget=forms.CheckboxSelectMultiple())
    first_dispute = django_filters.MultipleChoiceFilter(choices=FirstDispute.CHOICES, label="Первая подкатегория спора (выберите подходящее значение)", widget=(forms.CheckboxSelectMultiple()))
    second1_dispute = django_filters.MultipleChoiceFilter(choices=Card.SECOND1_DISPUTE, label="Вторая (1) подкатегория спора (выберите подходящее значение)", widget=(forms.CheckboxSelectMultiple()))
    second2_dispute = django_filters.MultipleChoiceFilter(choices=Card.SECOND2_DISPUTE, label="Вторая (2) подкатегория спора (выберите подходящее значение)", widget=(forms.CheckboxSelectMultiple()))
    third_dispute = django_filters.MultipleChoiceFilter(choices=Card.THIRD_DISPUTE, label="Третья подкатегория спора (выберите подходящее значение)", widget=(forms.CheckboxSelectMultiple()))
    class Meta: 
        model = Card
        fields = ['proceeding', 'trial', 'first_dispute', 'start_date', 'end_date']
