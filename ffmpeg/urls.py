from django.urls import path
from . import views
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

urlpatterns = [
    path("ffmpeg/version", views.FFMPEGVersion.as_view()),
    path("mediafiles/", views.MediaFiles.as_view()),
    path("invalidmediafiles/", views.InvalidMediaFiles.as_view()),
    path("mediafiles/<int:pk>", views.MediaDetail.as_view()),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="docs"),
    path("ffmpeg/getMediaInfo", views.GetMediaInfo.as_view()),
]
