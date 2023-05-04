import graphene


from .book.schema import BookQueries


class Query(BookQueries):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    node = graphene.Node.Field()


schema = graphene.Schema(query=Query)
