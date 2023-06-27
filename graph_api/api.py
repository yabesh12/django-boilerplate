import graphene


class Mutations(graphene.ObjectType):
    pass


class Queries(graphene.ObjectType):
    pass


schema = graphene.Schema(query=Queries, mutation=Mutations)
