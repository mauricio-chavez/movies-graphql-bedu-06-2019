"""Project schema"""

import graphene

from movies.schema import MoviesQuery, MoviesMutation


class Query(graphene.ObjectType, MoviesQuery):
    """Query root object"""
    hello = graphene.String(required=True)

    def resolve_hello(self, info):
        """Hello resolver"""
        return 'Hello, query'


class Mutation(graphene.ObjectType, MoviesMutation):
    """Mutation root object"""
    hello = graphene.String(required=True)

    def resolve_hello(self, info):
        """Hello resolver"""
        return 'Hello, mutation'


schema = graphene.Schema(query=Query, mutation=Mutation)
