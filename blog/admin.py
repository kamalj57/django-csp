from django.contrib import admin
from .models import QuillPost,Employee,Blog,NBlogs,Category,MyModel

from import_export.admin import ImportExportModelAdmin

@admin.register(QuillPost)
class QuillPostAdmin(admin.ModelAdmin):
    pass


class BlogAdmin(admin.ModelAdmin):
    
    list_display=('title','date_created','last_modified','is_draft')
    search_fields=('title',)

admin.site.register(Employee,ImportExportModelAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(NBlogs)
admin.site.register(Category)
admin.site.register(MyModel)