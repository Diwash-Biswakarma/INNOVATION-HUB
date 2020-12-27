from django.contrib import admin
from .models import Work, Message, Blog, Apply, Media


class WorkAdmin(admin.ModelAdmin):
    pass


class BlogAdmin(admin.ModelAdmin):
    pass


class MessageAdmin(admin.ModelAdmin):
    pass


class ApplyAdmin(admin.ModelAdmin):
    pass


class MediaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Work, WorkAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Apply, ApplyAdmin)
admin.site.register(Media, MediaAdmin)


