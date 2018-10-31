from rest_framework import serializers
from ..models import Person, Company
from signals.libs.serializers import AuditedModelSerializer
from signals.apps.authentication.api_v1.serializers import UserSerializer

class PersonSerializerAdmin(AuditedModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class CompanySerializerAdmin(AuditedModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class PersonSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    class Meta:
        model = Person
        fields = '__all__'

    """
    Overriding the default create method of the Model serializer.
    :param validated_data: data containing all the details of student
    :return: returns a successfully created student record
    """
    def create(self, validated_data):
        # Creation of user (Auth_user_model)
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)

        # Creation of specific type of user
        person, created = Person.objects.update_or_create(user=user,
                            **validated_data)
        return person

    def update(self, instance, validated_data):
        for field in validated_data:
            if field == 'password':
                instance.set_password(validated_data.get(field))
            else:
                instance.__setattr__(field, validated_data.get(field))
        instance.save()
        return instance

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
