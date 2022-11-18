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


def crear_base():
  conn = sqlite3.connect("artemis.db")
#  q = "DROP TABLE if exists NOVEDADES;"
#  conn.execute(q)
  q = """create TABLE if not exists NOVEDADES(
      foto1 TEXT,
      texto1 TEXT,
      foto2 TEXT,
      texto2 TEXT,
      foto3 TEXT,
      texto3 TEXT,
      foto4 TEXT,
      link TEXT
      );"""
  conn.execute(q)
crear_base()

@app.route('/')
def index():
  conn = sqlite3.connect("artemis.db")
  resu = conn.execute(f"""SELECT * FROM CualquierCosa1 """)
  respuestaDelIndex = resu.fetchall()
  conn.close()
  largoImagen = len(respuestaDelIndex)
  return render_template('index.html',
                         respuestaDelIndex=respuestaDelIndex,
                         largoImagen=len(respuestaDelIndex))

@app.route('/inicio', methods=["GET", "POST"])
def inicio():
  conn = sqlite3.connect("artemis.db")
  p = conn.execute(f"""SELECT * FROM Inicial""")
  respuestaInicial = p.fetchall()
  conn.close()
  lenghtR=len(respuestaInicial)  
  
  return render_template('inicio.html',
                         respuestaInicial=respuestaInicial,
                         lenghtR=lenghtR)


@app.route('/ingresar', methods=["GET", "POST"])
def cambioAIngresar():
  return render_template('ingresar.html')


@app.route('/verificar', methods=["GET", "POST"])
def ingresar():

  conn = sqlite3.connect("artemis.db")
  usuario = request.form["value"]
  contra = request.form["value2"]
  resu = conn.execute(
    f"""SELECT * FROM Administrador WHERE usuario='{usuario}' and contraseña='{contra}'"""
  )

  if resu.fetchone():  #Tengo usuario
    return (jsonify(True))
  #return redirect('/administrador')
  else:
    return (jsonify(False))


@app.route('/agregarIndex', methods=["POST"])
def agregarIndex():
  if request.method == "POST":
    conn = sqlite3.connect("artemis.db")

    search_term = request.form["informacion"]
    file1 = request.files["foto1"]
    file2 = request.files["foto2"]
    file3 = request.files["foto3"]
    file4 = request.files["foto4"]

    filename1 = secure_filename(file1.filename)
    file_path1 = os.path.join(app.config['UPLOAD_FOLDER'], filename1)
    file1.save(file_path1)
    print(file_path1)
    filename2 = secure_filename(file2.filename)
    file_path2 = os.path.join(app.config['UPLOAD_FOLDER'], filename2)
    file2.save(file_path2)
    print(file_path2)
    filename3 = secure_filename(file3.filename)
    file_path3 = os.path.join(app.config['UPLOAD_FOLDER'], filename3)
    file3.save(file_path3)
    print(file_path3)
    filename4 = secure_filename(file4.filename)
    file_path4 = os.path.join(app.config['UPLOAD_FOLDER'], filename4)
    file4.save(file_path4)
    print(file_path4)

    q = f"""SELECT * FROM Index"""
    q = """
        CREATE TABLE IF NOT EXISTS CualquierCosa1 (
    informacion varchar(255),
    foto1 varchar(255),
    foto2 varchar(255),
    foto3 varchar(255),
    foto4 varchar(255)
    );
    """
    
    
    q = f"""INSERT INTO CualquierCosa1(informacion, foto1, foto2, foto3,foto4) VALUES ('{search_term}', '{filename1}', '{filename2}', '{filename3}', '{filename4}')"""
    print(q)
    res = conn.execute(q)
    conn.commit()
    conn.close()

    return (redirect('/administrador'))
  else:
    return (redirect('/administrador'))

