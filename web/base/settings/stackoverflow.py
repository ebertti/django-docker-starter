# coding: utf-8

from django.views import debug
from django.conf import settings

FEITO = False
def get_search_link():

    search_urls = {
        "stackoverflow": "http://stackoverflow.com/views?q=[python] or "
                         "[django]+{{ exception_value|force_escape }}",
        "googlesearch": "https://www.google.com.tr/#q="
                        "+django+{{ exception_value|force_escape }}"
    }

    return search_urls['stackoverflow'], search_urls['googlesearch']


def _patch_django_debug_view():
    global FEITO
    if FEITO:
        return

    new_data = """
        <h3 style="margin-bottom:10px;">
            View in
            <a href="%s"
             target="_blank">Stackoverflow</a> or
             <a href="%s"
             target="_blank">Google</a>
        </h3>
    """ % get_search_link()

    replace_point = '<table class="meta">'
    replacement = new_data + replace_point

    # monkey patch the built-in template.
    debug.TECHNICAL_500_TEMPLATE = debug.TECHNICAL_500_TEMPLATE.replace(
        replace_point,
        replacement,
        1  # replace the first occurence
    )
    FEITO = True


'''

<!-- Sentry JS SDK 2.1.+ required -->
<script src="https://cdn.ravenjs.com/2.1.0/raven.min.js"></script>

<script>
// configure the SDK as you normally would
Raven.config('https://1dee9ec4f5be48da9a4ae14a903b7ea2@sentry.io/142474').install();

function handleRouteError(err) {
  Raven.captureException(err);
  Raven.showReportDialog();
};
</script>
'''

def middleware(get_response):
    if settings.DEBUG:
        _patch_django_debug_view()

    def middleware(request):
        return get_response(request)

    return middleware
