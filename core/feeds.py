from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.utils.feedgenerator import Atom1Feed
from .models import Post
from django.urls import reverse


class LatestPostsFeed(Feed):
    feed_type = Atom1Feed
    title = "My blog"
    link = ""
    description = "New posts of my blog."

    def items(self):
        return Post.objects.filter(status=1)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.content, 30)
