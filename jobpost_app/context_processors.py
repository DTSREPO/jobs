from jobpost_app import models


def site_settings(request):
    try:
        site_sets = models.SiteSetting.objects.get(pk=1)
    except models.SiteSetting.DoesNotExist:
        site_sets = None

    return {'site_sets': site_sets, 'title': 'Site Settings'}