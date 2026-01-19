# Import des modules Flask et Flask-RESTful
from flask import Flask
from flask_restful import Resource, Api

# Création de l'application Flask
app = Flask(__name__)
api = Api(app)

# Définition d'une ressource "Product"
class Product(Resource):
    def get(self):
        # Réponse JSON renvoyée par l'API
        return {
            'products': ['ipad pro 14', 'MacBook Pro', 'Ordinateur']
        }

# Association de la ressource à la route "/"
api.add_resource(Product, '/')

# Point d'entrée de l'application
if __name__ == '__main__':
    # host 0.0.0.0 = accessible depuis l'extérieur du conteneur
    # port 80 = port interne du conteneur
    app.run(host='0.0.0.0', port=80, debug=True)

