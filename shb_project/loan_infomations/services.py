from shb_project.common.message import MessageError
from shb_project.core.models import LoanInformation
from shb_project.loan_infomations.serializers import LoanCreateSerializer, LoanSerializer


class LoanService:
    @classmethod
    def create_loan_information(cls, request):
        result = LoanCreateSerializer(data=request, many=False)
        result.is_valid(raise_exception=True)
        result.save()
        return result.data

    @classmethod
    def get_list_loan_information(cls):
        loan_list = LoanInformation.objects.all()
        result = LoanSerializer(loan_list, many=True)
        return result.data

    @classmethod
    def update_loan_information(cls, pk, request):
        loan = cls.get_loan_by_id(pk)
        if loan:
            result = LoanCreateSerializer(loan, data=request)
            result.is_valid(raise_exception=True)
            result.save()
            return result.data
        return MessageError.ID_NOT_EXITS.value

    @classmethod
    def loan_information_detail(cls, pk):
        loan = cls.get_loan_by_id(pk)
        if loan:
            result = LoanSerializer(loan, many=False)
            return result.data
        return MessageError.ID_NOT_EXITS.value

    @classmethod
    def get_loan_by_id(cls, pk):
        try:
            return LoanInformation.objects.get(pk=pk)
        except LoanInformation.DoesNotExist:
            return None


