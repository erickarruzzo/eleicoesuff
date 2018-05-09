function votarCandidato(id_candidato, id_usuario){
  $.ajax({
      type: "POST",
      url: "voto-registrar",
      data: {
          "usuario_id": id_usuario,
          "candidato_id": id_candidato
      },
  });
}

function carregaCandidatos(){
  window.location.href = "voto/" + $("#usuario_register").val()
}
