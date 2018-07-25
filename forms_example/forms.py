from django import forms


class ReviewForm(forms.Form):
    input = forms.CharField(label='Your comment', max_length=100)
