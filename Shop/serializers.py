from rest_framework import serializers

from .models import Product,Price,Type


# class ProductSerializer(serializers.Serializer):

#     name = serializers.CharField(max_length=255)
#     count = serializers.IntegerField()
#     barcode = serializers.IntegerField()
#     update_date = serializers.DateField()
#     type_id = serializers.IntegerField()
#     price_id = serializers.IntegerField()

#     def create(self, validated_data):
#         return Product.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.price_id = validated_data.get('price_id', instance.price_id)
#         instance.barcode = validated_data.get('barcode', instance.barcode)
#         instance.type_id = validated_data.get('type_id', instance.type_id)
#         instance.update_date = validated_data.get('update_date', instance.update_date)
#         instance.count = validated_data.get('count', instance.count)
#         instance.save()
#         return instance


# class PriceSerializer(serializers.Serializer):

#     currency = serializers.CharField(max_length=255)
#     value = serializers.DecimalField(decimal_places=2, max_digits=10)

#     def create(self, validated_data):
#         return Price.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.currency = validated_data.get('currency', instance.currency)
#         instance.value = validated_data.get('value', instance.value)
#         instance.save()
#         return instance


# class TypeSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=255)
#     description = serializers.CharField(max_length=255)

#     def create(self, validated_data):
#         return Type.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.save()
#         return instance


from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):

    class Meta:

        model = Product
        fields = '__all__'


class TypeSerializer(serializers.ModelSerializer):

    class Meta:

        model = Type
        fields = '__all__'


class PriceSerializer(serializers.ModelSerializer):

    class Meta:

        model = Price
        fields = '__all__'
