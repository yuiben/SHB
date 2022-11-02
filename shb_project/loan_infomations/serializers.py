from rest_framework import serializers

from shb_project.core.models import LoanInformation


class LoanCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(allow_null=True, required=False)
    last_name = serializers.CharField(allow_null=True, required=False)

    class Meta:
        model = LoanInformation
        fields = ('id', 'name', 'first_name', 'last_name', 'phone', 'address', 'loan')

    def create(self, validated_data):
        loan = LoanInformation.objects.create(**validated_data)
        return loan

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanInformation
        fields = '__all__'


