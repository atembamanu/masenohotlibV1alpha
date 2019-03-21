from django.contrib import admin

from msuhotlib.models import (Person, MsuFacultyList,
                              MsuDepartmentList, StudySemester, DeptUnit, LectureResource,
                              LibrarianResource, AdminTutorial, AdminResource, AdminChallenge, AdminHowToRepo)

# Register your models here.

admin.site.register(Person)
admin.site.register(MsuFacultyList)
admin.site.register(MsuDepartmentList)
admin.site.register(StudySemester)
admin.site.register(DeptUnit)
admin.site.register(LectureResource)
admin.site.register(LibrarianResource)
admin.site.register(AdminChallenge)
admin.site.register(AdminTutorial)
admin.site.register(AdminResource)
admin.site.register(AdminHowToRepo)

