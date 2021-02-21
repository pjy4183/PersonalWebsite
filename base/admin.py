from django.contrib import admin

# Register your models here.

from .models import Post, Tag

class SnippetAdmin(admin.ModelAdmin):
    list_display = ('headline','created')

    def get_queryset(self, request):
        queryset = super(SnippetAdmin, self).get_queryset(request)
        queryset = queryset.order_by('headline')
        return queryset

admin.site.register(Post, SnippetAdmin)
admin.site.register(Tag)
