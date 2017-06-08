# _*_ encoding:utf-8 _*_
from django.shortcuts import render
from django.views.generic import View

from .models import CityDict, CourseOrg

# Create your views here.


class OrgView(View):
    def get(self, request):
        all_city = CityDict.objects.all()
        all_org = CourseOrg.objects.all()

        return render(request, 'org-list.html', {
            'all_city':all_city,
            'all_org':all_org
        })
