from django.contrib import admin
from goodcauses.models import Signin, Profile, Feedback, Funds, UserProfileInfo

# Register your models here.
admin.site.register(Signin)
admin.site.register(Profile)
admin.site.register(Feedback)
admin.site.register(Funds)
admin.site.register(UserProfileInfo)
