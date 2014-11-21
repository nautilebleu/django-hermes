from django.contrib import admin

from .models import Post, Category


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("subject", ), }
    list_display = ('subject', 'category', 'created_on', 'modified_on')
    list_filter = ('created_on', 'modified_on', 'category')
    search_fields = ['subject', 'slug']

class CategoryAdmin(admin.ModelAdmin):
    include = ('title', 'parent', 'slug')
    prepopulated_fields = {"slug": ("title", ), }

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
