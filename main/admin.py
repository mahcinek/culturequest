from django.contrib import admin
from .models import Gm, Question, Quest, Answer, Location

admin.site.register(Gm)
admin.site.register(Quest)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Location)

# Register your models here.
