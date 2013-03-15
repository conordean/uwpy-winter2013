from django.contrib import admin
from uw.models import Activity, ActivitySchedule, Program


class ActivityAdmin(admin.ModelAdmin):
    """Admin interface for models.Activity."""
    list_display = ('author', 'content', )
    list_display_links = ('author', 'content', )


class ActivityScheduleAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'end_time', 'notes', )
    list_display_links = ('start_time', 'end_time')
    ordering = ('-start_time', )
    date_hierarchy = 'start_time'


#class UserProfileAdmin(admin.ModelAdmin):
#    list_display = ('user', 'date_created', 'gender', 'date_of_birth')
#    list_display_links = ('user', )
#    ordering = ('-date_created', )
#    date_hierarchy = 'date_created'


class ProgramAdmin(admin.ModelAdmin):
  """Admin interface for models.Program."""
  list_display = ('name', 'visible')
  list_filter = ('visible',)
  search_fields = ('name',)


admin.site.register(Activity, ActivityAdmin)
admin.site.register(ActivitySchedule, ActivityScheduleAdmin)
#admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Program, ProgramAdmin)
