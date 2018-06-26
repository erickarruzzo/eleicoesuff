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
      type: "POST",
      url: "candidatos",
      dataType: "json",
      data: {
          "nome": nome,
          "partido": partido,
          "cargo": cargo,
          "estado": estado,
          'csrfmiddlewaretoken': '{{ csrf_token }}'
      },
      success : function(data) {
        $('body').html(data);
      }
  });
}

function carregaCandidatos(lista_candidatos){
  var arr = [];
  for (var prop in lista_candidatos) {
      arr.push(lista_candidatos[prop]);
  }

  $.ajax({
    type: "GET",
    url: "candidatos",
    dataType: "json",
    data: {
        "candidatos": arr
    }
  });
}
