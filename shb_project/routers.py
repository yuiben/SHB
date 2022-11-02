from rest_framework import routers

from shb_project.loan_infomations.urls import loan_urls


router = routers.SimpleRouter(trailing_slash=False)
urlpatterns = (
        router.urls + loan_urls
)
