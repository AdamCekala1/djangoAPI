from django.contrib import admin

# Register your models here.
from .models import AboutMe
from .models import Knowledge
from .models import Contact

admin.site.register(AboutMe)
admin.site.register(Knowledge)
admin.site.register(Contact)