function populaPresidente(){
  var candidatos = candidatos_global;
  var partidos = partidos_global;
  var estados = estados_global;
  var cargos = cargos_global;

  for (i=0;i<candidatos.length;i++){
    if (candidatos[i].cargo_id_id==1){
      $("#lista_1").append('<h3><a href="/candidato/' + candidatos[i].id + '">' + candidatos[i].nome + ' - ' + partidos[candidatos[i].partido_id_id - 1].sigla + '/' + estados[candidatos[i].estado_id_id - 1].sigla + '</a></h3></div>');
    }
  }
}

function populaCargos(cargo_id){
  var candidatos = candidatos_global;
  var partidos = partidos_global;
  var estados = estados_global;
  var cargos = cargos_global;

  for (i=0;i<estados.length;i++){
    $("#lista_" + cargo_id).append('<div><br><h3>' + estados[i].nome + '</h3>');
    for (j=0;j<candidatos.length;j++){
      if (candidatos[j].cargo_id_id == cargo_id){
        if (estados[i].id == candidatos[j].estado_id_id){
            $("#lista_" + cargo_id).append('<h4><a href="/candidato/' + candidatos[j].id + '">' +  candidatos[j].nome + ' - ' + partidos[candidatos[j].partido_id_id - 1].sigla + '/' + estados[candidatos[j].estado_id_id - 1].sigla + '</a></h4>');
        }
      }
    }
    $("#lista_" + cargo_id).append('</div>');
  }
}

$(document).ready(function() {
    getCandidatos();
    getPartidos();
    getEstados();
    getCargos();
    populaPresidente();
    populaCargos(2);
    populaCargos(3);
    populaCargos(4);
    populaCargos(5);

});

function contadorVotos(candidatos, cargo, estado){
  $.ajax({
      type: "GET",
      url: "/contador_votos",
      dataType: "json",
      data: {
          "candidatos": candidatos,
          "cargo": cargo,
          "estado": estado
      },
      success: function(response){

      },
      error: function(){

      }
  });
}
