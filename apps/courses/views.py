from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import Course


# Create your views here.


class CourseListView(View):
    def get(self, request):
        sort = request.GET.get('sort', '')

        all_courses = Course.objects.all()
        recommend_course = all_courses.order_by('-students')[:3]

        if sort == '':
            all_courses = all_courses.order_by('-add_time')
        elif sort == 'hot':
            all_courses = all_courses.order_by('-fav_nums')
        else:
            all_courses = all_courses.order_by('-students')

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # objects = ['john', 'edward', 'josh', 'frank']

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(all_courses, per_page=2, request=request)

        all_courses = p.page(page)


        return render(request, 'course-list.html', {
            'sort': sort,
            'all_courses': all_courses,
            'pg': 'course',
            'recommend': recommend_course,
        })
