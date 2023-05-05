import graphene


class BookType(graphene.ObjectType):
    """
    A simple Book schema
    """

    id = graphene.String()
    title = graphene.String()
    subtitle = graphene.String()
    description = graphene.String()
    publisher = graphene.String()
    publication_date = graphene.String()
    categories = graphene.List(graphene.String)
    authors = graphene.List(graphene.String)
    image = graphene.String()
    source = graphene.String()

    def resolve_image(self, info):
        """Resolve image absolute path"""
        if self.image:
            self.image = info.context.build_absolute_uri(self.image.url)
        return self.image
