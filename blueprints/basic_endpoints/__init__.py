from flask import Blueprint, request

blueprint = Blueprint('api', __name__, url_prefix="/basic_endpoint")


@blueprint.route("/test")
def test():
    return {
        "message": "index"
    }


@blueprint.route("/entities", methods=["GET", "POST"])
def entities():
    if request.method == "GET":
        return {
            "message": "This endpoint should return a list of entities!",
            "method": request.method
        }
    if request.method == "POST":
        return {
            "message": "This endpoint should create an entity",
            "method": request.method,
            "body": request.json
        }


@blueprint.route("/entities/<int:entity_id>", methods=["GET", "PUT", "PATCH", "DELETE"])
def entity(entity_id):
    if request.method == "GET":
        return {
            "id": entity_id,
            "message": "This endpoint should return the entity {} details".format(entity_id),
            "method": request.method
        }
    if request.method == "PUT":
        return {
            "id": entity_id,
            "message": "This endpoint should put update the entity {} details".format(entity_id),
            "method": request.method
        }
    if request.method == "PATCH":
        return {
            "id": entity_id,
            "message": "This endpoint should patch update the entity {} details".format(entity_id),
            "method": request.method
        }
    if request.method == "DELETE":
        return {
            "id": entity_id,
            "message": "This endpoint should delete the entity {} details".format(entity_id),
            "method": request.method
        }
