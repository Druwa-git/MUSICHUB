from django import forms
from post.models import Record, Comment

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['song_title', 'song_intro', 'song_file']

        '''
        widgets = {
            'song_title': forms.TextInput(attrs={'class': 'form-control'}),
            'song_intro': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
        '''

        labels = {
            'song_title': 'Song Title',
            'song_intro': 'Detail Of Song',
            'song_file': 'Song File',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

        labels = {
            'content': 'Content',
        }
