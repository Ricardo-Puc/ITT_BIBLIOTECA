/*
function multiplicar(numero1, numero2) {
    return numero1 * numero2;
}

var nombre = "juanito";
var edad = 90;
var sexo = true;

if(edad < 18) {
    alert("Persona es menor de edad");
} else if(edad >= 18 && edad <=30) {
    alert("La persona es un adulto joven");
} else {
    alert("la persona es mayor de edad");
}

for(i=0; i < 15; i++) {
    console.log(i);
}
var i = 0;
while(i < 30) {
    console.log(i);
    i++;
}

console.log("El resulado fue " + multiplicar(30,6));*/


//esperaremos que la pagina este cargada completamente

//$ significa jquery
$(document).ready(function() {
    //esta funcion se ejecuta cuando la pagina este totalmente
    //cargada

    //obtendremos una referencia al boton
    var btnCalcular = $("#btnCalcular");
    //le agregamos un escuchador


    btnCalcular.click(function() {
        
        //obtendremos una referencia a la caja numero1
        var txtNumero1  = $("#txtNumero1");
        
        var txtNumero2 = $("#txtNumero2");
        var txtResultado = $("#txtResultado");
        
        var resultado = 0;
        var tipoCalculo = $("#cboTipo").val();

        if(tipoCalculo == 1) {
            resultado =
             parseInt(txtNumero1.val()) + parseInt(txtNumero2.val());
        } else if(tipoCalculo == 2) {
            resultado = 
            parseInt(txtNumero1.val()) - parseInt(txtNumero2.val());
        } else if(tipoCalculo == 3) {
            resultado = 
            parseInt(txtNumero1.val()) * parseInt(txtNumero2.val());
        } else {
            resultado = 
            parseInt(txtNumero1.val()) / parseInt(txtNumero2.val());
        }
        
        txtResultado.val(resultado);
    });

});


    
    







