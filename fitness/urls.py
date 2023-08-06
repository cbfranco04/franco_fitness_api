from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from fitness import views

urlpatterns = [
    path("account/", views.AccountListView.as_view(), name="account-list"),
    path(
        "account/<int:account_id>/",
        views.AccountView.as_view(),
        name="account_detail",
    ),
    path('activities/<int:pk>/', views.ActivityView.as_view(), name='activity_detail'),
    path(
        "account/<int:account_id>/activities",
        views.ActivityListView.as_view(),
        name="activity_list",
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
