from django.urls import path
from conversations import views

app_name = 'conversations'

urlpatterns = [
    path('inbox/', views.inbox, name=''),
    path('<int:pk>/', views.detail, name='detail'),
    path('new/<int:item_pk>/', views.new_conversation, name='new'),
]