from django.contrib import admin

from .models import Post, Group, Follow, Comment


class PostAdmin(admin.ModelAdmin):
    """Для модели Post создана кастомная админка.
    Зарегистрированы модели Group, Follow, Comment."""
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group',
    )
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


admin.site.register(Post, PostAdmin)
admin.site.register(Group)
admin.site.register(Follow)
admin.site.register(Comment)
