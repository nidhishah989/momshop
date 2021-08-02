from django_mongoengine import mongo_admin as admin

from store.models import ArtWorks

# Register your models here.

#@admin.register(taglines)
#class taglinesAdmin(admin.DocumentAdmin):

@admin.register(ArtWorks)
class ArtWorksAdmin(admin.DocumentAdmin):
    
    pass


