import re
from datetime import datetime

from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
from django.core.urlresolvers import reverse

from user.models import UserSession


class UserMiddle(MiddlewareMixin):
    def process_request(self, request):
        paths=['/user/login/','/user/register/','/user/home/',
               '/media/df_goods/',
               '/backadmin/index/','/backadmin/productlist/',
               '/backadmin/productdetail/','/backadmin/recyclebin/',
               '/backadmin/login/','/backadmin/deletegood/',
               '/backadmin/recovergood/']


        for path in paths:
            if re.match(path,request.path):
                return None

        session = request.COOKIES.get('session')
        if not session:
            return HttpResponseRedirect(reverse('user:login'))

        user = UserSession.objects.filter(session=session).first()
        if not user:
            return HttpResponseRedirect(reverse('user:login'))

        if user.out_time.replace(tzinfo=None) < datetime.now():
            user.delete()
            return HttpResponseRedirect(reverse('user:login'))

        request.user = user.user
