from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreatePostView, CreateUserView, CreateLickView, UserPostView, UserProfileView

urlpatterns = {
    url(r'^auth/', include('rest_framework.urls')),
    url(r'^Posts/$', CreatePostView.as_view(), name="create_post"),
    url(r'^Users/$', CreateUserView.as_view(), name="create_user"),
    url(r'^Licks/$', CreateLickView.as_view(), name="create_licks"),
    url(r'^UserPostView/$', UserPostView.as_view(), name="view_user_posts"),
    url(r'^UserProfileView/$', UserProfileView.as_view(),name="view_user_details")

}

urlpatterns = format_suffix_patterns(urlpatterns)

