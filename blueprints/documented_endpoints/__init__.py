from flask import Blueprint
from flask_restx import Api
from blueprints.documented_endpoints.hello_world import namespace as hello_world_ns
from blueprints.documented_endpoints.entities import namespace as entities_ns
from blueprints.documented_endpoints.jinja_template import namespace as jinja_template_ns

blueprint = Blueprint("documented_api", __name__, url_prefix="/documented_api")

api_extension = Api(
    blueprint,
    title="Flask RESTx Demo",
    version="1.0",
    description="Simple Application with Flask to demostrate Flask RESTx capabilities for better"
                " project structure and autogenerated docuementation",
    doc="/doc"
)

api_extension.add_namespace(hello_world_ns)
api_extension.add_namespace(entities_ns)
api_extension.add_namespace(jinja_template_ns)
