from flask import Flask
from app.database import init_app
from app.views import *
from flask_cors import CORS

#Crear una instancia de Flask
app = Flask(__name__)

init_app(app)
#permitir solicitudes desde cualquier origin
CORS(app)


#asociacion de rutas con vistas
app.route('/',methods=['GET'])(index)
app.route('/api/productos/',methods=['GET'])(get_all_productos)
app.route('/api/productos/',methods=['POST'])(create_producto)
app.route('/api/productos/<int:producto_id>', methods=['GET'])(get_producto)
app.route('/api/productos/<int:producto_id>', methods=['PUT'])(update_producto)
app.route('/api/productos/<int:producto_id>', methods=['DELETE'])(delete_producto)




#Permite separa el codigo que se ejecuta cuando se corre el archivo
if __name__=='__main__':
    app.run(debug=True)