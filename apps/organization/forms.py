# _*_ encoding:utf-8 _*_
import re

from django.forms import ModelForm
from django import forms

from operation.models import UserAsk


class UserAskForm(ModelForm):
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        REGEX = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
        p = re.compile(REGEX)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(u'手机号码非法', code='mobile_invalid')
