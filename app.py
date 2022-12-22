from flask import Flask
from blueprints.basic_endpoints import blueprint as bp_basic_ep
from blueprints.jinja_endpoints import blueprint as bp_jinja_template_ep
from blueprints.documented_endpoints import blueprint as documented_endpoint

app = Flask(__name__)

app.config["RESTPLUS_MASK_SWAGGER"] = False

app.register_blueprint(bp_basic_ep)
app.register_blueprint(bp_jinja_template_ep)
app.register_blueprint(documented_endpoint)


@app.route("/")
def index():
    return "Index"


if __name__ == "__main__":
    app.run()
