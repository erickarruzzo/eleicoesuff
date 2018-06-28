$(document).ready(function() {
    getCandidatos();
});

function carregaEstado(valor){
    if (valor != 1){
        $("#divEstado").show();
    } else {
        $("#divEstado").hide();
    }
}

function consultar(cargo_id, estado_id){
    var candidatos = candidatos_global;
    var votados = [];
    var votos_totais = [];

    if (cargo_id == 1){
        for (i=0;i<candidatos.length;i++){
            if (candidatos[i].cargo_id==cargo_id){
                votados.push(candidatos[i].nome);
                votos = candidatos[i].total_votos
                votos_totais.push(votos)
            }
        }
    } else {
        if (estado_id == "" || estado_id == null){
            $("#erro_consulta").show();
            $("#erro_consulta").text("Por favor, preencha o campo Estado");
            return;
        }
        for (i=0;i<candidatos.length;i++){
            if (candidatos[i].cargo_id==cargo_id && candidatos[i].estado_id==estado_id){
                votados.push(candidatos[i].nome);
                votos = candidatos[i].total_votos
                votos_totais.push(votos)
            }
        }
    }

    if (votados.length < 1){
        $("#erro_consulta").show();
        $("#erro_consulta").text("Nenhum resultado encontrado. Candidatos não cadastrados");
        return;
    }

    criaGrafico(votados, votos_totais);
    
}

function criaGrafico(candidatos, valores){
    $("#erro_consulta").hide();
    $("#sectionChart").show();

    //Apagando o canvas para redesenhar
    $('#chart').remove(); // this is my <canvas> element
    $('#graph-container').append('<canvas id="chart"><canvas>');

    var ctx = document.getElementById('chart');
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

function getRandomColor(numero) {
    colors = [];
    for (i=0;i<numero;i++){
      color = '#' + (Math.random().toString(16) + '0000000').slice(2, 8);
      colors.push(color);
    }
    return colors;
}