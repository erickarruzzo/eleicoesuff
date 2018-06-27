function consultaLocal(titulo, estado){
    $.ajax({
        type: "GET",
        url: "/get_local_votacao",
        dataType: "json",
        data: {
            "titulo": titulo,
            "estado": estado
        },
        success: function(local){
            if (local){
                $("#section_resultado").show();
                $("#erro_consulta").hide();
                $("#tabela_local").html('<tr><td>' + local.zona + '</td><td>' + local.secao + '</td><td>' + local.endereco + '</td><td>' + local.estado + '</td></tr>');
                $('#mapa').html(local.mapa)
            } else {
                $("#section_resultado").hide();
                $("#erro_consulta").show();
            }
        }
    });
}