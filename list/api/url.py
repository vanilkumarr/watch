from django.urls import path
from . import views
urlpatterns=[
    path('list/', views.WatchlistAV.as_view(), name='seen'),
    path('list/<str:pk>', views.Moviedetail.as_view(), name='details'),
    path('stream/',views.StreamPlatformAV.as_view(),name='stream'),
    path('stream/<str:pk>',views.StreamdetailAV.as_view(),name="streamdetails"),
    path('stream/<str:pk>/reviews',views.ReviewdetailAV.as_view(),name="streamdetails"),
    path('stream/reviews/<str:pk>',views.ReviewList.as_view(),name='reviews')
]