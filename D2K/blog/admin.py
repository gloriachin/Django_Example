from django.contrib import admin

# Register your models here.

from .models import   Title, Subtitle, Paragraph

#admin.site.register(Question)#


#class TitleAdmin(admin.ModelAdmin):
#    fieldsets = [
#        (None,               {'fields': ['Title_text']}),
#        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#    ]

#class contentAdmin(admin.ModelAdmin):
#    fieldsets = [
#        (None,               {'fields': ['Title_text']}),
#        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#        ('sub title', {'field':['content_title']}),
#        ('content', {'field':['content_text']}),
#    ]
admin.site.register(Title)
admin.site.register(Subtitle)
admin.site.register(Paragraph)