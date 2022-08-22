from rest_framework import routers, serializers
from Main.models import Question,Answer,Comment
from .models import TESTModel 
class PublicUser(serializers.Serializer):
    pk =serializers.IntegerField(read_only=True) 
    username =serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)  
class QuestionSerilazer(serializers.ModelSerializer):
    author = PublicUser(read_only=True)

    class Meta:
        model = Question
        fields = [
            "pk",
            "author",
            "question_title",
            "description",
        ]

class testSerilazer(serializers.ModelSerializer):
    class Meta:
        model =TESTModel
        fields = [
            'title',
            'text'
        ]

class AnsSerializer(serializers.ModelSerializer):
    user =PublicUser(read_only=True)
    class Meta:
        model=Answer
        fields = [
            "user",
            "question",
            'Answer',
            "likes",
            "dislike"
        ]
class ComSerializer(serializers.ModelSerializer):
    user =PublicUser(read_only=True)
    class Meta:
        model = Comment
        fields = [
            "user",
            "link",
            "comment"
        ]