import graphene
import graphql_jwt


from .book.schema import BookQueries, DeleteBook


class Query(BookQueries):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    node = graphene.Node.Field()


class Mutation(graphene.ObjectType):
    delete_book = DeleteBook.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