@app.route('/borrarIndex', methods=["DELETE"])
def borrarIndexImagen():
  SelectEliminarIndexImagen = request.form["value"]
  conn = sqlite3.connect("artemis.db")
  resu = (
    f"""DELETE FROM CualquierCosa1 WHERE foto1= '{SelectEliminarIndexImagen}'"""
  )
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
    search_term4 = request.form["hora"]
    search_term5 = request.form["precio"]
    search_term6 = request.form["ubicacion"]
    search_term7 = request.form["barrio"]
    search_term8 = request.form["linkPagina"]
    file1 = request.files["logo"]
    file2= request.files["fotoMuseo"]
    
    filename1 = secure_filename(file1.filename)
    filename2 = secure_filename(file2.filename)

    file_path1 = os.path.join(app.config['UPLOAD_FOLDER'], filename1)
    file1.save(file_path1)
    file_path2 = os.path.join(app.config['UPLOAD_FOLDER'], filename2)
    file2.save(file_path2)

    q = f"""SELECT * FROM Museo"""
    q = f"""INSERT INTO Museo(nombreMuseo,informacio, coleccionActual, horario, precio, ubicacion, barrio, linkPagina, logo, imagen) VALUES ('{search_term}', '{search_term2}','{search_term3}','{search_term4}','{search_term5}','{search_term6}','{search_term7}','{search_term8}','{filename1}','{filename2}')"""
    print(q)
    conn.execute(q)
    conn.commit()
    conn.close()
    return (redirect('/administrador'))
  else:
    return (redirect('/'))

@app.route('/borrarMuseos', methods=['DELETE'])
def borrarMuseos():
  SelectEliminarMuseos = request.form["value"]
  conn = sqlite3.connect("artemis.db")
  resu = (f"""DELETE FROM Museo WHERE nombreMuseo= '{SelectEliminarMuseos}'""")
  conn.execute(resu)
  conn.commit()
  conn.close()
  return SelectEliminarMuseos


@app.route('/agregarPreguntas', methods=["GET", "POST"])
def agregarPreguntas():
  if request.method == "POST":
    conn = sqlite3.connect("artemis.db")
    search_term = request.form["value"]
    search_term2 = request.form["value2"]

    q = f"""INSERT INTO FAQ(pregunta, respuesta ) VALUES ('{search_term}', '{search_term2}')"""
    conn.execute(q)
    conn.commit()
    conn.close()

  return (jsonify(True))

@app.route(('/borrarPreguntas'), methods=["DELETE"])
def borrarPreguntas():
  SelectEliminar = request.form["value"]
  conn = sqlite3.connect("artemis.db")
  resu = (f"""DELETE FROM FAQ WHERE id= '{SelectEliminar}'""")
  conn.execute(resu)
  conn.commit()
  conn.close()
  return SelectEliminar
  
@app.route('/agregarInicio', methods=['POST'])
def agregarInicio():
  if request.method=="POST":
    conn=sqlite3.connect("artemis.db")
    file1=request.files["imagen1"]
    file2=request.files["imagen2"]
    file3=request.files["imagen3"]
    file4=request.files["imagen4"]
    file5=request.files["thinklink"]
    search_term=request.form["texto"]
    search_term2=request.form["linkInicio"]
    
    filename1 = secure_filename(file1.filename)
    filename2 = secure_filename(file2.filename)
    filename3 = secure_filename(file3.filename)
    filename4 = secure_filename(file4.filename)
    filename5 = secure_filename(file5.filename)
    file_path1 = os.path.join(app.config['UPLOAD_FOLDER'], filename1)
    file1.save(file_path1)
    file_path2 = os.path.join(app.config['UPLOAD_FOLDER'], filename2)
    file2.save(file_path2)
    file_path3 = os.path.join(app.config['UPLOAD_FOLDER'], filename3)
    file3.save(file_path3)
    file_path4 = os.path.join(app.config['UPLOAD_FOLDER'], filename4)
    file4.save(file_path4)
    file_path5 = os.path.join(app.config['UPLOAD_FOLDER'], filename5)
    file5.save(file_path5)

    e = f"""SELECT * FROM Inicial"""
    q = """
        CREATE TABLE IF NOT EXISTS Inicial (
    imagen1 varchar(255),
    imagen2 varchar(255),
    imagen3 varchar(255),
    imagen4 varchar(255),
    thinklink varchar(255),
    texto varchar(255),
    linkInicio varchar(255)
    );
    """
    conn.execute(q)
    conn.commit()
    conn.close()
    conn2=sqlite3.connect("artemis.db")
    q2 = f"""INSERT INTO Inicial(imagen1, imagen2, imagen3, imagen4, thinklink , texto, linkInicio) VALUES ('{filename1}', '{filename2}','{filename3}','{filename4}','{filename5}','{search_term}','{search_term2}')"""
    conn2.execute(q2)
    conn2.commit()
    conn2.close()
    return (redirect('/administrador'))
  else:
    return (redirect('/'))
    
    
@app.route('/borrarInicial', methods=["DELETE"])
def borrarInicial():
  SelectEliminarInicial = request.form["value"]
  conn = sqlite3.connect("artemis.db")
  resu = (f"""DELETE FROM Inicial WHERE imagen1= '{SelectEliminarInicial}'""")
  conn.execute(resu)
  conn.commit()
  conn.close()
  return SelectEliminarInicial
  
