from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.decorators import api_view
from rest_framework.response import Response

from shb_project.common.message import MessageError
from shb_project.core.models import LoanInformation
from shb_project.loan_infomations.serializers import LoanCreateSerializer
from shb_project.loan_infomations.services import LoanService


@extend_schema(
    request=LoanCreateSerializer,
    responses={200: {}},
    methods=['POST'], )
@api_view(["POST"])
def create_loan_information(request):
    data = LoanService.create_loan_information(request.data)
    return Response({'data': data})


@extend_schema(
    responses={200: {}},
    methods=['GET'], )
@api_view(["GET"])
def get_list_loan_information(request):
    data = LoanService.get_list_loan_information()
    return Response({'data': data})


@extend_schema(
    parameters=[
          OpenApiParameter("id", OpenApiTypes.INT, OpenApiParameter.QUERY),
        ],
    request=LoanCreateSerializer,
    responses={200: {}},
    methods=['PUT'], )
@api_view(["PUT"])
def update_loan_information(request):
    pk = request.GET.get('id')
    data = LoanService.update_loan_information(pk, request.data)
    return Response({'data': data})


@extend_schema(
    parameters=[
          OpenApiParameter("id", OpenApiTypes.INT, OpenApiParameter.QUERY),
        ],
    request=LoanCreateSerializer,
    responses={200: {}},
    methods=['GET'], )
@api_view(["GET"])
def loan_information_detail(request):
    pk = request.GET.get('id')
    data = LoanService.loan_information_detail(pk)
    return Response({'data': data})


@extend_schema(
    parameters=[
          OpenApiParameter("id", OpenApiTypes.INT, OpenApiParameter.QUERY),
        ],
    request=LoanCreateSerializer,
    responses={200: {}},
    methods=['DELETE'], )
@api_view(["DELETE"])
def delete_loan_information(request):
    pk = request.GET.get('id')
    try:
        snippet = LoanInformation.objects.get(pk=pk)
        snippet.delete()
    except:
        return Response({'data': MessageError.ID_NOT_EXITS.value})
    return Response({'status': 200})
