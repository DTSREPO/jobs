from django.shortcuts import render
from jobpost_app.models import SiteSetting
from django.views import View
from django.http import FileResponse
from django.conf import settings
import os


# Create your views here.
class CrudSiteSetting(View):
    template = "jobpost_app/backend/site_settings.html"

    def get(self, request, site_id=None):
        context = {}
        return render(request, self.template, context)

    def post(self, request):

        try:
            site_info = SiteSetting.objects.get(pk=1)
            site_id = int(site_info.id)
        except SiteSetting.DoesNotExist:
            site_info = None
            site_id = None

        title = request.POST.get('site_title', '')
        logo_file = request.FILES.get('image_file', None)

        if logo_file is not None:
            logo_file_path = logo_file.name
        else:
            logo_file_path = ""

        meta_title = request.POST.get('meta_title', '')
        meta_description = request.POST.get('meta_desc', '')
        meta_keyword = request.POST.get('meta_keyword', '')
        short_desc = request.POST.get('short_desc', '')
        long_desc = request.POST.get('long_desc', '')
        copyrights = request.POST.get('copyright', '')
        # create_date = None
        # update_date = None

        if site_info:
            site = SiteSetting.objects.get(pk=site_id)
            site.title = title
            site.logo_file_path = logo_file_path
            site.meta_title = meta_title
            site.meta_description = meta_description
            site.meta_keyword = meta_keyword
            site.short_desc = short_desc
            site.long_desc = long_desc
            site.copyrights = copyrights
            # loc.active=status
            site.save()
            msg = 'Data Updated Successfully'
        else:
            site = SiteSetting(
                title=title,
                logo_file_path=logo_file_path,
                meta_title=meta_title,
                meta_description=meta_description,
                meta_keyword=meta_keyword,
                short_desc=short_desc,
                long_desc=long_desc,
                copyrights=copyrights
            )
            site.save()

            if logo_file:
                with open(settings.UPLOAD_DIR + os.sep + logo_file.name, "wb") as fw:
                    for c in logo_file.chunks():
                        fw.write(c)

            msg = 'Data Inserted Successfully'
        context = {'title': 'Site Settings Form', 'site': site, 'msg': msg}
        return render(request, self.template, context)
