# _*_ encoding:utf-8 _*_
from django.shortcuts import render, render_to_response
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import CityDict, CourseOrg


# Create your views here.


class OrgView(View):
    def get(self, request):
        all_city = CityDict.objects.all()
        all_org = CourseOrg.objects.all()

        # 筛选城市
        city_id = request.GET.get('city', "")
        if city_id:
            all_org = all_org.filter(city_id=int(city_id))

        # 筛选机构类别
        category = request.GET.get('ct', "")
        if category:
            all_org = all_org.filter(category=category)

        org_num = all_org.count()

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # objects = ['john', 'edward', 'josh', 'frank']

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(all_org, per_page=4, request=request)

        all_org = p.page(page)

        # return render_to_response('org-list.html', {
        #     'all_org': all_org,
        #     'all_city':all_city
        # })
        return render(request, 'org-list.html', {
            'all_city': all_city,
            'city_id': city_id,
            'all_org': all_org,
            'org_num': org_num,
            'category': category
        })
