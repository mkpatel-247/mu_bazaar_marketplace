from django.urls import path
from listings import views


urlpatterns = [
    path("new-ads-listings/<str:uid>/",
         views.new_ad_listing, name='new_ad_listing'),
    path("ads/<str:id>/", views.single_page_ads, name='single_ads'),
    path("delete_listing/<str:uid>/<str:aid>/",
         views.delete_listing, name='delete_listing'),
     path("update_listing/<str:uid>/<str:aid>/",
         views.update_listing, name='update_listing'),
    path("listing/", views.all_listing, name="all_listing"),
    path("search/", views.search_listing, name="search"),
    path("wishlist_operations/<str:ads_id>/", views.wishlist_view, name="wishlist_operation")
    # path("profile/<str:uid>/", views.profile, name='profile'),
]
