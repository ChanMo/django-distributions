from rest_framework import serializers

from .models import *


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ('name', 'slug', 'icon', 'description', 'get_android_version_name', 'get_android_version_number', 'get_android_version_content', 'get_ios_version_name', 'get_ios_version_number', 'get_ios_version_content', 'get_android_url', 'get_ios_url')

class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Version
        fields = ('app__name', 'platform', 'name', 'number', 'content', 'created')
