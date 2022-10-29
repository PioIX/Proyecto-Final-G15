from flask import Flask, render_template, request, jsonify, redirect
import sqlite3, os

from os.path import abspath, dirname, join
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './static/media'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
path = './static'
path2 = 'img'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
  conn = sqlite3.connect("artemis.db")
  resu=conn.execute(f"""SELECT * FROM CualquierCosa """)
  respuestaDelIndex= resu.fetchall()
  conn.close()
  largoImagen=len(respuestaDelIndex)
  return render_template('index.html',respuestaDelIndex = respuestaDelIndex, largoImagen=len(respuestaDelIndex))
  

@app.route('/museos2', methods=["GET", "POST"])
def museos2():
    return render_template('museos2.html')

@app.route('/inicio', methods=["GET", "POST"])
def inicio():
    return render_template('inicio.html')

@app.route('/ingresar', methods=["GET", "POST"])
def cambioAIngresar():
    return render_template('ingresar.html')
 
@app.route('/verificar', methods=["GET", "POST"])
def ingresar():

  conn = sqlite3.connect("artemis.db")
  usuario=request.form["value"]
  contra=request.form["value2"]
  resu=conn.execute(f"""SELECT * FROM Administrador WHERE usuario='{usuario}' and contraseña='{contra}'""")
 
  if resu.fetchone(): #Tengo usuario
      return(jsonify(True))
    #return redirect('/administrador')
  else:
      return(jsonify(False))
       
@app.route('/agregarIndex', methods=["POST"])
def agregarIndex():
  if request.method == "POST":
    conn = sqlite3.connect("artemis.db")

    search_term = request.form["informacion"]
    file = request.files["fotos"]
   
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)
    print(file_path)
   
    
    q = f"""SELECT * FROM Index"""
    q = """
        CREATE TABLE IF NOT EXISTS CualquierCosa (
    informacion varchar(255),
    fotos varchar(255)
    );
    """
    q = f"""INSERT INTO CualquierCosa(informacion, fotos) VALUES ('{search_term}', '{filename}')"""
    print(q)
    res = conn.execute(q)
    conn.commit()
    conn.close()
   
    return(redirect('/administrador'))
  else:
    return(redirect('/administrador'))

@app.route('/borrarIndex', methods=["DELETE"])
def borrarIndexImagen():
  SelectEliminarIndexImagen = request.form["value"]
  conn = sqlite3.connect("artemis.db")
  resu = (f"""DELETE FROM CualquierCosa WHERE fotos= '{SelectEliminarIndexImagen}'""")  
  print(resu)
  conn.execute(resu)
  conn.commit()
  conn.close()
  return SelectEliminarIndexImagen
 
  
@app.route('/agregarMuseo', methods=["POST"])
def agregarMuseo():
  if request.method == "POST":
    conn = sqlite3.connect("artemis.db")
    search_term = request.form["titulo"]
    search_term2 = request.form["informacion"]
    search_term3 = request.form["coleccion"]
    search_term4 = request.form["horario"]
    search_term5 = request.form["precios"]
    search_term6 = request.form["ubicacion"]
    search_term7 = request.form["barrio"]
    search_term8 = request.form["linkPagina"]
    file = request.files["logo"]

    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)
    print(file_path)
    
    q = f"""SELECT * FROM Museo"""
    
    q = f"""INSERT INTO Museo(nombreMuseo, informacio, coleccionActual, horario, precio, ubicacion, barrio, linkPagina, logo) VALUES ('{search_term}', '{search_term2}', '{search_term3}', '{search_term4}', '{search_term5}', '{search_term6}', '{search_term7}', '{search_term8}', '{filename}')"""
    conn.execute(q)
    conn.commit()
    conn.close()
    print(q)
    res = conn.execute(q)
    conn.commit()
    conn.close()
   
    return(redirect('/administrador'))
  else:
    return(redirect('/administrador'))

 
@app.route('/borrarMuseos', methods=['DELETE'])
def borrarMuseoos():  
  SelectEliminarM = request.form["value"]
  conn = sqlite3.connect("artemis.db")
  resu = (f"""DELETE FROM Museo WHERE nombreMuseo= '{SelectEliminarM}'""")  
  conn.execute(resu)
  conn.commit()
  conn.close()
  return SelectEliminarM

@app.route('/agregarPreguntas', methods=["GET","POST"])
def agregarPreguntas():
  if request.method == "POST":
    conn = sqlite3.connect("artemis.db")
    search_term = request.form["value"]
    search_term2 = request.form["value2"]
   
    q = f"""INSERT INTO FAQ(pregunta, respuesta ) VALUES ('{search_term}', '{search_term2}')"""
    conn.execute(q)
    conn.commit()
    conn.close()

  return(jsonify(True))

