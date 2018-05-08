function editaUsuario(btn){
  btn.hide();
  $("#nome_perfil").attr("readonly", false);
  $("#cpf_perfil").attr("readonly", false);
  $("#estado_perfil").attr("readonly", false);
  $("#email_perfil").attr("readonly", false);
  $("#btnEditaUsuario").show()
}
