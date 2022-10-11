from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')

@app.route('/inicio', methods=["GET", "POST"])
def inicio():
    return render_template('inicio.html')

@app.route('/Ingresar', methods=["GET", "POST"])
def cambioAIngresar():
    return render_template('ingresar.html')


@app.route('/ingresar', methods=["GET", "POST"])
def ingresar():
   #return render_template('ingresar.html')
  if request.method == "POST":
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
  else:
    return render_template('ingresar.html')
    
  return(jsonify(True))


@app.route('/guardarMuseo', methods=["POST"])
def guardarMuseo():
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
    
    q = f"""INSERT INTO Museo(nombreMuseo, informacio, coleccionActual, horario, precio, ubicacion, barrio, linkPagina, logo) VALUES ('{search_term}', '{search_term2}', '{search_term3}', '{search_term4}', '{search_term5}', '{search_term6}', '{search_term7}', '{search_term8}', '{search_term9}')"""
    conn.execute(q)
    conn.commit()
    conn.close()

  return(jsonify(True))


@app.route('/guardarPreguntas', methods=["GET","POST"])
def guardarPreguntas():
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

@app.route('/guardarInternacional', methods=["GET", "POST"])
def guardadInternacional():
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

@app.route('/internacional', methods=["GET", "POST"])
def internacional():
  return render_template('internacional.html')

@app.route('/faq', methods=["GET", "POST"])
def faq():
  return render_template('faq.html')
  
@app.route('/administrador', methods=["GET", "POST", "PUT", "DELETE"])
def administrador():  
  
  return render_template('administrador.html')
@app.route('faqAgregar',methods=["GET"])
def faqAgregar():
  


app.run(host='0.0.0.0', port=81)