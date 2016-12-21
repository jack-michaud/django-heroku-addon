# from reroute import handler404, handler500, patterns, url, include
# from reroute.verbs import verb_url

from django.conf.urls import url
import api.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^$',               api.views.home),

    # Heroku-specific routes
	url(r'^heroku/resources$',                        api.views.heroku_provision),
	url(r'^heroku/resources/(?P<id>[0-9].*)$',        api.views.heroku_resources),
	url(r'^sso/login$',                               api.views.heroku_sso),
	url(r'^heroku/ssolanding$',                       api.views.heroku_sso_landing),
]
