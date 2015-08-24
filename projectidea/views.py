from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import Http404
from .models import Idea
#from .forms import IdeaForm
from .serializers import IdeaSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from ratelimit.mixins import RatelimitMixin
from rest_framework import permissions
from ideaproject.settings import consumer_key, consumer_secret, access_token, access_token_secret, text_api_id_key, text_api_secret
import tweepy
from aylienapiclient import textapi
from .forms import IdeaForm
from ratelimit.decorators import ratelimit
from .serializers import IdeaSerializer
from django.shortcuts import redirect

# Create your views here.
@ratelimit(key='ip', rate='10/m', block=True)
@login_required(login_url='/accounts/login')
def idea_list(request):
    ideas=get_list_or_404(Idea)[:5]
    return render(request, 'projectidea/idea_list.html', {'ideas': ideas})
@ratelimit(key='ip', rate='10/m', block=True)
@login_required(login_url='/idea/accounts/login')
def technology_list(request):
    tech_ideas=get_list_or_404(Idea, category='Technology')
    return render(request, 'projectidea/idea_list.html', {'ideas': tech_ideas})
@ratelimit(key='ip', rate='10/m', block=True)
@login_required(login_url='/idea/accounts/login')
def environment_list(request):
    tech_ideas=get_list_or_404(Idea, category='Environment')
    return render(request, 'projectidea/idea_list.html', {'ideas': tech_ideas})
@ratelimit(key='ip', rate='10/m', block=True)
@login_required(login_url='/idea/accounts/login')
def shopping_list(request):
    tech_ideas=get_list_or_404(Idea, category='Shopping')
    return render(request, 'projectidea/idea_list.html', {'ideas': tech_ideas})
@ratelimit(key='ip', rate='10/m', block=True)
@login_required(login_url='/idea/accounts/login')
def people_list(request):
    tech_ideas=get_list_or_404(Idea, category='People')
    return render(request, 'projectidea/idea_list.html', {'ideas': tech_ideas})
@ratelimit(key='ip', rate='10/m', block=True)
@login_required(login_url='/idea/accounts/login')
def financial_list(request):
    tech_ideas=get_list_or_404(Idea, category='Financial')
    return render(request, 'projectidea/idea_list.html', {'ideas': tech_ideas})
@ratelimit(key='ip', rate='10/m', block=True)
@login_required(login_url='/idea/accounts/login')
def writing_list(request):
    tech_ideas=get_list_or_404(Idea, category='Writing')
    return render(request, 'projectidea/idea_list.html', {'ideas': tech_ideas})
@ratelimit(key='ip', rate='10/m', block=True)
@login_required(login_url='/idea/accounts/login')
def idea_detail(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    return render(request, 'projectidea/idea_detail.html', {'idea': idea})
def idea_new(request):
    if request.method == "POST":
        form=IdeaForm(request.POST)
        if form.is_valid():
            serializer = IdeaSerializer(data=form.data)
            if serializer.is_valid():
                idea = IdeaSerializer.create(self=serializer, validated_data=serializer.data)
                serializer.save()
                idea.save()
            return redirect('projectidea.views.idea_detail', pk=idea.pk)
    else:
        form = IdeaForm()
        return render(request, 'projectidea/idea_edit.html', {'form': form})


@ratelimit(key='ip', rate='10/m', block=True)
@login_required(login_url='/idea/accounts/login')
def idea_edit(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    if request.method == "POST":
        form=IdeaForm(request.POST, instance=idea)
        if form.is_valid():
            serializer = IdeaSerializer(data=form.data)
            idea2 = IdeaSerializer.update(self=serializer, instance=idea)
            idea2.save()
            return redirect('projectidea.views.idea_detail', pk=idea.pk)
    else:
        form = IdeaForm(instance=idea)
        return render(request, 'projectidea/idea_edit.html', {'form': form})

@ratelimit(key='ip', rate='10/m', block=True)
@login_required(login_url='/idea/accounts/login')
def idea_remove(request, pk):
  idea = get_object_or_404(Idea, pk=pk)
  idea.delete()
  return idea_list(request)
class IdeasList(RatelimitMixin, generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    ratelimit_key = 'ip'
    ratelimit_rate = '25/m'
    ratelimit_block = True
    queryset = Idea.objects.all().order_by('created_at')
    serializer_class = IdeaSerializer

    # Class Views Api model

    #class IdeasList(APIView):
    # def get(self, request, format=None):
    #     if request.method == 'GET':
    #         ideas = Idea.objects.all().order_by('created_at')
    #         serializer = IdeaSerializer(ideas, many=True)
    #         return Response(serializer.data)
    # def post(self, request, format=None):
    #     serializer = IdeaSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)

    #API Decorator Model of Api Viewing
    #@api_view(['GET', 'POST', 'DELETE'])
    # def getIdeas(request, format=None):
    #     if request.method == 'GET':
    #         ideas = Idea.objects.all().order_by('created_at')
    #         serializer = IdeaSerializer(ideas, many=True)
    #         return Response(serializer.data)
    #     elif request.method == 'POST':
    #         serializer = IdeaSerializer(validated_data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data, status=status.HTTP_201_CREATED)
    #         return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)

class IdeaDetail(RatelimitMixin, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    ratelimit_key = 'ip'
    ratelimit_rate = '25/m'
    ratelimit_block = True
    queryset = Idea.objects.all().order_by('created_at')
    serializer_class = IdeaSerializer

    # Class Views Api model
    #class IdeaDetail(APIView):
    # def get_object(self, pk):
    #     try:
    #         return Idea.objects.get(pk=pk)
    #     except Idea.DoesNotExist:
    #         raise Http404
    # def get(self, request, pk, format=None):
    #     idea = self.get_object(pk)
    #     serializer = IdeaSerializer(idea)
    #     return Response(serializer.data)
    # def put(self, request, pk, format=None):
    #     idea = self.get_object(pk)
    #     serializer = IdeaSerializer(idea, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # def delete(self, request, pk, format=None):
    #     idea = self.get_object(pk)
    #     idea.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    #Decorator API VIEW
# @api_view(['GET', 'PUT', 'DELETE'])
# def idea_detail(request, pk, format=None):
#     try:
#         idea = Idea.objects.get(pk=pk)
#     except Idea.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = IdeaSerializer(idea)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = IdeaSerializer(idea, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         idea.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
