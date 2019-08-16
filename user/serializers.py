from rest_framework import serializers
from user.models import MultilingualUser
from django.utils.translation import ugettext as _


class MultilingualUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = MultilingualUser
        fields = ('username', 'first_name', 'last_name', 'position', 'image_id')

    def to_representation(self, user):
        user_dict = super().to_representation(user)
        return {
            _('username'): user_dict['username'],
            _('first name'): user_dict['first_name'],
            _('last name'): user_dict['last_name'],
            _('position'): user_dict['position'],
            _('image id'): user_dict['image_id']
        }
