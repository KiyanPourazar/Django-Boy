from django.contrib import admin
from blog.models import Post, Category, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'author','counted_views', 'created_date', 'updated_date', 'status')
    list_filter = ('status','author',)
    # ordering = ('-created_date',)
    search_fields = ('title','content')
    sumernote_fields = ('content',)

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name', 'post','approved', 'created_date',)
    list_filter = ('post','approved',)
    search_fields = ('title','post')

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)