$(document).on('ready', function(){ //cuando el documento este listo
        
        /*Ajustamos el tamaño de los diferentes elementos*/
        $('#view').css({ //accesamos a todos los elementos div del documento
            'height': ($(document).outerHeight(true) - 90  ) //la altura del documento - 60px de la barra - los margenes
        });
        
        $('#text').css({ //accesamos a todos los elementos div del documento
            'height': ($(document).outerHeight(true)/2  ) // 50% del alto
        });        
        /*Formato sobre editor de texto*/
        $('#text').on('keyup', function(evento){
            $("#view").html("");
            $("#view").html("<p>"+$(this).text()+"</p>");
            //console.log(evento.which); permite identificar la tecla presionada
        });
        
        $('#text').focus();  //auto foco en el editor
        
});//del $('document').on('ready')