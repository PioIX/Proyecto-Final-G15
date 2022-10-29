function signUp() {
  nombreLogin = document.getElementById("name").value 
  contraLogin = document.getElementById("password").value
 
  $.ajax({ 
    url:"/verificar", 
    type:"POST", 
    data: {"value": nombreLogin,
          "value2": contraLogin}, 

    success: function(response){  //En response voy a tener el JSON
      datos = (response); //

      
      //document.getElementById("form1").submit()
      if (datos){
        alert(`Ha sido ingresado correctamente`)
        location.href = "/administrador"
      }
      else{
        alert("Datos incorrectos")
        location.href = "/inicio"
      }
      
      
    }, 
    error: function(error){ 
      console.log(error); 
  }, });

}
function index() {
  informacion = document.getElementById("informacion").value
  fotos = document.getElementById("fotos").files[0]
  console.log(fotos)
  $.ajax({ 
    url:"/agregarIndex", 
    type:"POST", 
    data: {"value": informacion,
          "value2": fotos,
          }, 

    success: function(response){  //En response voy a tener el JSON
      datos = (response); 

     alert(`Ha sido agregado correctamente`)
    
    }, 
    error: function(error){ 
      console.log("hola"); 
  }, });
}

function borrarIndex(){
  SelectEliminarIndexImagen = document.getElementById('SelectEliminarIndexImagen').value

  $.ajax({
    url:"/borrarIndex",
    type:"DELETE",
    data: {"value": SelectEliminarIndexImagen,
          },

    success: function(response){
      datos = response
      alert("La imagen se ha eliminado correctamente")
      
    },
    error: function(error){
      console.log(error);
  }, });

}

function museos() {
  titulo= document.getElementById("titulo").value 
  informacion= document.getElementById("informacion").value
  coleccion= document.getElementById("coleccion").value 
  horario= document.getElementById("horario").value 
  precio= document.getElementById("precios").value
  ubicacion= document.getElementById("ubicacion").value 
  barrio= document.getElementById("barrio").value
  linkPagina= document.getElementById("linkPagina").value 
  logo= document.getElementById("logo").files[0]
  console.log(logo)
  $.ajax({ 
    url:"/agregarMuseo", 
    type:"POST", 
    data: {"value": titulo,
          "value2": informacion,
          "value3": coleccion,
          "value4": horario,
          "value5": precio,
          "value6": ubicacion,
          "value7": barrio,
          "value8": linkPagina,
          "value9": logo,
          }, 

    success: function(response){  //En response voy a tener el JSON
      datos = (response); 

      alert(`Ha sido agregado correctamente`)
    
    }, 
    error: function(error){ 
      console.log(error); 
  }, });

}
function borrarMuseos(){
  SelectEliminarM = document.getElementById('SelectEliminarM').value

  $.ajax({
    url:"/borrarMuseos",
    type:"DELETE",
    data: {"value": SelectEliminarM,
          }, 

    success: function(response){
      datos = response
      alert("La definición se ha eliminado correctamente")
      
    },
    error: function(error){
      console.log(error);
  }, });
}
function internacional() {
  campo1 = document.getElementById("campo1").value 
  textoCampo1 = document.getElementById("textocampo1").value
  fotoCampo1 = document.getElementById("fotoCampo1").files[0] 
  campo2 = document.getElementById("campo2").value
  textoCampo2 = document.getElementById("textocampo2").value 
  fotoCampo2 = document.getElementById("fotoCampo2").files[0]
  campo3 = document.getElementById("campo3").value 
  textoCampo3 = document.getElementById("textocampo3").value
  fotoCampo3 = document.getElementById("fotoCampo3").files[0] 
  
  $.ajax({ 
    url:"/agregarInternacional", 
    type:"POST", 
    data: {"value": campo1,
          "value2": textoCampo1,
          "value3": fotoCampo1,
          "value4": campo2,
          "value5": textoCampo2,
          "value6": fotoCampo2,
          "value7": campo3,
          "value8": textoCampo3,
          "value9": fotoCampo3,
          }, 

    success: function(response){  //En response voy a tener el JSON
      datos = (response); 

      alert(`Ha sido agregado correctamente`)
      
    }, 
    error: function(error){ 
      console.log(error); 
  }, });

}
function preguntas() {
  pregunta = document.getElementById("pregunta").value 
  respuesta = document.getElementById("respuesta").value
  
  $.ajax({ 
    url:"/agregarPreguntas", 
    type:"POST", 
    data: {"value": pregunta,
          "value2": respuesta,
          }, 

    success: function(response){  //En response voy a tener el JSON
      datos = (response); 

      alert(`Ha sido agregado correctamente`)
  
    }, 
    error: function(error){ 
      console.log("hola"); 
      console.log(error); 
  }, });

}
function borrarPreguntas(){
  SelectEliminar = document.getElementById('SelectEliminar').value

  $.ajax({
    url:"/borrarPreguntas",
    type:"DELETE",
    data: {"value": SelectEliminar,
          }, 

    success: function(response){
      datos = response
      alert("La definición se ha eliminado correctamente")
      
    },
    error: function(error){
      console.log(error);
  }, });
}

function novedades(){
  foto1=document.getElementById("foto1").value
  texto1=document.getElementById("texto1").value
  foto2=document.getElementById("foto2").value
  texto2=document.getElementById("texto2").value
  foto3=document.getElementById("foto3").value
  texto3=document.getElementById("texto3").value
  foto4=document.getElementById("foto4").value
  texto4=document.getElementById("texto4").value
  link=document.getElementById("link").value
 
  $.ajax({ 
    url:"/agregarNovedades", 
    type:"POST", 
    data: {"value": foto1,
          "value2": texto1,
          "value3": foto2,
          "value4": texto2,
          "value5": foto3,
          "value6": texto3,
          "value7": foto4,
          "value8": link,
          }, 

    success: function(response){  //En response voy a tener el JSON
      datos = (response); 

      alert(`Ha sido agregado correctamente`)

    }, 
    error: function(error){ 
      console.log(error); 
  }, });

}
function museosi(){
  document.getElementById("modificarTuPagina").hidden = true
  document.getElementById("modificarMuseos").hidden = false
  document.getElementById("modificarNovedades").hidden = true
  document.getElementById("modificarInternacional").hidden = true
  document.getElementById("modificarPreguntas").hidden = true
  
}

function novedadesi(){
  document.getElementById("modificarTuPagina").hidden = true
  document.getElementById("modificarMuseos").hidden = true
  document.getElementById("modificarNovedades").hidden = false
  document.getElementById("modificarInternacional").hidden = true
  document.getElementById("modificarPreguntas").hidden = true
    
}
function internacionali(){
  document.getElementById("modificarTuPagina").hidden = true
  document.getElementById("modificarMuseos").hidden = true
  document.getElementById("modificarNovedades").hidden = true
  document.getElementById("modificarInternacional").hidden = false
  document.getElementById("modificarPreguntas").hidden = true
  
}
function preguntasi(){
  document.getElementById("modificarTuPagina").hidden = true
  document.getElementById("modificarMuseos").hidden = true
  document.getElementById("modificarNovedades").hidden = true
  document.getElementById("modificarInternacional").hidden = true
  document.getElementById("modificarPreguntas").hidden = false
  
  
}
 
