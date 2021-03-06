from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse

from accounts.api.serializers import UserPublicSerializer
from books.models import Books

'''
**serializers turn data into JSON data which make it able to be stored on drives**
JSON -- JavaScript Object Notation
json.dumps(data)
data = {'abc': 123}

Serializers --> JSON
Serializers --> validate Data
'''


class BooksSerializer(serializers.ModelSerializer):
    # Comment: whats the difference between having attributes up
    # or under meta?


    # title           = serializers.CharField(max_length=50)
    # # uri             = serializers.SerializerMethodField(read_only=True) <-- DO NOT DELETE. figure out what this is used for.
    # user            = UserPublicSerializer(read_only=True)
    # # user_id          =serializers.PrimaryKeyRelatedField(source='user', read_only=True)
    # # user        =serializers.SlugRelatedField(read_only=True, slug_field='username') # source='email' <-- pulls email info
    #
    class Meta:
        model = Books
        fields = [
            # 'uri',
    #         # 'user_id',
    #         # 'id', # ?
            'title',
            'author',
            'user',
            'content',
            'image',
            'rentalRate',
            'timestamp',
            'condition',
            'id', # <-- Automatically comes in
        ]
    #     read_only_fields = ['user'] #GET calls only. change users anymore

    # def get_user(self,obj):
    #     request = self.context.get('request')
    #     user = obj.user
    #     return UserPublicSerializer(user, read_only=True, context={"request"}).data


    # def get_uri(self, obj):
    #     request = self.context.get('request')
    #     return api_reverse('api-books:detail', kwargs={'id': obj.id}, request=request)

    #field level validation
    # def validate_<fieldname>(self, value):
    # def validate_content(self, value):
    #     if len(value) > 10000:
    #         raise serializers.ValidationError("This is way too long")
    #     return value

    # def validate(self, data):
    #     content = data.get("content", None)
    #     if content == "":
    #         content = None
    #     image = data.get("image", None)
    #     if content is None and image is None:
    #         raise serializers.ValidationError("content or image is required")
    #     return data
