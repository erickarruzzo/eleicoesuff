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
  });
}
