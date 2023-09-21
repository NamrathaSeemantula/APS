from dataclasses import field
from django.forms import ModelForm
from django import forms
from . models import blogs, blogcomments

TAG_CHOICES = [
    ('Artificial_Intelligence', 'Artificial_Intelligence'),
    ('Machine_Learning', 'Machine_Learning'),
    ('Robotics', 'Robotics'),
    ('Internet_of_Things', 'Internet_of_Things'),
    ('Web_Development', 'Web_Development'),
    ('App_Development', 'App_Development'),
    ('Competitive_Programming', 'Competitive_Programming'),
]

class writeblogform(ModelForm):
    blogtopic = forms.CharField(widget=forms.Textarea(attrs={'rows':1,'class': 'input-fields', 'placeholder': 'Enter the topic of your blog here'}))
    blogcontent = forms.CharField(widget=forms.Textarea(attrs={'rows':8, 'cols':120, 'class': 'input-fields', 'placeholder': 'Enter the blog content here'})) 
    tag = forms.CharField(label='Tag', widget=forms.Select(choices=TAG_CHOICES,attrs={'class': 'input-fields'}))

    class Meta:
        model = blogs
        fields = ['blogtopic', 'blogcontent', 'tag']

class blogcommentsform(ModelForm):
    commentcontent = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'cols':60, 'class': 'input-fields', 'placeholder': 'Enter your comment here'}))

    class Meta:
        model = blogcomments
        fields = ['commentcontent']
