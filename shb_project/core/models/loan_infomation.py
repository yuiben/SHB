from django.db import models

from shb_project.common.model import BaseModel, ConstantsFields


class LoanInformation(BaseModel, ConstantsFields):
    name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    loan = models.DecimalField(max_digits=65, decimal_places=2)

    class Meta:
        db_table = 'loan_information'
