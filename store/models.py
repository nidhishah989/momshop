from django_mongoengine import Document, fields,EmbeddedDocument
from django.utils import timezone


class ArtWorks(Document):
    artname=fields.StringField(max_length=200)
    description=fields.StringField(max_length=700,row=5)
    artType = (
        ('Acrylic', 'Acrylic Painting'),
        ('WaterColor', 'WaterColor Painting'),
        ('fabric', 'fabric Painting')
       )
    paintingType = fields.StringField(max_length=30,choices=artType,default='Acrylic')
    artCategory=(
        ('landscape','Landscape Painting'),
        ('still life','Still Life Painting'),
        ('portrait', 'Portrait Painting'),
        ('Religious','Religious Painting'),
        ('flower', 'Flower painting'),
        ('Animal','Animal Painting'),
        ('bird', 'bird Painting')
    )
    paintingCategory = fields.StringField(max_length=30,choices=artCategory,default='landscape')
    priceUSA= fields.DecimalField(min_value=0,max_digits=6,precision=2)
    #wishCount= fields.IntField(min_value=0)
    available= fields.BooleanField()
    tags= fields.ListField(fields.StringField(max_length=30))
    painting_photo= fields.ImageField(size=(300,400,False))
    artsizeInch=fields.DictField()
    
    created_date = fields.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.artname