from django.contrib import admin

from .models import Post, PostFile,Category

class PostFileInline(admin.TabularInline):
    model = PostFile
    template = 'hermes/postfiles.html'

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("subject", ), }
    exclude = ('summary',)
    list_display = ('subject', 'category', 'created_on', 'modified_on')
    list_filter = ('created_on', 'modified_on', 'category')
    search_fields = ('subject', 'slug')
    inlines = (PostFileInline, )

class CategoryAdmin(admin.ModelAdmin):
    include = ('title', 'parent')
    exclude = ('slug', )

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
