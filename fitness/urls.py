from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from fitness import views

urlpatterns = [
    path("account/", views.AccountList.as_view(), name="account-list"),
    path(
        "account/<int:pk>/",
        views.AccountDetail.as_view(),
        name="account-detail",
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
