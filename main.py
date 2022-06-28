from ariadne.asgi import GraphQL
from ariadne_graphql_modules import make_executable_schema
from fastapi import FastAPI

from config import DEBUG
from gql.query import Query

schema = make_executable_schema(Query)

graphql = GraphQL(schema, debug=DEBUG)

app = FastAPI()
app.add_route("/", graphql)
app.add_websocket_route("/", graphql)
