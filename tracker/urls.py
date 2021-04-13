from django.urls import path

from tracker import views

app_name = 'tracker'

urlpatterns = [
    path('', views.PurchaseListView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('items/', views.ItemListView.as_view(), name='items'),
    path('item/new/', views.ItemCreateView.as_view(), name='item-new'),
    path('item/<int:pk>', views.ItemDetailView.as_view(), name='item-detail'),
    path('item/<int:pk>/delete/', views.ItemDeleteView.as_view(), name='item-delete'),
    path('item/<int:pk>/update/', views.ItemUpdateView.as_view(), name='item-update'),
    path('purchase/<int:pk>', views.PurchaseDetailView.as_view(), name='purchase-detail'),
    path('purchase/new/', views.PurchaseCreateView.as_view(), name='purchase-new'),
    path('purchase/<int:pk>/update/', views.PurchaseUpdateView.as_view(), name='purchase-update'),
    path('purchase/<int:pk>/delete/', views.PurchaseDeleteView.as_view(), name='purchase-delete'),
]