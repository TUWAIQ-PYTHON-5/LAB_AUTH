from django.contrib import admin
from .models import Clinc, Review
# Register your models here.


#to customize the panel
class ClincAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'clinc')
    list_filter = ('clinc',)

admin.site.register(Clinc, ClincAdmin)
admin.site.register(Review, ReviewAdmin)

