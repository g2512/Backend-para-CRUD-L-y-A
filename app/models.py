from app.database import get_db

class Producto:
    #CONSTRUCTOR
    def __init__(self,id_producto=None,categoría=None,nombre=None,material=None,descripción=None,precio=None,foto=None):
        self.id_producto = id_producto
        self.categoría = categoría
        self.nombre = nombre
        self.material = material
        self.descripción= descripción
        self.precio=precio
        self.foto= foto
    @staticmethod
    def get_by_id(producto_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM productos WHERE idproductos_lya = %s", (producto_id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Producto(id_producto=row[0], categoría=row[1], nombre=row[2], material=row[3], descripción=row[4],precio=row[5],foto=row[6])
        return None
    @staticmethod    
    def get_all():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM productos")
        rows = cursor.fetchall()
        # movies = []
        productos = [Producto(id_producto=row[0], categoría=row[1], nombre=row[2], material=row[3], descripción=row[4],precio=row[5],foto=row[6]) for row in rows]
        # for row in rows:
        #     new_movie =  Movie(row[0],row[1],row[2],row[3],row[4])
        #     movies.append(new_movie)
        cursor.close()
        return productos

    def save(self):
        #logica para INSERT/UPDATE en base datos
        db = get_db()
        cursor = db.cursor()
        if self.id_producto:
            query = """
                UPDATE productos SET categoría = %s, nombre = %s, material = %s, descripción = %s,precio = %s, foto = %s,
                WHERE id_producto = %i
            """, (self.categoría, self.nombre, self.material, self.descripción,self.precio, self.foto, self.id_producto)
            cursor.execute(query)
        else:
            cursor.execute("""
                INSERT INTO productos (categoría, nombre, material, descripción,precio,foto) VALUES (%s, %s, %s, %s,%s,%s)
            """, (self.categoría, self.nombre, self.material, self.descripción,self.precio,self.foto))
            self.id_producto = cursor.lastrowid
        db.commit()
        cursor.close()

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM productos WHERE idproductos_lya = %s", (self.id_producto,))
        db.commit()
        cursor.close()   


    def serialize(self):
        return {
           'id_producto': self.id_producto,
           'categoría': self.categoría,
           'nombre': self.nombre,
           'material': self.material,
           'descripción': self.descripción,
           'precio': self.precio,
           'foto': self.foto,
                }
    
    