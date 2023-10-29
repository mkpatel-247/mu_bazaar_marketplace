from django.urls import path
from profiles import views


urlpatterns = [
    path("profile/<str:uid>/", views.profile, name='profile'),
    path("dashboard/<str:uid>/", views.dashboard, name='dashboard'),
    path("wishlist/", views.wishlist, name='wishlist'),
    path("inbox/", views.inbox, name='inbox'),
    # path('<int:pk>/', views.detail, name='detail'),
    # path("conversation/<str:adsid>/", views.new_conversation, name='conversation'),
    
    
]
