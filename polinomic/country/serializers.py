from rest_framework import serializers
from .models import Country

class CountrySerializer(serializers.ModelSerializer):
    
    flag_png = serializers.URLField(required=False)
    flag_svg = serializers.URLField(required=False)
    flag_alt = serializers.CharField(required=False, allow_blank=True, allow_null=True)

    common_native_name = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    official_native_name = serializers.CharField(required=False, allow_blank=True, allow_null=True)

    latitude = serializers.FloatField(required=False, allow_null=True)
    longitude = serializers.FloatField(required=False, allow_null=True)

    class Meta:
        model = Country
        fields = [
            'name', 'official_name', 'common_name', 'official_native_name', 'common_native_name',
            'flag_png', 'flag_svg', 'flag_alt', 'capital', 'population', 'area', 'latitude', 'longitude',
            'timezones', 'continents'
        ]

    def to_internal_value(self, data):

        name_field = data.get('name', {})
        data['name'] = name_field.get('common', 'Unknown')
        data['official_name'] = name_field.get('official', 'Unknown')
        data['common_name'] = name_field.get('common', 'Unknown')

        native_names = name_field.get('nativeName', {})

        if isinstance(native_names, dict):
            first_native = next(iter(native_names.values()), {})
            data['official_native_name'] = first_native.get('official', 'Unknown')
            data['common_native_name'] = first_native.get('common', 'Unknown')

        else:
            data['official_native_name'] = 'Unknown'
            data['common_native_name'] = 'Unknown'

        flags = data.get('flags', {})
        data['flag_png'] = flags.get('png', '')
        data['flag_svg'] = flags.get('svg', '')
        data['flag_alt'] = flags.get('alt') or 'No description available'

        latlng = data.get('latlng', [])
        data['latitude'] = latlng[0] if len(latlng) > 0 else None
        data['longitude'] = latlng[1] if len(latlng) > 1 else None

        data['capital'] = data.get('capital', [])[0] if data.get('capital') else 'Unknown'

        return super().to_internal_value(data)

    def validate(self, data):

        return data

    def create(self, validated_data):

        country, created = Country.objects.update_or_create(
            name=validated_data['name'],
            defaults=validated_data
        )

        return country
