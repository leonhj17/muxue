# _*_ encoding:utf-8 _*_
import xadmin

from .models import UserAsk,UserCourse,UserFavorite,UserMessage,CourseComments


class UserAskAdmin(object):
    list_display = ['name','mobile','course_name','add_time']
    list_filter = ['name','mobile','course_name','add_time']
    search_fields = ['name','mobile','course_name']


class UserCourseAdmin(object):
    list_display = ['user','course','add_time']
    list_filter = ['user','course__name','add_time']
    search_fields = ['user','course']


class UserFavoriteAdmin(object):
    list_display = ['user','fav_id','fav_type','add_time']
    list_filter = ['user__nick_name','fav_id','fav_type','add_time']
    search_fields = ['user','fav_id','fav_type']


class UserMessageAdmin(object):
    list_display = ['user','messages','has_read','add_time']
    list_filter = ['user','messages','has_read','add_time']
    search_fields = ['user','messages','has_read']


class CourseCommentsAdmin(object):
    list_display = ['user','course','comments','add_time']
    list_filter = ['user__nick_name','course__name','comments','add_time']
    search_fields = ['user','course','comments']


xadmin.site.register(UserAsk,UserAskAdmin)
xadmin.site.register(UserCourse,UserCourseAdmin)
xadmin.site.register(UserFavorite,UserFavoriteAdmin)
xadmin.site.register(UserMessage,UserMessageAdmin)
xadmin.site.register(CourseComments,CourseCommentsAdmin)