@app.route(('/borrarPreguntas'), methods=["DELETE"])
def borrarPreguntas():
  SelectEliminar = request.form["value"]
  conn = sqlite3.connect("artemis.db")
  resu = (f"""DELETE FROM FAQ WHERE id= '{SelectEliminar}'""")  
  conn.execute(resu)
  conn.commit()
  conn.close()
  return SelectEliminar
 
@app.route('/agregarNovedades', methods=['GET', 'POST'])
def agregarNovedades():
  if request.method=="POST":
    conn=sqlite3.connect('artemis.db')
   
    search_term = request.files["value"]
    search_term2 = request.form["value2"]
    search_term3 = request.files["value3"]
    search_term4 = request.form["value4"]
    search_term5 = request.files["value5"]
    search_term6 = request.form["value6"]
    search_term7 = request.files["value7"]
    search_term8 = request.form["value8"]
   
    q = f"""INSERT INTO Novedades(foto1, texto1, foto2, texto2, foto3, texto3, foto4, link4) VALUES ('{search_term}', '{search_term2}','{search_term3}', '{search_term4}', '{search_term5}','{search_term6}',' {search_term7}','{search_term8}')"""
    conn.execute(q)
    conn.commit()
    conn.close()

  return(jsonify(True))
   
@app.route('/agregarInternacional', methods=["POST"])
def agregarInternacional():
  if request.method == "POST":
    conn = sqlite3.connect("artemis.db")

    search_term = request.form["campo1"]
    search_term2 = request.form["textocampo1"]
    file = request.files["fotoCampo1"]
    search_term4 = request.form["campo2"]
    search_term5 = request.form["textocampo2"]
    file2 = request.files["fotoCampo2"]
    search_term7 = request.form["campo3"]
    search_term8 = request.form["textocampo3"]
    file3 = request.files["fotoCampo3"]
    
    filename = secure_filename(file.filename)
    filename2 = secure_filename(file2.filename)
    filename3 = secure_filename(file3.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename, filename2, filename3)
    file.save(file_path)
    print(file_path)
    q = f"""SELECT * FROM Internacionales"""
    q = """
        CREATE TABLE IF NOT EXISTS internacional2 (
    nombreCampo1 varchar(255),
    textoCampo1 varchar(255),
    fotoCampo1 varchar(255),
    nombreCampo2 varchar(255),
    textoCampo2 varchar(255),
    fotoCampo2 varchar(255),
    nombreCampo3 varchar(255),
    textoCampo3 varchar(255),
    fotoCampo3 varchar(255),
    
    );
    """
    q = f"""INSERT INTO internacional2((nombreCampo1, textoCampo1, fotoCampo1, nombreCampo2, textoCampo2,fotoCampo2, nombreCampo3, textoCampo3, fotoCampo3) VALUES ('{search_term}','{search_term2}' ,'{filename}', '{search_term4}', '{search_term5}','{filename2}',' {search_term7}','{search_term8}','{filename3}')"""
    print(q)
    res = conn.execute(q)
    conn.commit()
    conn.close()
  
    return(redirect('/administrador'))
  else:
    return(redirect('/administrador'))

@app.route('/museos', methods=["GET", "POST"])
def museos():
  conn = sqlite3.connect("artemis.db")
  resu=conn.execute(f"""SELECT * FROM Museo """)
  respuestaMuseos= resu.fetchall()
     #pedido a la base

    #me traigo datos
  conn.close()  
  return render_template('museos.html',
                        respuestaMuseos=respuestaMuseos,             lenght=len(respuestaMuseos))
   

@app.route('/novedades', methods=["GET", "POST"])
def novedades():
  return render_template('novedades.html')

@app.route('/administrador', methods=["GET", "POST", "PUT", "DELETE"])
def administrador():  
  conn = sqlite3.connect('artemis.db')
  q = conn.execute(f"""SELECT * FROM FAQ""")
  r = conn.execute(f"""SELECT * FROM Museo""")
  i= conn.execute(f"""SELECT * FROM CualquierCosa""")
  mostrarM= r.fetchall()
  mostrar = q.fetchall()
  mostrarI= i.fetchall()
  conn.close()
  lenghtI=len(mostrarI)
  lenghtM=len(mostrarM)
  lenght = len(mostrar)
  return render_template('administrador.html', lenght = lenght, mostrar = mostrar, lenghtM=lenghtM, lenghtI=lenghtI, mostrarI=mostrarI)
 
@app.route('/internacional', methods=["GET", "POST"])
def internacional():
  return render_template('internacional.html')

@app.route('/faq', methods=["GET", "POST"])
def faq():
  conn = sqlite3.connect("artemis.db")
  resu=conn.execute(f"""SELECT * FROM FAQ """)
  respuestaDeLaBaseDeDatos= resu.fetchall()
     #pedido a la base

    #me traigo datos
  conn.close()  
  return render_template('faq.html',
                        respuestaDeLaBaseDeDatos = respuestaDeLaBaseDeDatos, lenght = len(respuestaDeLaBaseDeDatos))
 

app.run(host='0.0.0.0', port=81)
