from django.contrib import admin
from django.conf import settings
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, PostFile, Category


class PostFileInline(admin.TabularInline):
    model = PostFile
    template = 'hermes/postfiles.html'


class PostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {"slug": ("subject", ), }
    exclude = ('summary',)
    list_display = ('subject', 'category', 'created_on', 'modified_on')
    list_filter = ('created_on', 'modified_on', 'category')
    search_fields = ('subject', 'slug')
    inlines = (PostFileInline, )

    class Media:
        css = {
            'all': (
                "http://fonts.googleapis.com/css?family=Source+Sans+Pro:200,300,400,700",
                '//cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.5/css/bootstrap.min.css',
                settings.STATIC_URL + 'css/admin_post.css',
            ),
        }
        js = [
            settings.STATIC_URL + 'js/jquery.min.js',
            '//cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.5/js/bootstrap.min.js']


class CategoryAdmin(admin.ModelAdmin):
    include = ('title', 'parent')
    exclude = ('slug', )

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
