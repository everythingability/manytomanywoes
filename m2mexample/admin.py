from django.contrib import admin
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe
from django.contrib.contenttypes.admin import  GenericTabularInline, GenericStackedInline 


#from genericadmin.admin import GenericAdminModelAdmin, TabularInlineWithGeneric

from .models import Relationship
from .models import Person, Funder, Organisation
from .models import ResearchCategory, ResearchArea, ResearchProject, HEResearchArea, HEResearchCategory

from  django.contrib.contenttypes.admin import GenericInlineModelAdmin
####################### RELATIONSHIPS ####################

'''class RelationshipInline(GenericAdminModelAdmin, GenericTabularInline):
    model = Relationship'''



class RelationshipAdminInLine( GenericInlineModelAdmin ):#GenericAdminModelAdmin):
    model = Relationship

    


####################### CONTENT OBJECTS ####################

class PersonInline(admin.StackedInline):
    model = Person
    inlines = [ RelationshipAdminInLine ]


class PersonAdmin(admin.ModelAdmin):
    ''
 

class ResearchProjectAdmin(admin.ModelAdmin):
    ''



class HEResearchCategoryInline(admin.StackedInline):
    model = HEResearchCategory
    #inlines = [ RelationshipInline ]


class HEResearchCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    #inlines = [ RelationshipInline ]

class HEResearchAreaAdmin(admin.ModelAdmin):
    #list_display = ('name','hecatname')
    list_filter = ['hecategory',]
    #inlines = [HEResearchCategoryInline]
    #inlines = [ RelationshipInline ]


admin.site.register(Relationship)

### CONTENT OBJECTS ####

admin.site.register(Person, PersonAdmin)
admin.site.register(Funder)
admin.site.register(Organisation)
admin.site.register(ResearchCategory)
admin.site.register(ResearchArea)
admin.site.register(HEResearchCategory, HEResearchCategoryAdmin)
admin.site.register(HEResearchArea, HEResearchAreaAdmin)
admin.site.register(ResearchProject, ResearchProjectAdmin)

#admin.site.register( Relationship, RelationshipAdmin)


### END CONTENT OBJECTS ####