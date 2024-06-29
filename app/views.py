from flask import jsonify, request
from app.models import Producto

def index():
    response = {'message':'Hola mundo API FLASK 🐍'}
    return jsonify(response)

#funcion que busca todo el listado de las peliculas
def get_all_productos():
    productos = Producto.get_all()
    list_productos = [producto.serialize() for producto in productos]
    return jsonify(list_productos)

#funcion que busca una pelicula
def get_producto(producto_id):
    producto = Producto.get_by_id(producto_id)
    if not producto:
        return jsonify({'message': 'Producto not found'}), 404
    return jsonify(producto.serialize())

def create_producto():
    data = request.json
    #agregar una logica de validacion de datos
    new_producto = Producto(None,data['categoría'],data['nombre'],data['material'],data['descripción'],data['precio'],data['foto'])
    new_producto.save()
    return jsonify({'message':'Producto creado con exito'}), 201
    

def update_producto(producto_id):
    producto = Producto.get_by_id(producto_id)
    if not producto:
        return jsonify({'message': 'Producto not found'}), 404
    data = request.json
    producto.categoría = data['categoría']
    producto.nombre = data['nombre']
    producto.material = data['material']
    producto.descripción = data['descripción']
    producto.precio = data['precio']
    producto.foto = data['foto']
    producto.save()
    return jsonify({'message': 'Producto guardado exitosamte'})

def delete_producto(producto_id):
    producto = Producto.get_by_id(producto_id)
    if not producto:
        return jsonify({'message': 'Producto not found'}), 404
    producto.delete()
    return jsonify({'message': 'Producto deleted successfully'})