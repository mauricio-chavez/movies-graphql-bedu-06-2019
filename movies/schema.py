"""Movies app schema"""

import graphene
from graphene_django.types import DjangoObjectType

from .models import Director, Movie


class DirectorType(DjangoObjectType):
    """Director object"""
    class Meta:
        model = Director


class MovieType(DjangoObjectType):
    """Movie object"""
    class Meta:
        model = Movie


class MoviesQuery:
    """Movies app query"""
    movies = graphene.List(MovieType)
    movie = graphene.Field(
        type=MovieType,
        id=graphene.Int(required=True)
    )
    director_movies = graphene.List(
        of_type=MovieType,
        id=graphene.Int(required=True)
    )

    def resolve_movies(self, info):
        """Get all movies"""
        return Movie.objects.prefetch_related().all()

    def resolve_movie(self, info, id):
        """Get one movie"""
        queryset = Movie.objects.filter(id=id)
        if (queryset.exists()):
            return queryset.get()
        else:
            return None

    def resolve_director_movies(self, info, id):
        """Get all movies of a director"""
        return Director.objects.get(id=id).movie_set.all()


class MovieMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        year = graphene.Int(required=True)
        sinopsis = graphene.String(required=True)
        director = graphene.Int(required=True)

    movie = graphene.Field(MovieType)

    def mutate(self, info, title, year, sinopsis, director):
        movie = Movie.objects.create(
            title=title, year=year,
            sinopsis=sinopsis, director_id=director
        )
        return MovieMutation(movie=movie)


class MoviesMutation:
    create_movie = MovieMutation.Field()

