from . import views
from django.urls import path
from django.contrib.sitemaps.views import sitemap
from core.sitemaps import PostSitemap
from .feeds import LatestPostsFeed

sitemaps = {
    'post': PostSitemap,
}

urlpatterns = [
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
    path('home/', views.PostList.as_view(), name='home-index'),
    path('<slug:slug>/', views.post_detail, name='post-detail'),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),

]