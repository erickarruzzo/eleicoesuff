function votarCandidato(id_candidato, id_usuario){
  $.ajax({
      type: "POST",
      url: "voto-registrar",
      data: {
          "usuario_id": id_usuario,
          "candidato_id": id_candidato
      },
      success: function(data){
        $("#alerta_voto").html("")
        if (data.response==0){
          $("#alerta_voto").append('<div class="alert alert-danger alert-dismissible fade show" role="alert">Seu voto não foi computado, pois já votou nesse cargo.<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>')
        } else {
          $("#alerta_voto").append('<div class="alert alert-success alert-dismissible fade show" role="alert">Voto computado.<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>')
        }
      }
  });
}

function carregaCandidatos(){
  window.location.href = "voto/" + $("#usuario_register").val()
}
