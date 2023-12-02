from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'

db = SQLAlchemy(app)
app.app_context().push()

api = Api(app)

from my_app.catalog.routes import catalog
app.register_blueprint(catalog)

# Add resources to the API
from my_app.catalog.resources import *

api.add_resource(CustomerTicketResource, '/customer_ticket')
api.add_resource(MenuResource, '/menu')
api.add_resource(WaiterResource, '/waiter')
api.add_resource(RevenueResource, '/calculate_cost')
api.add_resource(TotalRevenueResource, '/total_revenue')

db.create_all()
