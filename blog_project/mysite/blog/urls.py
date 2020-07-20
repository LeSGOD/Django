from django.conf.urls import url
from blog import views

app_name = 'blog'


urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^post/new/$', views.PostCreateView.as_view(), name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$',
        views.PostUpdateView.as_view(), name='post_edit'),
    url(r'^post/(?P<pk>\d+)/remove/$',
        views.PostDeleteView.as_view(), name='post_remove'),
    url(r'^drafts/$', views.DraftListView.as_view(), name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/comment/$',
        views.add_comment_to_post.as_view(), name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$',
        views.comment_approve.as_view(), name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$',
        views.comment_remove.as_view(), name='comment_remove'),
    url(r'^comment/(?P<pk>\d+)/publish/$',
        views.post_publish.as_view(), name='post_publish'),
]
