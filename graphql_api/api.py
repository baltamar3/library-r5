import graphene
import graphql_jwt


from .book.schema import BookQueries, CreateBook, DeleteBook


class Query(BookQueries):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    node = graphene.Node.Field()


class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()
    delete_book = DeleteBook.Field()
    # Auth mutations
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
