from django.urls import path

from portxpress.news.views import (
    traffic_list_view,
    traffic_detail_view,
    news_list_view,
    news_detail_view
)

app_name = "news"
urlpatterns = [
    path("news/", view=news_list_view, name="news-list"),
    path("traffic/", view=traffic_list_view, name="traffic-list"),
    path("traffic/<str:slug>/", view=traffic_detail_view, name="traffic-detail"),
    path("news/<str:slug>/", view=news_detail_view, name="news-detail"),
]
