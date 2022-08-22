from django.shortcuts import render
from rest_framework import generics,mixins
from rest_framework.response import Response
from rest_framework.authentication import *
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.decorators import api_view
from Main.models import Question, Answer,Comment
from .models import TESTModel 
from .serilizer import QuestionSerilazer,testSerilazer,AnsSerializer,ComSerializer
from django.http import Http404
from .permissions import IsAllowed,CreateIsAllowed,IsAllowedToDelete
# Create your views here.
class ListCreateAPIView(generics.ListCreateAPIView):
    queryset =Question.objects.all()
    serializer_class = QuestionSerilazer
    authentication_classes= [TokenAuthentication,SessionAuthentication]
    permission_classes= [CreateIsAllowed,IsAllowed]

    def perform_create(self,serializer):
        return serializer.save(author=self.request.user)
class detailAPIView(generics.RetrieveAPIView):
    queryset=Question.objects.all()
    serializer_class = QuestionSerilazer
    lookup_field = "pk"
class deleteAPIView(generics.GenericAPIView,mixins.DestroyModelMixin):
    queryset=Question.objects.all()
    serializer_class = QuestionSerilazer  
    authentication_classes = [SessionAuthentication,TokenAuthentication]
    permission_classes = [CreateIsAllowed]
    lookup_field = "pk"

    def delete(self, request, *args, **kwargs):
        obj = Question.objects.get(pk=kwargs.get('pk'))
        if request.user == obj.author:
            return self.destroy(request,args,kwargs)
        return Response({"err":"error not autherized"})
class updateAPIView(generics.GenericAPIView,mixins.UpdateModelMixin):
    queryset=Question.objects.all()
    serializer_class = QuestionSerilazer
    authentication_classes = [SessionAuthentication,TokenAuthentication]
    permission_classes = [CreateIsAllowed]
    lookup_field = "pk"

    def put(self, request, *args,**kwargs):
        obj = Question.objects.get(pk=kwargs.get('pk'))
        if request.user == obj.author:
            try:
                return self.update(request,*args,**kwargs)
            except:
                return self.partial_update(request,*args,**kwargs)
    def perform_update(self, serializer):
        question_title = serializer.data['question_title']
        if Question.objects.filter(question_title=question_title).exists():
            return Response({"err":"error"})
        serializer.save()
        return serializer.data
            
class AnsCreateListAPIView(generics.ListCreateAPIView):
    queryset =Answer.objects.all()
    serializer_class = AnsSerializer
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    permission_classes = [CreateIsAllowed]
    def get_queryset(self):
        ids =self.kwargs.get('slug')
        question =Question.objects.get(slug=ids)
        queryset = Answer.objects.filter(question=question)
        return queryset

    def perform_create(self,serializer,*args,**kwargs):
        if self.request.user.is_authenticated:
            id =self.kwargs.get('slug')
            question =Question.objects.filter(slug=id).first()
            return serializer.save(user=self.request.user,question=question)
        return Response({"err":"error"})
class AnsupdateAPIView(generics.GenericAPIView,mixins.UpdateModelMixin):
    queryset=Answer.objects.all()
    serializer_class = AnsSerializer
    authentication_classes = [SessionAuthentication,TokenAuthentication]
    permission_classes = [CreateIsAllowed]
    lookup_field = "pk"

    def put(self, request, *args,**kwargs):
        obj = Answer.objects.get(pk=kwargs.get('pk'))
        if request.user == obj.user:
            try:
                return self.update(request,*args,**kwargs)
            except:
                return self.partial_update(request,*args,**kwargs)
class AnsdeleteAPIView(generics.GenericAPIView,mixins.DestroyModelMixin):
    queryset=Answer.objects.all()
    serializer_class = AnsSerializer  
    authentication_classes = [SessionAuthentication,TokenAuthentication]
    permission_classes = [CreateIsAllowed]
    lookup_field = "pk"

    def delete(self, request, *args, **kwargs):
        obj = Answer.objects.get(pk=kwargs.get('pk'))
        if request.user == obj.user:
            return self.destroy(request,args,kwargs)
        return Response({"err":"error not autherized"})
class ComCreateListAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class=ComSerializer
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    permission_classes = [CreateIsAllowed]

    def get_queryset(self):
        ids = self.kwargs.get("pk")
        ans = Answer.objects.get(pk=ids)
        comment = Comment.objects.filter(link=ids)
        return comment

    def perform_create(self,serializer):
        ans = Answer.objects.get(pk=self.kwargs.get('pk'))
        return serializer.save(user=self.request.user,link=ans)

class ComupdateAPIView(generics.GenericAPIView,mixins.UpdateModelMixin):
    queryset=Comment.objects.all()
    serializer_class = ComSerializer
    authentication_classes = [SessionAuthentication,TokenAuthentication]
    permission_classes = [CreateIsAllowed]
    lookup_field = "pk"

    def put(self, request, *args,**kwargs):
        obj = Comment.objects.get(pk=kwargs.get('pk'))
        if request.user == obj.user:
            try:
                return self.update(request,*args,**kwargs)
            except:
                return self.partial_update(request,*args,**kwargs)
class ComdeleteAPIView(generics.GenericAPIView,mixins.DestroyModelMixin):
    queryset=Comment.objects.all()
    serializer_class = ComSerializer  
    authentication_classes = [SessionAuthentication,TokenAuthentication]
    permission_classes = [CreateIsAllowed]
    lookup_field = "pk"

    def delete(self, request, *args, **kwargs):
        obj = Comment.objects.get(pk=kwargs.get('pk'))
        if request.user == obj.user:
            return self.destroy(request,args,kwargs)
        return Response({"err":"error not autherized"})