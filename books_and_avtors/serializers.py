from rest_framework import serializers
class BooksSerializer(serializers.Serializer):
    book_name=serializers.CharField()
    book_cost=serializers.IntegerField()
    book_year=serializers.DateField()

class AvtorsSerializer(serializers.Serializer):
    avtor_name=serializers.CharField()
    avtor_bday=serializers.DateField()
    avtor_books_created_name=serializers.CharField()
    avtor_date_of_die=serializers.DateField()

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)