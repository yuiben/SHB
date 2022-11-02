from django.urls import path

from shb_project.loan_infomations.views import (
    create_loan_information,
    get_list_loan_information,
    update_loan_information,
    loan_information_detail,
    delete_loan_information,
)

loan_urls = [
    path("list-loan/", view=get_list_loan_information, name="list loan"),
    path("create-loan/", view=create_loan_information, name="create loan"),
    path("update-loan/", view=update_loan_information, name="update loan"),
    path("detail-loan/", view=loan_information_detail, name="detail loan"),
    path("delete-loan/", view=delete_loan_information, name="delete loan"),
]
