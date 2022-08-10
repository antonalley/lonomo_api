from django.contrib import admin

# Register your models here.
from .models import Interest, RelatedInterest, PersonInterest, InterestCategory

admin.site.register(Interest)
admin.site.register(RelatedInterest)
admin.site.register(PersonInterest)
admin.site.register(InterestCategory)