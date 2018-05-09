var candidatos_global;
var partidos_global;
var estados_global;
var cargos_global;

function populaPresidente(){
  var candidatos = candidatos_global;
  var partidos = partidos_global;
  var estados = estados_global;
  var cargos = cargos_global;

  for (i=0;i<candidatos.length;i++){
    if (candidatos[i].cargo_id_id==1){
      $("#lista_presidente").append('<h3><a href="/candidato/' + candidatos[i].id + '">' + candidatos[i].nome + ' - ' + partidos[candidatos[i].partido_id_id - 1].sigla + '/' + estados[candidatos[i].estado_id_id - 1].sigla + '</a></h3></div>');
    }
  }
}

$(document).ready(function() {
    getCandidatos();
    getPartidos();
    getEstados();
    getCargos();
    populaPresidente();
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

function getCandidatos() {
  $.ajax({
      type: "GET",
      url: "get_candidatos",
      dataType: "json",
      async: false,
      success: function(candidatos){
        candidatos_global = candidatos;
      },
      error: function(erro){
        console.log(erro)
      }
  });
}

function getPartidos() {
  $.ajax({
      type: "GET",
      url: "get_partidos",
      dataType: "json",
      async: false,
      success: function(partidos){
        partidos_global = partidos;
      },
      error: function(erro){
        console.log(erro)
      }
  });
}

function getEstados() {
  $.ajax({
      type: "GET",
      url: "get_estados",
      dataType: "json",
      async: false,
      success: function(estados){
        estados_global = estados;
      },
      error: function(erro){
        console.log(erro)
      }
  });
}

function getCargos() {
  $.ajax({
      type: "GET",
      url: "get_cargos",
      dataType: "json",
      async: false,
      success: function(cargos){
        cargos_global = cargos;
      },
      error: function(erro){
        console.log(erro)
      }
  });
}
