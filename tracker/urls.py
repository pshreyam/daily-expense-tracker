from django.urls import path

from tracker import views

urlpatterns = [
    path('', views.PurchaseListView.as_view(), name='tracker-home'),
    path('about/', views.about, name='tracker-about'),
    path('items/', views.ItemListView.as_view(), name='tracker-items'),
    path('item/new/', views.ItemCreateView.as_view(), name='tracker-item-new'),
    path('item/<int:pk>', views.ItemDetailView.as_view(), name='tracker-item-detail'),
    path('item/<int:pk>/delete/', views.ItemDeleteView.as_view(), name='tracker-item-delete'),
    path('item/<int:pk>/update/', views.ItemUpdateView.as_view(), name='tracker-item-update'),
    path('purchase/<int:pk>', views.PurchaseDetailView.as_view(), name='tracker-purchase-detail'),
    path('purchase/new/', views.PurchaseCreateView.as_view(), name='tracker-purchase-new'),
    path('purchase/<int:pk>/update/', views.PurchaseUpdateView.as_view(), name='tracker-purchase-update'),
    path('purchase/<int:pk>/delete/', views.PurchaseDeleteView.as_view(), name='tracker-purchase-delete'),
]