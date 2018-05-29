function getCandidatosComFiltro(nome, partido, cargo, estado) {
  if (nome == null || nome == ''){
    nome = null
  }
  if (partido == null || partido == ''){
    partido = null
  }
  if (cargo == null || cargo == ''){
    cargo = null
  }
  if (estado == null || estado == ''){
    estado = null
  }

  $.ajax({
      type: "GET",
      url: "get_candidatos_com_filtro",
      dataType: "json",
      data: {
          "nome": nome,
          "partido": partido,
          "cargo": cargo,
          "estado": estado
      },
      success: function(data){
        if (data.length > 0){
          $("#tabela-candidatos").html('');

          for(i=0;i<data.length;i++){
            $("#tabela-candidatos").append('<tr><th scope="row">' + data[i].id + '</th><td>' + data[i].candidato + '</td><td>' + data[i].partido + '</td><td>' + data[i].estado + '</td><td>' + data[i].cargo + '</td><td><a class="btn btn-primary" href="candidato/' + data[i].id + '"><i class="fas fa-user-tie"></i></a></td></tr>');
          }

          $(".pagination").html('');
          $("#aviso-busca").html('');

        } else {
          $("#aviso-busca").text("Nenhum resultado para a busca");
        }
      }
  });
}
