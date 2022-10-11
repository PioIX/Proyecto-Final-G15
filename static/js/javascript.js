function signUp() {
  nombreLogin = document.getElementById("name").value 
  contraLogin = document.getElementById("password").value
 
  $.ajax({ 
    url:"/ingresar", 
    type:"POST", 
    data: {"value": nombreLogin,
          "value2": contraLogin}, 

    success: function(response){  //En response voy a tener el JSON
      datos = (response); //

      alert(`Ha sido resgistrado correctamente`)
      location.href = "/administrador"
      //document.getElementById("form1").submit()
    }, 
    error: function(error){ 
      console.log("hola"); 
  }, });

}

function museos() {
  titulo= document.getElementById("titulo").value 
  informacion= document.getElementById("informacion").value
  coleccion= document.getElementById("coleccion").value 
  hora= document.getElementById("horario").value 
  precio= document.getElementById("precios").value
  ubicacion= document.getElementById("ubicacion").value 
  barrio= document.getElementById("barrio").value
  linkPagina= document.getElementById("linkPagina").value 
  logo= document.getElementById("logo").value
 
  $.ajax({ 
    url:"/guardarMuseo", 
    type:"POST", 
    data: {"value": titulo,
          "value2": informacion,
          "value3": coleccion,
          "value4": hora,
          "value5": precio,
          "value6": ubicacion,
          "value7": barrio,
          "value8": linkPagina,
          "value9": logo,
          }, 

    success: function(response){  //En response voy a tener el JSON
      datos = (response); //

      alert(`Ha sido agregado correctamente`)
    
    }, 
    error: function(error){ 
      console.log("hola"); 
  }, });

}
function internacional() {
  pregunta1 = document.getElementById("campo1").value 
  respuesta1 = document.getElementById("textoCampo1").value
  pregunta2 = document.getElementById("foto1").value 
  respuesta2 = document.getElementById("campo2").value
  pregunta3 = document.getElementById("textoCampo2").value 
  respuesta3 = document.getElementById("foto2").value
  pregunta4 = document.getElementById("campo3").value 
  respuesta4 = document.getElementById("textoCampo3").value
  pregunta5 = document.getElementById("foto3").value 
  
  console.log(pregunta1)
  console.log(respuesta1)
  console.log(pregunta2)
  console.log(respuesta2)
  console.log(pregunta3)
  console.log(respuesta3)
  console.log(pregunta4)
  console.log(respuesta4)
  console.log(pregunta5)
  console.log(respuesta5)
  $.ajax({ 
    url:"/guardarPreguntas", 
    type:"POST", 
    data: {"value": pregunta1,
          "value2": respuesta2,
          "value3": pregunta2,
          "value4": respuesta2,
          "value5": pregunta3,
          "value6": respuesta3,
          "value7": pregunta4,
          "value8": respuesta4,
          "value9":pregunta5,
          "value10": respuesta5,
          }, 

    success: function(response){  //En response voy a tener el JSON
      datos = (response); //

      alert(`Ha sido agregado correctamente`)
      
      //document.getElementById("form1").submit()
    }, 
    error: function(error){ 
      console.log("hola"); 
      console.log(error); 
  }, });

}
function preguntas() {
  pregunta1 = document.getElementById("pregunta1").value 
  respuesta1 = document.getElementById("respuesta1").value
  pregunta2 = document.getElementById("pregunta2").value 
  respuesta2 = document.getElementById("respuesta2").value
  pregunta3 = document.getElementById("pregunta3").value 
  respuesta3 = document.getElementById("respuesta3").value
  pregunta4 = document.getElementById("pregunta4").value 
  respuesta4 = document.getElementById("respuesta4").value
  pregunta5 = document.getElementById("pregunta5").value 
  respuesta5 = document.getElementById("respuesta5").value
  console.log(pregunta1)
  console.log(respuesta1)
  console.log(pregunta2)
  console.log(respuesta2)
  console.log(pregunta3)
  console.log(respuesta3)
  console.log(pregunta4)
  console.log(respuesta4)
  console.log(pregunta5)
  console.log(respuesta5)
  $.ajax({ 
    url:"/guardarPreguntas", 
    type:"POST", 
    data: {"value": pregunta1,
          "value2": respuesta2,
          "value3": pregunta2,
          "value4": respuesta2,
          "value5": pregunta3,
          "value6": respuesta3,
          "value7": pregunta4,
          "value8": respuesta4,
          "value9":pregunta5,
          "value10": respuesta5,
          }, 

    success: function(response){  //En response voy a tener el JSON
      datos = (response); //

      alert(`Ha sido agregado correctamente`)
      
      //document.getElementById("form1").submit()
    }, 
    error: function(error){ 
      console.log("hola"); 
      console.log(error); 
  }, });

}
function museosi(){
  document.getElementById("ModificarTuPagina").hidden = true
  document.getElementById("ModificarMuseos").hidden = false
  document.getElementById("modificarNovedades").hidden = true
  document.getElementById("modificarInternacional").hidden = true
  document.getElementById("modificarPreguntas").hidden = true
  
}

function novedadesi(){
  document.getElementById("ModificarTuPagina").hidden = true
  document.getElementById("ModificarMuseos").hidden = true
  document.getElementById("modificarNovedades").hidden = false
  document.getElementById("modificarInternacional").hidden = true
  document.getElementById("modificarPreguntas").hidden = true
    
}
function internacionali(){
  document.getElementById("ModificarTuPagina").hidden = true
  document.getElementById("ModificarMuseos").hidden = true
  document.getElementById("modificarNovedades").hidden = true
  document.getElementById("modificarInternacional").hidden = false
  document.getElementById("modificarPreguntas").hidden = true
  
}
function preguntasi(){
  document.getElementById("ModificarTuPagina").hidden = true
  document.getElementById("ModificarMuseos").hidden = true
  document.getElementById("modificarNovedades").hidden = true
  document.getElementById("modificarInternacional").hidden = true
  document.getElementById("modificarPreguntas").hidden = false
  
  
}
function rellenarInfo{
  $.ajax({ 
    url:"/faq", 
    type:"GET", 
    data: {"value": pregunta1,
          "value2": respuesta1}, 

    success: function(response){  //En response voy a tener el JSON
      datos = (response); //

      //alert(`Ha sido resgistrado correctamente`)
      
      //document.getElementById("form1").submit()
    }, 
    error: function(error){ 
      console.log(error); 
  }, });
  document.getElementById("summary1").innerHTML=rellenarInfo()
}
 