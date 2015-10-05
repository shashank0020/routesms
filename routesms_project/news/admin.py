from django.contrib import admin

# Register your models here.
from .models import Question,Choice,template_name,comment

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(template_name)
admin.site.register(comment)