from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from fitness.views import account, activity

urlpatterns = [
    path("accounts/", account.AccountListView.as_view(), name="account_list"),
    path(
        "account/<int:account_id>/",
        account.AccountView.as_view(),
        name="account_detail",
    ),
    path(
        "activity/<int:pk>/", activity.ActivityView.as_view(), name="activity_detail"
    ),
    path(
        "account/<int:account_id>/activities",
        activity.ActivityListView.as_view(),
        name="activity_list",
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
