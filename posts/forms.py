from django import forms
from .models import Post,Category

cat_choice = Category.objects.all().values_list('name','name')
CATEGORY_CHOICES = []

for cat in cat_choice:
    CATEGORY_CHOICES.append(cat)

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
    
    category = forms.ChoiceField(
        choices=CATEGORY_CHOICES,
        label='Visibility',
        widget=forms.Select(attrs={'class': 'post-visibility'})
    )
    
    visibility = forms.ChoiceField(
        choices=MY_CHOICES,
        label='Visibility',
        widget=forms.Select(attrs={'class': 'post-visibility'})
    )
        
    class Meta:
        model = Post
        fields = ['title','content','category','visibility']