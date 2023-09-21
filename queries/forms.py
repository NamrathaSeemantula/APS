from django.forms import ModelForm
from django import forms
from . models import queries, answers

TAG_CHOICES = [
    ('Artificial_Intelligence', 'Artificial_Intelligence'),
    ('Machine_Learning', 'Machine_Learning'),
    ('Robotics', 'Robotics'),
    ('Internet_of_Things', 'Internet_of_Things'),
    ('Web_Development', 'Web_Development'),
    ('App_Development', 'App_Development'),
    ('Competitive_Programming', 'Competitive_Programming'),
]

class queryform(ModelForm):
    query = forms.CharField(widget=forms.Textarea(attrs={'rows':10, 'cols':120, 'class': 'input-fields', 'placeholder': 'Enter your query here'})) 
    tag = forms.CharField(label='Tag', widget=forms.Select(choices=TAG_CHOICES, attrs={'class': 'input-fields'}))

    class Meta:
        model = queries
        fields = ['query', 'tag']

class answersform(ModelForm):
    answer = forms.CharField(widget=forms.Textarea(attrs={'rows':10, 'cols':120, 'class': 'input-fields', 'placeholder': 'Enter your answer here'}))

    class Meta:
        model = answers
        fields = ['answer']
