from django.urls import path
from . import views
from .views import PostCreateView, ItemDetail, ItemUpdateView, ItemDeleteView
from django.conf import settings
from django.conf.urls.static import static
from .views import contact



urlpatterns = [
    path('', views.home, name='findme-home'),
    path('found/', views.itemfound, name='findme-found'),
    path('contact/', views.contact, name='findme-contact'),
    path('item/create/', PostCreateView.as_view(), name='create'),
    path('item/<int:pk>/', ItemDetail.as_view(), name='detail'),
    path('founditem/<int:pk>/update', ItemUpdateView.as_view(), name='item-update'),
    path('founditem/<int:pk>/delete', ItemDeleteView.as_view(), name='item-delete'),
    path('found/<int:ItemID>', views.found, name='found'), 
    
    ]
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
