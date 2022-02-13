from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.serializers import MovieSerializer, ReviewSerializer
from movie_app.models import Director, Movie, Review


@api_view(['GET'])
def director_list_view(request):
    directors = Movie.objects.all()
    data = MovieSerializer(directors, many=True).data
    return Response(data=data)

@api_view(['GET'])
def director_detail_view(request, id):
    try:
        movie = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'massage': 'Page Not Found'})
    data = ReviewSerializer(movie).data
    return Response(data=data)
