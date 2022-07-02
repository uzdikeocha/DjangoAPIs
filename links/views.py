from rest_framework import viewsets
from .models import links
from .serializers import linkserializers


class PostListApi(generics.ListAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer


class PostCreateApi(generics.CreateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostDetailApi(generic.RetrieveAPIView):
    queryset = Link.objects.filter(active=True) 
    serializer_class = LinkSerializer

class PostUpdateApi(generic.UpdateAPIView):
    queryset = Link.objects.filter(active=True) 
    serializer_class = LinkSerializer

class PostDeleteApi(generic.DestroyAPIView):
    queryset = Link.objects.filter(active=True) 
    serializer_class = LinkSerializer