@app.route('/agregarNovedades', methods=['GET', 'POST'])
def agregarNovedades():
  if request.method == "POST":
    conn = sqlite3.connect('artemis.db')
    file1 = request.files["foto1"]
    search_term1 = request.form["texto1"]
    file2 = request.files["foto2"]
    search_term2 = request.form["texto2"]
    file3 = request.files["foto3"]
    search_term3 = request.form["texto3"]
    file4 = request.files["foto4"]
    search_term4 = request.form["link"]

    filename1 = secure_filename(file1.filename)
    file_path1 = os.path.join(app.config['UPLOAD_FOLDER'], filename1)
    file1.save(file_path1)
    filename2 = secure_filename(file2.filename)
    file_path2 = os.path.join(app.config['UPLOAD_FOLDER'], filename2)
    file2.save(file_path2)
    filename3 = secure_filename(file3.filename)
    file_path3 = os.path.join(app.config['UPLOAD_FOLDER'], filename3)
    file3.save(file_path3)
    filename4 = secure_filename(file4.filename)
    file_path4 = os.path.join(app.config['UPLOAD_FOLDER'], filename4)
    file4.save(file_path4)
    
    q = f"""INSERT INTO NOVEDADES(foto1, texto1, foto2, texto2, foto3, texto3, foto4, link) VALUES ('{filename1}', '{search_term1}', '{filename2}', '{search_term2}', '{filename3}', '{search_term3}', '{filename4}', '{search_term4}')"""
    print(q)
    conn.execute(q)
    conn.commit()
    conn.close()
  return (redirect('/administrador'))

@app.route('/borrarNovedades', methods=["DELETE"])
def borrarNovedades():
  SelectEliminarNovedades = request.form["value"]
  print(SelectEliminarNovedades)
  conn = sqlite3.connect("artemis.db")
  resu = (f"""DELETE FROM NOVEDADES WHERE foto1=  '{SelectEliminarNovedades}'""")
  conn.execute(resu)
  conn.commit()
  conn.close()
  return SelectEliminarNovedades

@app.route('/agregarInternacional', methods=["POST"])
def agregarInternacional():
  if request.method == "POST":
    conn = sqlite3.connect("artemis.db")

    search_term = request.form["campo1"]
    search_term2 = request.form["textocampo1"]

    file1 = request.files["fotoCampo1"]
    search_term4 = request.form["campo2"]
    search_term5 = request.form["textocampo2"]
    file2 = request.files["fotoCampo2"]
    search_term7 = request.form["campo3"]
    search_term8 = request.form["textocampodos"]
    file3 = request.files["fotoCampo3"]

    filename1 = secure_filename(file1.filename)
    filename2 = secure_filename(file2.filename)
    filename3 = secure_filename(file3.filename)

    file_path1 = os.path.join(app.config['UPLOAD_FOLDER'], filename1)
    file1.save(file_path1)
    file_path2 = os.path.join(app.config['UPLOAD_FOLDER'], filename2)
    file2.save(file_path2)
    file_path3 = os.path.join(app.config['UPLOAD_FOLDER'], filename3)
    file3.save(file_path3)

    q = f"""INSERT INTO Internacionales(nombreCampo1, textoCampo1, fotoCampo1, nombreCampo2, textoCampo2,fotoCampo2, nombreCampo3, textoCampo3, fotoCampo3) VALUES ('{search_term}','{search_term2}' ,'{filename1}', '{search_term4}', '{search_term5}','{filename2}',' {search_term7}','{search_term8}','{filename3}')"""
    print(q)
    conn.execute(q)
    conn.commit()
    conn.close()
    return (redirect('/administrador'))
  else:
    return (redirect('/'))

@app.route('/borrarInternacional', methods=['DELETE'])
def borrarInternacional():
  SelectEliminarInternacional = request.form["value"]
  conn = sqlite3.connect("artemis.db")
  resu = (
    f"""DELETE FROM Internacionales WHERE nombreCampo1= '{SelectEliminarInternacional}'"""
  )
  conn.execute(resu)
  conn.commit()
  conn.close()
  return SelectEliminarInternacional
  
  
