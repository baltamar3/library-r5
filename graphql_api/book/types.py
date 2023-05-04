import graphene


class BookType(graphene.ObjectType):
    id = graphene.String()
    title = graphene.String()
    subtitle = graphene.String()
    description = graphene.String()
    publisher = graphene.String()
    publication_date = graphene.String()
    categories = graphene.List(graphene.String)
    authors = graphene.List(graphene.String)
    source = graphene.String()
