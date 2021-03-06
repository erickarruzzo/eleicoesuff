function populaPresidente(){
  var candidatos = candidatos_global;
  var partidos = partidos_global;
  var estados = estados_global;
  var cargos = cargos_global;
  var presidentes = [];
  var votosPresidentes = [];

  for (i=0;i<candidatos.length;i++){
    if (candidatos[i].cargo_id==1){
      presidentes.push(candidatos[i].nome);
      votos = getVotosPorCandidato(candidatos[i].id)
      votosPresidentes.push(votos)
    }
  }

  criaGrafico(presidentes, votosPresidentes, "chartPresidente")

  //for (i=0;i<candidatos.length;i++){
  //  if (candidatos[i].cargo_id==1){
  //    $("#lista_1").append('<h3><a href="/candidato/' + candidatos[i].id + '">' + candidatos[i].nome + ' - ' + partidos[candidatos[i].partido_id -1].sigla + '/' + estados[candidatos[i].estado_id - 1].sigla + '</a> (<span id="candidato_' + candidatos[i].id + '"></span>)</h4>');
  //  }
  //}
}

function getRandomColor(numero) {
  colors = [];
  for (i=0;i<numero;i++){
    color = '#' + (Math.random().toString(16) + '0000000').slice(2, 8);
    colors.push(color);
  }
  return colors;
}

function criaGrafico(candidatos, valores, nome){

  var ctx = document.getElementById(nome);
  var myChart = new Chart(ctx, {
  type: 'bar',
  data: {
      labels: candidatos,
      datasets: [{
          label: 'Número de votos',
          data: valores,
          backgroundColor: getRandomColor(candidatos.length),
          borderWidth: 1
      }]
  },
  options: {
    legend: {
      display: false
    },
    scales: {
        yAxes: [{
            ticks: {
                beginAtZero:true
            }
        }]
    }
  }
  });
}

function populaCargos(cargo_id){
  var candidatos = candidatos_global;
  var partidos = partidos_global;
  var estados = estados_global;
  var cargos = cargos_global;

  for (i=0;i<estados.length;i++){

    if (i==0) {
      $("#lista_" + cargo_id).append('<a class="nav-link active" id="' + estados[i].id + '-tab" data-toggle="pill" href="#body_' + estados[i].id + cargo_id + '" role="tab" aria-controls="body_' + estados[i].id + cargo_id + '" aria-selected="true">' + estados[i].nome + ' (<span id="estado_cargo_' + estados[i].id + cargo_id + '"></span>)</a>');
    } else {
      $("#lista_" + cargo_id).append('<a class="nav-link" id="' + estados[i].id + '-tab" data-toggle="pill" href="#body_' + estados[i].id + cargo_id + '" role="tab" aria-controls="body_' + estados[i].id + cargo_id + '" aria-selected="true">' + estados[i].nome + ' (<span id="estado_cargo_' + estados[i].id + cargo_id + '"></span>)</a>');
    }

    if (i==0) {
      $("#tabContent_" + cargo_id).append('<div class="tab-pane fade show active" id="body_' + estados[i].id + cargo_id + '" role="tabpanel" aria-labelledby="' + estados[i].id + '-tab"></div>');
    } else {
      $("#tabContent_" + cargo_id).append('<div class="tab-pane fade" id="body_' + estados[i].id + cargo_id + '" role="tabpanel" aria-labelledby="' + estados[i].id + '-tab"></div>');
    }

    var candidatosTemp = [];
    var votosTemp = [];

    for (j=0;j<candidatos.length;j++){
      if (estados[i].id == candidatos[j].estado_id){
        if (candidatos[j].cargo_id == cargo_id){
            //$("#body_" + estados[i].id + cargo_id).append('<h3><a href="/candidato/' + candidatos[j].id + '">' + candidatos[j].nome + ' - ' + partidos[candidatos[j].partido_id - 1].sigla + '/' + estados[candidatos[j].estado_id - 1].sigla + '</a> (<span id="candidato_' + candidatos[j].id + '"></span>)</h4>');
            $("#body_" + estados[i].id + cargo_id).append('<canvas id="chart' + cargo_id + estados[candidatos[j].estado_id - 1].id + '" width="1600" height="900"></canvas>');
            candidatosTemp.push(candidatos[j].nome);
            votos = getVotosPorCandidato(candidatos[j].id);
            votosTemp.push(votos);
        }
      }
    }
    if (candidatosTemp.length > 0) {
      criaGrafico(candidatosTemp, votosTemp, "chart" + cargo_id + estados[i].id)
    }    
  }
}

$(document).ready(function() {
    getCandidatos();
    getPartidos();
    getEstados();
    getCargos();
    populaPresidente();
    populaCargos(2); //Governador
    populaCargos(3); //Senador
    populaCargos(4); //Deputado Federal
    populaCargos(5); //Deputado Estadual

    for (i=1;i<=cargos_global.length;i++){
      getVotosPorCargo(i);
    }

    for (i=1;i<=estados_global.length;i++){
      for (j=1;j<=cargos_global.length;j++){
          getVotosPorCargoEstado(j,i);
      }
    }

    for (i=1;i<=candidatos_global.length;i++){
      getVotosPorCandidato(i);
    }
});

function getVotosPorCargo(cargo_id){
  var cargos = cargos_global;

  $.ajax({
      type: "GET",
      url: "/get_votos_por_cargo",
      dataType: "json",
      data: {
          "cargo": cargo_id
      },
      success: function(data){
        if (data.response == 1){
          $("#votos_total_" + cargo_id).html(data.response + " voto")
        } else {
          $("#votos_total_" + cargo_id).html(data.response + " votos")
        }
      }
  });
}

function getVotosPorCargoEstado(cargo_id, estado_id){
  var estados = estados_global;
  var cargos = cargos_global;

  $.ajax({
      type: "GET",
      url: "/get_votos_por_cargo_estado",
      dataType: "json",
      data: {
          "cargo": cargo_id,
          "estado": estado_id
      },
      success: function(data){
        if (data.response == 1){
          $("#estado_cargo_" + estado_id + cargo_id).html(data.response + " voto")
        } else {
          $("#estado_cargo_" + estado_id + cargo_id).html(data.response + " votos")
        }
      }
  });
}

function getVotosPorCandidato(candidato_id){
  var votos;

  $.ajax({
      type: "GET",
      url: "/get_votos_por_candidato",
      dataType: "json",
      data: {
          "candidato": candidato_id,
      },
      async:false,
      success: function(data){
        votos = data.response.toString();
      }
  });

  return votos;
}

function alternaTab(objeto) {
	if (objeto.attr('id') === "login-tab"){
		$("#login_form").show()
		$("#register_form").hide()
		$("#register-tab").removeClass("active")
		$("#login-tab").addClass("active")
	} else {
		$("#login_form").hide()
		$("#register_form").show()
		$("#login-tab").removeClass("active")
		$("#register-tab").addClass("active")
	}
}
