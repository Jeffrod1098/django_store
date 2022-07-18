from dataclasses import fields
from rest_framework import serializers
from .models import User,Item,Cart,CartItem,Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password', 'username',]
        extra_kwargs = {'password': {'write_only':True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model= Item
        fields = ('id', 'name', 'price', 'details', 'photo_1_url', 'photo_2_url',)

class CartSerializer(serializers.HyperlinkedModelSerializer):

    userId = UserSerializer()

    class Meta:
        model = Cart 
        fields = ('id', 'userId', 'quantity')

class CartItemSerializer(serializers.HyperlinkedModelSerializer):

    cartId = CartSerializer()
    itemId = ItemSerializer()

    class Meta:
        model = CartItem
        fields = ('id', 'cartId', 'itemId', 'quantity')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    item = ItemSerializer()

    user = UserSerializer()

    class Meta:
        model= Comment
        fields = ('title', 'content', 'item', 'user', 'created')
