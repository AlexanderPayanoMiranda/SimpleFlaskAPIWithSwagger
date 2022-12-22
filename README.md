# Simple API with Flask and Swagger

**Important**, this API was made to show the workflow when using Flask and Swagger.
___
## To run the project, you need to execute the following steps:
1. Install dependencies with:
`pip install -r requirements.txt`
2. Set environment variables:
`SET FLASK_APP=app.py` for Windows or `EXPORT FLASK_APP=app.py` for a Linux based OS or macOS.
3. Run project with: `flask run`.
4. The routes available to test are:
   1. `http://127.0.0.1:5000/` - Index route that only shows the word "Index".
   2. `http://127.0.0.1:5000/basic_endpoint/test` - Route that shows the `__init__.py` of "basic_endpoints", shows the "test" route.
   3. `http://127.0.0.1:5000/basic_endpoint/entities` - Route that shows the `__init__.py` of "basic_endpoints", shows the "entities" route.
   4. `http://127.0.0.1:5000/basic_endpoint/entities/1` - Route that shows the `__init__.py` of "basic_endpoints", shows the "entities/id" route.
   5. `http://localhost:5000/jinja_template?top=cancel%20the%20REST%20API%20creation&bottom=I%20have%20to%20watch%20this%20bird` - Route that shows the `__init__.py` of "jinja_endpoints", shows the "" route.
   6. `http://localhost:5000/documented_api/doc` - Route that shows the `__init__.py` of "documented_endpoints", shows the "entities", "hello_world" and "jinja_template" route.
___
**Note**: This project only shows the simulation of an API and its documentation with Swagger.