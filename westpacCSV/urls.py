from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
#import django.contrib
#django.contrib.admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'westpacCSV.views.home', name='home'),
    # url(r'^westpacCSV/', include('westpacCSV.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     #url(r'^admin/', include(django.contrib.admin.site.urls)),
)
