from django.contrib import admin

# Register your models here.

#from .models import Dates
# class DatesAdmin(admin.ModelAdmin):
#     list_display = ('date', 'peopleid', 'locationid')
#     search_fields = ('date',)
#     list_filter = ('peopleid', 'locationid')
#     ordering = ('date','peopleid',)
# admin.site.register(Dates,DatesAdmin)

from .models import Country
admin.site.register(Country)

from .models import ExaminationCategory
admin.site.register(ExaminationCategory)

from .models import People

class PeopleAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'mail')
    search_fields = ('surname', 'name')
    list_filter = ('surname',)
#Many to Many    filter_horizontal = ('countryid',)
    ordering = ('surname','-name',)
    fields = ('surname', 'name', 'mail' ,)
#Many to Many    raw_id_fields = ('countryid',)

admin.site.register(People,PeopleAdmin)

from .models import Examination
class ExaminationAdmin(admin.ModelAdmin):
    list_display = ('surname', 'dateofexam','notes')
    search_fields = ('dateofexam',)
    list_filter = ('dateofexam',)
admin.site.register(Examination,ExaminationAdmin)



from .models import Locations
admin.site.register(Locations)


from .models import MedicineCategory
admin.site.register(MedicineCategory)

from .models import Medicine
admin.site.register(Medicine)




from .models import SpecialUsers
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class SpecialUsersInline(admin.StackedInline):
    model = SpecialUsers
    can_delete = False
    verbose_name_plural = 'SpecialUsers'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (SpecialUsersInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

