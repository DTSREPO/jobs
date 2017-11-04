from django.conf.urls import include, url
from jobpost_app.views.frontend.index_view import (index_view)
from jobpost_app.views.frontend.category_job_list_view import (cat_job_list)
from jobpost_app.views.frontend.upload_file_provider import (upload_file_provider_view)
from jobpost_app.views.backend.backend_index_view import (backend_index_view)
from jobpost_app.views.backend.backend_settings_view import (CrudSiteSetting)
from jobpost_app.views.backend.backend_category_view import (backend_category_view, CategoryCrud)
from jobpost_app.views.backend.backend_industry_view import (backend_industry_view, IndustryCrud)
from jobpost_app.views.backend.backend_location_view import (backend_location_view, LocationCrud)

urlpatterns = [
    # Frontend Part
    url(r'^$', index_view, name='index'),
    url(r'^(?P<cat_id>[0-9]*)$', cat_job_list, name='cat-job'),

    # Backend Part
    url(r'^admin/settings/$', CrudSiteSetting.as_view(), name='site-settings'),
    url(r'^admin/dashboard/$', backend_index_view, name='backend_index'),
    url(r'^admin/category/$', backend_category_view, name='cat-list'),
    url(r'^admin/category-form/(?P<cat_id>[0-9]*)$', CategoryCrud.as_view(), name='cat-form'),
    url(r'^admin/industry/$', backend_industry_view, name='ind-list'),
    url(r'^admin/industry-form/(?P<ind_id>[0-9]*)$', IndustryCrud.as_view(), name='ind-form'),
    url(r'^admin/location/$', backend_location_view, name='job-loc'),
    url(r'^admin/location-form/(?P<loc_id>[0-9]*)$', LocationCrud.as_view(), name='loc-form'),
    url(r'^upload_dir/(?P<file_path>.*)', upload_file_provider_view, name="upload_file_provider"),


]
