from django import forms
from .models import Post



class PostCreationForm(forms.ModelForm):

    MY_CHOICES = {
        'Private':'Private',
        'Public': 'Public'
    }
     
    title = forms.CharField(
    label='post title',
    widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Post Title'})
    )
    
    content = forms.CharField(
    label = 'post content here',
    widget=forms.Textarea(attrs={'class':'post-content','placeholder':'Enter Post content'})
    )
    
    visibility = forms.ChoiceField(
        choices=MY_CHOICES,
        label='Visibility',
        widget=forms.Select(attrs={'class': 'post-visibility'})
    )
        
    class Meta:
        model = Post
        fields = ['title','content','visibility']