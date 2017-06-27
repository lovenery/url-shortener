from django import forms
from .validators import validate_url, validate_dot_com

class SubmitUrlForm(forms.Form):
    url = forms.CharField(label='Your original URL here', validators=[validate_url, validate_dot_com])

    # def clean(self):
    #     cleaned_data = super(SubmitUrlForm, self).clean()
    #     print("forms.py, clean(): ", cleaned_data)
    #     url = cleaned_data.get('url')
    #     url_validator = URLValidator()
    #     try:
    #         url_validator(url)
    #     except:
    #         raise forms.ValidationError('Invalid URL for this field')

    # def clean_url(self):
    #     print("forms.py, clean_url(): ", self.cleaned_data)
    #     url = self.cleaned_data['url']
    #     url_validator = URLValidator()
    #     try:
    #         url_validator(url)
    #     except:
    #         raise forms.ValidationError('Invalid URL for this field')
    #     return url