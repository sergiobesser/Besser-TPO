from flask import Flask ,jsonify, request
from flask_cors import CORS
 
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
 
app=Flask(__name__)
CORS(app)
 
# configuro la base de datos, con el nombre el usuario y la clave
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost/cursosmysql'
#                                               user:clave@localhost/nombreBaseDatos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db= SQLAlchemy(app)
ma=Marshmallow(app)
 
# defino la tabla
class Curso(db.Model):   # la clase Producto hereda de db.Model     
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    nombre=db.Column(db.String(100))
    duracion=db.Column(db.String(100))
    nivel=db.Column(db.String(100))
    precio=db.Column(db.Integer)
 
    def __init__(self,nombre,duracion,nivel,precio):   #crea el  constructor de la clase
        self.nombre=nombre   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.duracion=duracion
        self.nivel=nivel
        self.precio=precio
db.create_all()  # crea las tablas
#  ************************************************************
class CursoSchema(ma.Schema):
    class Meta:
        fields=('id','nombre','duracion','nivel','precio')
 
curso_schema=CursoSchema()            # para crear un producto
cursos_schema=CursoSchema(many=True)  # multiples registros
 

@app.route('/cursos',methods=['GET'])
def get_Cursos():
    all_cursos=Curso.query.all()     # query.all() lo hereda de db.Model
    result=cursos_schema.dump(all_cursos)  # .dump() lo hereda de ma.schema
    return jsonify(result)
 
@app.route('/cursos/<id>',methods=['GET'])
def get_curso(id):
    curso=Curso.query.get(id)
    return curso_schema.jsonify(curso)

@app.route('/curso/<id>',methods=['DELETE'])
def delete_curso(id):
    curso=Curso.query.get(id)
    db.session.delete(curso)
    db.session.commit()
    return curso_schema.jsonify(curso)

@app.route('/cursos', methods=['POST']) # crea ruta o endpoint
def create_curso():
    print(request.json)  # request.json contiene el json que envio el cliente
    nombre=request.json['nombre']
    duracion=request.json['duracion']
    nivel=request.json['nivel']
    precio=request.json['precio']
    new_curso=Curso(nombre,duracion,nivel,precio)
    db.session.add(new_curso)
    db.session.commit()
    return curso_schema.jsonify(new_curso)

@app.route('/cursos/<id>' ,methods=['PUT'])
def update_curso(id):
    curso=Curso.query.get(id)
   
    nombre=request.json['nombre']
    duracion=request.json['duracion']
    nivel=request.json['nivel']
    precio=request.json['precio']
 
    curso.nombre=nombre
    curso.duracion=duracion
    curso.nivel=nivel
    curso.precio=precio
    db.session.commit()
    return curso_schema.jsonify(curso)

# programa principal
if __name__=='__main__':  
    app.run(debug=True, port=5000)