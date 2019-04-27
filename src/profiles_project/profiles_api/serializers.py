from rest_framework import serializers
from . import models


class HelloSerializer(serializers.Serializer):
    '''Serializes a name field for testing APIViews'''

    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for user profile object"""

    # Specifies what classes we want from models
    class Meta:
        model = models.UserProfile
        fields = ('id', 'name', 'email', 'password')
        # Extra keyword argument
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Create and return a new user"""

        user = models.UserProfile(
            email = validated_data['email'],
            name = validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
