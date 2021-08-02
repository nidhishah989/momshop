from django_mongoengine import forms

from store import models


class ArtWorksForm(forms.DocumentForm):
   # artsize = forms.fields.EmbeddedDocumentField(artsizeInchForm)
    class Meta:
        document = models.ArtWorks
        fields = ['artname', 'description', 'available','paintingType','paintingCategory','priceUSA','painting_photo','tags']
