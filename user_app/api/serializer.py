from django.contrib.auth.models import User
from    rest_framework import serializers

class RegisterSerializer(serializers.Serializer):
    password2=serializers.CharField(style={'input_type': "password"},write_only=True)
    class Meta:
        model = User
        fields=["username","email","password","password2"]
        extra_kwarg ={
            "password" :{"write_only":True}
        }
    def save(self):
        password1 = self.validated_data['password']
        password2=self.validated_data['password2']

        if password1 !=password2:
            raise serializers.ValidationError("password must be same")