from flask import Flask, render_template, request, jsonify
import sqlite3


UPLOAD_FOLDER = './media'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
path = './media'
path2 = 'img'

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'clave'


@app.route('/')
def index():
  return render_template('index.html')

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
    #return redirect('/inicio')
  #else:
    #return render_template('ingresar.html')
    
    
@app.route('/agregarIndex', methods=["POST"])
def agregarIndex():
  if request.method == "POST":
    conn = sqlite3.connect("artemis.db")

    search_term = request.form["value"]
    search_term2 = request.files["value2"]

        
    q = f"""INSERT INTO Index(informacion, fotos) VALUES ('{search_term}', '{search_term2})"""
    conn.execute(q)
    conn.commit()
    conn.close()

  return(jsonify(True))

@app.route('/borrarIndex', methods=["DELETE"])
def borrarIndex():
  conn = sqlite3.connect('artemis.db')
  q = conn.execute(f"""SELECT * FROM Index""")
  mostrar = q.fetchall()
  print(mostrar)
  conn.close()
  lenght = len(mostrar)

  return render_template('', lenght=lenght, conn=mostrar)

@app.route('/agregarMuseo', methods=["POST"])
def agregarMuseo():
  if request.method == "POST":
    conn = sqlite3.connect("artemis.db")
    
    search_term = request.form["value"]
    search_term2 = request.form["value2"]
    search_term3 = request.form["value3"]
    search_term4 = request.form["value4"]
    search_term5 = request.form["value5"]
    search_term6 = request.form["value6"]
    search_term7 = request.form["value7"]
    search_term8 = request.form["value8"]
    search_term9 = request.files["value9"]
    
    q = f"""INSERT INTO Museo(nombreMuseo, informacio, coleccionActual, horario, precio, ubicacion, barrio, linkPagina, logo) VALUES ('{search_term}', '{search_term2}', '{search_term3}', '{search_term4}', '{search_term5}', '{search_term6}', '{search_term7}', '{search_term8}', '{search_term9}')"""
    conn.execute(q)
    conn.commit()
    conn.close()

  return(jsonify(True))


@app.route('/agregarPreguntas', methods=["GET","POST"])
def agregarPreguntas():
  if request.method == "POST":
    conn = sqlite3.connect("artemis.db")
      
    search_term = request.form["value"]
    search_term2 = request.form["value2"]
    search_term3 = request.form["value3"]
    search_term4 = request.form["value4"]
    search_term5 = request.form["value5"]
    search_term6 = request.form["value6"]
    search_term7 = request.form["value7"]
    search_term8 = request.form["value8"]
    search_term9 = request.form["value9"]
    search_term10 = request.form["value10"]
    q = f"""INSERT INTO FAQ(pregunta1, respuesta1, pregunta2, respuesta2, pregunta3, respuesta3, pregunta4, respuesta4, pregunta5, respuesta5) VALUES ('{search_term}', '{search_term2}','{search_term3}', '{search_term4}', '{search_term5}','{search_term6}',' {search_term7}','{search_term8}','{search_term9}', '{search_term10}')"""
    conn.execute(q)
    conn.commit()
    conn.close()

  
  return(jsonify(True))


@app.route(('/borrarPreguntas'), methods=["DELETE"])
def borrarPreguntas():
  SelectEliminar = request.form["value"]
  conn = sqlite3.connect("artemis.db")
      
  conne = sqlite3.connect('artemis.db')
  qq = conne.execute(f"""SELECT * FROM FAQ""")
  mostrar = qq.fetchall()
  conne.close()
  
  if SelectEliminar in mostrar[-1][0]:
    resu = (f"""INSERT INTO FAQ pregunta1 ='{SelectEliminar}'""")
  elif SelectEliminar in mostrar[-1][2]:
    resu = (f"""DELETE FROM FAQ WHERE pregunta2 ='{SelectEliminar}'""")
  elif SelectEliminar in mostrar[-1][4]:
    resu = (f"""DELETE FROM FAQ WHERE pregunta3 ='{SelectEliminar}'""")
  elif SelectEliminar in mostrar[-1][6]:
    resu = ( f"""DELETE FROM FAQ WHERE pregunta4 ='{SelectEliminar}'""")
  else :
   resu = (f"""DELETE FROM FAQ WHERE pregunta5 ='{SelectEliminar}'""")
    
  conn.commit()
  conn.close()

  return SelectEliminar
  
''' SelectEliminar = request.form["value"]
    conexion = sqlite3.connect('artemis.db')
    cursor = conexion.cursor()
    resu=cursor.execute(f"""SELECT * FROM FAQ""")

    usuario = cursor.fetchone()
  
    if SelectEliminar== '{pregunta1}':
      resu = (f"""DELETE FROM FAQ WHERE pregunta1 ='{SelectEliminar}'""")
    elif SelectEliminar== '{pregunta2}':
      resu = (f"""DELETE FROM FAQ WHERE pregunta2 ='{SelectEliminar}'""")
    elif SelectEliminar== '{pregunta3}':
      resu = (f"""DELETE FROM FAQ WHERE pregunta3 ='{SelectEliminar}'""")
    elif SelectEliminar== '{pregunta4}':
      resu = ( f"""DELETE FROM FAQ WHERE pregunta4 ='{SelectEliminar}'""")
    else :
     resu = (f"""DELETE FROM FAQ WHERE pregunta5 ='{SelectEliminar}'""")
     
    print(resu)
    cursor.execute(resu)
    cursor.commit()
    cursor.close()
    
'''
  
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
    

@app.route('/agregarInternacional', methods=["GET", "POST"])
def agregarInternacional():
  if request.method == "POST":
    conn = sqlite3.connect("artemis.db")

    search_term = request.form["value"]
    search_term2 = request.form["value2"]
    search_term3 = request.files["value3"]
    search_term4 = request.form["value4"]
    search_term5 = request.form["value5"]
    search_term6 = request.files["value6"]
    search_term7 = request.form["value7"]
    search_term8 = request.form["value8"]
    search_term9 = request.files["value9"]
    q = f"""INSERT INTO Internacionales(nombreCampo1, textoCampo1, fotoCampo1, nombreCampo2, textoCampo2, fotoCampo2, nombreCampo3, textoCampo3, fotoCampo3) VALUES ('{search_term}', '{search_term2}','{search_term3}', '{search_term4}', '{search_term5}','{search_term6}',' {search_term7}','{search_term8}','{search_term9}')"""
    conn.execute(q)
    conn.commit()
    conn.close()

  
  return(jsonify(True))

@app.route('/museos', methods=["GET", "POST"])
def museos():
    return render_template('museos.html')

@app.route('/novedades', methods=["GET", "POST"])
def novedades():
  return render_template('novedades.html')

@app.route('/administrador', methods=["GET", "POST", "PUT", "DELETE"])
def administrador():  
  conn = sqlite3.connect('artemis.db')
  q = conn.execute(f"""SELECT * FROM FAQ""")
  mostrar = q.fetchall()
  conn.close()
  lenght = len(mostrar[-1])
  return render_template('administrador.html', lenght = lenght, mostrar = mostrar)
  
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
                        respuestaDeLaBaseDeDatos = respuestaDeLaBaseDeDatos)
  

app.run(host='0.0.0.0', port=81)
