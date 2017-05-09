# _*_ encoding:utf-8 _*_
import xadmin

from .models import CityDict, Teacher, CourseOrg


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    list_filter = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'tag','category','click_nums','fav_nums',
                    'image','address','city','students','course_nums','add_time']
    list_filter = ['name', 'desc', 'tag','category','click_nums','fav_nums',
                    'image','address','city','students','course_nums','add_time']
    search_fields = ['name', 'desc', 'tag','category','click_nums','fav_nums',
                    'image','address','city','students','course_nums']


class TeacherAdmin(object):
    list_display = ['name', 'org', 'work_years','work_company','work_position','points',
                    'click_nums','fav_nums','age','image','add_time']
    list_filter = ['name', 'org__name', 'work_years','work_company','work_position','points',
                    'click_nums','fav_nums','age','image','add_time']
    search_fields = ['name', 'org', 'work_years','work_company','work_position','points',
                    'click_nums','fav_nums','age','image']



xadmin.site.register(CityDict,CityDictAdmin)
xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(Teacher,TeacherAdmin)