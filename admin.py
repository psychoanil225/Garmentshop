from django.contrib import admin
from garments.models import FormalShirt
class FormalShirtAdmin(admin.ModelAdmin):
     list_display=('name','price','stock')

# Register your models here.
admin.site.register(FormalShirt, FormalShirtAdmin)