@app.route('/administrador', methods=["GET", "POST", "PUT", "DELETE"])
def administrador():
  conn = sqlite3.connect('artemis.db')
  q = conn.execute(f"""SELECT * FROM FAQ""")
  r = conn.execute(f"""SELECT * FROM Museo""")
  i = conn.execute(f"""SELECT * FROM CualquierCosa1""")
  n = conn.execute(f"""SELECT * FROM NOVEDADES""")
  z = conn.execute(f"""SELECT * FROM Internacionales""")
  x=conn.execute(f"""SELECT * FROM Inicial""")
  mostrarZ = z.fetchall()
  mostrarM = r.fetchall()
  mostrar = q.fetchall()
  mostrarI = i.fetchall()
  mostrarN = n.fetchall()
  mostrarX= x.fetchall()
  
  conn.close()

  lenghtZ = len(mostrarZ)
  lenghtX= len(mostrarX)
  lenghtI = len(mostrarI)
  lenghtM = len(mostrarM)
  lenght = len(mostrar)
  lenghtN = len(mostrarN)
  
  #print(mostrarN)

  #if len(mostrarN) == 0:
   # mostrarN = ['foto1', 'texto1', 'foto2', 'texto2', 'foto3', 'texto3', 'foto4', 'link']
  #else:
    #mostrarN = mostrarN[0]

  return render_template('administrador.html',
                         lenght=lenght,
                         mostrar=mostrar,
                         lenghtI=lenghtI,
                         mostrarI=mostrarI,
                         lenghtM=lenghtM,
                         mostrarM=mostrarM,
                         mostrarN=mostrarN,
                         lenghtN=lenghtN,
                         lenghtZ=lenghtZ,
                         mostrarZ=mostrarZ,
                         mostrarX=mostrarX,
                         lenghtX=lenghtX
                        );

@app.route('/internacional', methods=["GET", "POST"])
def internacional():
  conn = sqlite3.connect("artemis.db")
  p = conn.execute(f"""SELECT * FROM Internacionales""")

  respuestaInternacional = p.fetchall()
  lenghtR=len(respuestaInternacional)
  conn.close()
  return render_template('internacional.html',
                         respuestaInternacional=respuestaInternacional, lenghtR=lenghtR)

@app.route('/museos2/<nombre>', methods=["GET", "POST"])
def museos2(nombre):
  if request.method == "POST": #Aca podria leer el museo
    print(request.form["museo"])
    conn=sqlite3.connect("artemis.db")
    m= conn.execute(f"""SELECT * FROM Museo WHERE nombreMuseo ='{nombre}'""")
    respuestaMuseos2=m.fetchall()
    lenghtM=len(respuestaMuseos2)
    conn.close()
    
    return render_template('museos2.html', respuestaMuseos2=respuestaMuseos2[0], lenghtM=lenghtM)
  
  else:
    conn=sqlite3.connect("artemis.db")
    m= conn.execute(f"""SELECT * FROM Museo""")
    respuestaMuseos2=m.fetchall()
    lenghtM=len(respuestaMuseos2)
    conn.close()
    
    return render_template('museos2.html', respuestaMuseos2=respuestaMuseos2, lenghtM=lenghtM)
  
@app.route('/faq', methods=["GET", "POST"])
def faq():
  conn = sqlite3.connect("artemis.db")
  resu = conn.execute(f"""SELECT * FROM FAQ """)
  respuestaDeLaBaseDeDatos = resu.fetchall()
  #pedido a la base

  #me traigo datos
  conn.close()
  return render_template('faq.html',
                         respuestaDeLaBaseDeDatos=respuestaDeLaBaseDeDatos,
                         lenght=len(respuestaDeLaBaseDeDatos))

@app.route('/museos', methods=["GET", "POST"])
def museos():
  conn = sqlite3.connect("artemis.db")
  p = conn.execute(f"""SELECT * FROM Museo """)
  respuestaMuseos = p.fetchall()
  LENGHTM = len(respuestaMuseos)
  #pedido a la base
  #me traigo datos
  conn.close()
  return render_template('museos.html',
                         respuestaMuseos=respuestaMuseos,
                         LENGHTM=LENGHTM)

@app.route('/novedades', methods=["GET", "POST"])
def novedades():
  conn = sqlite3.connect("artemis.db")
  w = conn.execute(f"""SELECT * FROM Novedades""")
  respuestaNovedades = w.fetchall()
  lenghtN =len(respuestaNovedades)
  conn.close()
  return render_template('novedades.html',
                         respuestaNovedades=respuestaNovedades,
                        lenghtN = lenghtN)

app.run(host='0.0.0.0', port=81)
