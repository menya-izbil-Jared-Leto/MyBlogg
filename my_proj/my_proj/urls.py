from django.contrib import admin
from django.urls import include, path
from django.contrib.sitemaps.views import sitemap
from my_app.sitemaps import PostSitemap

sitemaps = {
    'posts': PostSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('my_app/', include("my_app.urls", namespace='blog')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap')
]
