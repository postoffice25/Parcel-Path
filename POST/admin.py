from django.contrib import admin

# Register your models here.
from.models import USER
admin.site.register(USER)
from.models import postman
admin.site.register(postman)
from.models import Feedback
admin.site.register(Feedback)
from.models import postoffice
admin.site.register(postoffice)
from.models import postmodel
admin.site.register(postmodel)
from.models import Reschedule
admin.site.register(Reschedule)
from.models import stamp
admin.site.register(stamp)