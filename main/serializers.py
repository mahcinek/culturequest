from rest_framework import serializers
from main.models import Location, Quest, Question, Gm, Answer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('text', 'is_valid', 'id')

    def create(self, validated_data):
        """
        Create and return a new `Location` instance, given the validated data.
        """
        return Location.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Location` instance, given the validated data.
        """
        instance.text = validated_data.get('text', instance.text)
        instance.is_valid = validated_data.get('is_valid', instance.is_valid)
        instance.save()
        return instance


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ('name', 'desc', 'logo', 'long', 'lat', 'id')

    def create(self, validated_data):
        """
        Create and return a new `Location` instance, given the validated data.
        """
        return Location.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Location` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.desc = validated_data.get('desc', instance.desc)
        instance.logo = validated_data.get('logo', instance.logo)
        instance.long = validated_data.get('long', instance.long)
        instance.lat = validated_data.get('lat', instance.lat)
        instance.save()
        return instance


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ('exp', 'content', 'answers', 'id')

    def create(self, validated_data):
        """
        Create and return a new `Location` instance, given the validated data.
        """
        return Location.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Location` instance, given the validated data.
        """
        instance.exp = validated_data.get('exp', instance.exp)
        instance.content = validated_data.get('content', instance.content)
        instance.answers = validated_data.get('answers', instance.answers)
        instance.save()
        return instance


class QuestSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    location = LocationSerializer()

    class Meta:
        model = Quest
        fields = ('questions', 'name', 'desc', 'image', 'bonus', 'location', 'id')

    def create(self, validated_data):
        """
        Create and return a new `Location` instance, given the validated data.
        """
        return Location.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Location` instance, given the validated data.
        """
        instance.questions = validated_data.get('questions', instance.questions)
        instance.name = validated_data.get('name', instance.name)
        instance.desc = validated_data.get('desc', instance.desc)
        instance.image = validated_data.get('image', instance.image)
        instance.bonus = validated_data.get('bonus', instance.bonus)
        instance.location = validated_data.get('location', instance.location)
        instance.save()
        return instance


class GmSerializer(serializers.ModelSerializer):
    quests = QuestSerializer(many=True)
    locations = LocationSerializer(many=True)

    class Meta:
        model = Gm
        fields = ('locations', 'quests', 'name', 'id')

    def create(self, validated_data):
        """
        Create and return a new `Location` instance, given the validated data.
        """
        return Location.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Location` instance, given the validated data.
        """
        instance.locations = validated_data.get('locations', instance.locations)
        instance.quests = validated_data.get('quests', instance.quests)
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
