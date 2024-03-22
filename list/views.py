# from django.shortcuts import render
# from .models import Movies
# from django.http import JsonResponse,HttpResponse
# # Create your views here.
#
# def seen(request):
#     movies = Movies.objects.all()
#     data={
#         'mos': list(movies.values())
#     }
#     return JsonResponse(data)
# def details(request,pk):
#     movies=Movies.objects.get(pk=pk)
#     data={
#         'Name': movies.Name,
#         'Description':movies.Description
#     }
#     return JsonResponse(data)