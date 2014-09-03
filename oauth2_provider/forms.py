from django import forms
from mongodbforms import DocumentForm

from .documents import get_application_doc


class AllowForm(forms.Form):
    allow = forms.BooleanField(required=False)
    redirect_uri = forms.CharField(widget=forms.HiddenInput())
    scope = forms.CharField(required=False, widget=forms.HiddenInput())
    client_id = forms.CharField(widget=forms.HiddenInput())
    state = forms.CharField(required=False, widget=forms.HiddenInput())
    response_type = forms.CharField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        data = kwargs.get('data')
        # backwards compatible support for plural `scopes` query parameter
        if data and 'scopes' in data:
            data['scope'] = data['scopes']
        return super(AllowForm, self).__init__(*args, **kwargs)


class RegistrationForm(DocumentForm):

    class Meta:
        document = get_application_doc()
        fields = ('name', 'client_id', 'client_secret', 'client_type',
            'authorization_grant_type', 'redirect_uris')
