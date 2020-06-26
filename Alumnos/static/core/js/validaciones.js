

$(document).ready(function() {

    $("#formularioAutomovil").validate({
        rules:{
            txtPatente:{
                required:true,
                minlength:3,
                maxlength:20
                //email:true,
                //date:true
            },
            cboMarca: {
                required:true
            },
            txtAnio: {
                required:true,
                number:true,
                min:1950,
                max:2018
            },
            txtModelo:{
                required:true,
                minlength:3,
                maxlength:20
            }

        },
        messages: {
            txtPatente:{
                required:"Campo requerido",
                minlength:"Este campo debe tener al menos 3 caracteres",
                maxlength:"Este campo debe tener como maximo 20 caracteres"
            },
            cboMarca: {
                required:"Eliga una opción"
            },
            txtAnio:{ 
                required:"Este campo es requerido",
                min:"El año minima es 1950",
                max:"No puede ingresar un año superior a 2018"
            },
            txtModelo: {
                required:"Este campo es requerido",
                minlength:"Minimo 3 caracteres",
                maxlength:"Maximo 20 caracteres"
            }
        }
    });

});