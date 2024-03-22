from .serializer import WatchlistSerializer,StreamPlatformSerializer,ReviewsSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
# from rest_framework import mixins
from rest_framework import generics

from rest_framework.views import APIView
from list.models import Watchlist,StreamPlatform,Reviews


class ReviewList(generics.ListCreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    permission_classes = [IsAuthenticated]

class ReviewdetailAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer





# class ReviewList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Reviews.objects.all()
#     serializer_class = ReviewsSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
class StreamPlatformAV(APIView):

    def get(self,request):
        stream=StreamPlatform.objects.all()
        serializer=StreamPlatformSerializer(stream,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
class StreamdetailAV(APIView):
    def get(self,request,pk):
        stream=StreamPlatform.objects.get(pk=pk)
        serializer=StreamPlatformSerializer(stream)
        return Response(serializer.data)
    def put(self,request,pk):
        serializer=StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.data)
    def delete(self,request,pk):

        stream=StreamPlatform.objects(pk=pk)
        stream.delete()
        return Response("deleted")
class WatchlistAV(APIView):
    def get(self,request):
        movie = Watchlist.objects.all()
        serializer=WatchlistSerializer(movie,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = WatchlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
class Moviedetail(APIView):
    def get(self,request,pk):
        movie = Watchlist.objects.get(pk=pk)
        serializer = WatchlistSerializer(movie)
        return Response(serializer.data)
    def put(self,request,pk):
        movie = Watchlist.objects.get(pk=pk)
        serializer=WatchlistSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def delete(self,request,pk):
        movie = Watchlist.objects.get(pk=pk)
        movie.delete()
        return Response("Deleted")








# @api_view(['GET','POST'])
# def list(request):
#     if request.method=="GET":
#         movie= Movies.objects.all()
#         serializer = MoviesSerializer(movie, many=True)
#         return Response(serializer.data)
#     if request.method =="POST":
#         serializer=MoviesSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
# @api_view(['GET','POST',"PUT","DELETE"])
# def details(request,pk):
#     if request.method == "GET":
#         movie= Movies.objects.get(pk=pk)
#         serializer= MoviesSerializer(movie)
#
#         return Response(serializer.data)
#     if request.method == "PUT":
#         movie=Movies.objects.get(pk=pk)
#         serializer=MoviesSerializer(movie,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#     if request.method == "DELETE":
#         movie = Movies.objects.get(pk=pk)
#         movie.delete()
#         return Response("Deleted")



