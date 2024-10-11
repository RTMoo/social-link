from rest_framework import serializers
from django.contrib.auth import authenticate


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        if email and password:
            user = authenticate(username=email, password=password)
            if user is None:
                raise serializers.ValidationError("Неверные данные для входа.")
        else:
            raise serializers.ValidationError("Необходимо указать email и пароль.")

        data['user'] = user
        return data
