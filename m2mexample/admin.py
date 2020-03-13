from django.contrib import admin
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe
from django.contrib.contenttypes.admin import  GenericTabularInline, GenericStackedInline 

from .models import Relation,Relationship
from .models import Person, Funder, Organisation
from .models import ResearchCategory, ResearchArea, ResearchProject


####################### RELATIONSHIPS ####################

class RelationInline(GenericTabularInline):
    model = Relation
    extra = 1

class RelationAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'content_object', )
    
 

class OtherOjectInline(GenericStackedInline):
    model = Relationship
    extra = 1

class RelationshipInline(GenericStackedInline):
    model = Relationship
    extra = 1


class RelationshipAdmin(admin.ModelAdmin):
    exclude = ['reverse_name' ]
    list_display = ('__str__', 'kind','reverse_name' )
    search_fields = ['kind', "reverse_name"]

    inlines = [RelationInline]

####################### CONTENT OBJECTS ####################

class PersonInline(admin.StackedInline):
    model = Person


class ResearchProjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [RelationshipInline,RelationInline]


admin.site.register(Relationship, RelationshipAdmin)
admin.site.register(Relation)

### CONTENT OBJECTS ####
admin.site.register(Person)
admin.site.register(Funder)
admin.site.register(Organisation)
admin.site.register(ResearchCategory)
admin.site.register(ResearchArea)
admin.site.register(ResearchProject)
### END CONTENT OBJECTS ####