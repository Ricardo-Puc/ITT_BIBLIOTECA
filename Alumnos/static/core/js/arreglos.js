

window.onload = function() {

    var nombres = ["paula", "joaquin", "laslo", 2000];

    //agregamos un elemento mas al final 
    //del arreglo
    nombres.push("tobias");
    for(i=0; i < nombres.length; i++) {
        console.log(nombres[i]);
    }

    //foreach

    nombres.forEach(function(item) {
        console.log(item);
    });

    //JSON
    //arreglo de objetos JSON
    var personas = [
        {
            "rut":"888888-1",
            "nombre":"rodrigo",
            "edad":99,
            "sexo":true
        },
        {
            "rut":"7777777-1",
            "nombre":"rafael",
            "edad":20,
            "sexo":true
        },
        {
            "rut":"2222222-1",
            "nombre":"laura",
            "edad":50,
            "sexo":false
        }
    ]

    personas.forEach(function(item){

        console.log(item.nombre);
        console.log(item.edad);
        console.log(item.rut);
        console.log("--------------------");

    });
    

}