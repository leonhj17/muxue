# _*_ encoding:utf-8 _*_
import xadmin

from .models import Course, BannerCourse, Lesson, Video, CourseResource


class CourseAdmin(object):
    list_display = ['courseorg','name','desc','teacher']
    list_filter = ['courseorg__name','name','desc','teacher__name']
    search_fields = ['courseorg','name','desc','teacher']


class LessonAdmin(object):
    list_display = ['course','name','learn_times','add_time']
    list_filter = ['course__name','name','learn_times','add_time']
    search_fields = ['course','name','learn_times']


class VideoAdmin(object):
    list_display = ['lesson','name','learn_times','url','add_time']
    list_filter = ['lesson__name','name','learn_times','url','add_time']
    search_fields = ['lesson','name','learn_times','url']

class CourseResourceAdmin(object):
    list_display = ['course','name','download','add_time']
    list_filter = ['course__name','name','download','add_time']
    search_fields = ['course','name','download']



xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)