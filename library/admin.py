from django.contrib import admin

from library.models import AuthorModel, BookModel, CategoryModel

@admin.register(AuthorModel)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'created_at']
    search_fields = ['name']
    list_filter = ['created_at']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'created_at']
    search_fields = ['name']
    list_filter = ['created_at']
    prepopulated_fields = {'slug': ('name',)}
    
@admin.register(BookModel)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'author', 'category', 'isbn', 'available_copies']
    search_fields = ['title', 'isbn']
    list_filter = ['author', 'category']
    prepopulated_fields = {'slug': ('title',)}    