from django import forms
from .models import Article

class ArticleModelForm(forms.ModelForm):
    image = forms.ImageField(label='', required=False)
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Title'}), label='')
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Start writing...'}), label='')
    class Meta:
        model = Article
        fields = [
            'image',
			'title',
			'content',
		]