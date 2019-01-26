from django.contrib import admin

from .models import User, Message, Scrap, Write


admin.site.register(User)
admin.site.register(Message)
admin.site.register(Scrap)
admin.site.register(Write)
