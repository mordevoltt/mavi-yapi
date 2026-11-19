from .models import SiteSetting

def site_settings(request):
    try:
        setting = SiteSetting.get_settings()
    except Exception:
        setting = None
    return {
        'site_setting': setting
    }

