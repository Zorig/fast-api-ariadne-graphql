from ariadne_graphql_modules import ObjectType, gql


class Query(ObjectType):
    __schema__ = gql(
        """
            type Query {
                me: String!
            }
        """
    )

    @staticmethod
    def resolve_me(*_):
        return "World"
