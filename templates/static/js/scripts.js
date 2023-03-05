$( document ).ready(function() {

  // Progress bar
  let containerA = document.getElementById("circleA");

  let circleA = new ProgressBar.Circle(containerA, {

    color: '#FFF',
    strokeWidth: 8,
    duration: 1400,
    from: { color: '#aaa'},
    to: { color: '#FFF'},

    step: function(state, circle) {
      circle.path.setAttribute('stroke', state.color);

      var value = Math.round(circle.value() * 156);
      circle.setText(value);

    }

  });

  let containerB = document.getElementById("circleB");

  let circleB = new ProgressBar.Circle(containerB, {

    color: '#FFF',
    strokeWidth: 8,
    duration: 1600,
    from: { color: '#aaa'},
    to: { color: '#FFF'},

    step: function(state, circle) {
      circle.path.setAttribute('stroke', state.color);

      var value = Math.round(circle.value() * 125);
      circle.setText(value);

    }

  });

  let containerC = document.getElementById("circleC");

  let circleC = new ProgressBar.Circle(containerC, {

    color: '#FFF',
    strokeWidth: 8,
    duration: 1800,
    from: { color: '#aaa'},
    to: { color: '#FFF'},

    step: function(state, circle) {
      circle.path.setAttribute('stroke', state.color);

      var value = Math.round(circle.value() * 32);
      circle.setText(value);

    }

  });

  let containerD = document.getElementById("circleD");

  let circleD = new ProgressBar.Circle(containerD, {

    color: '#FFF',
    strokeWidth: 8,
    duration: 2000,
    from: { color: '#aaa'},
    to: { color: '#FFF'},

    step: function(state, circle) {
      circle.path.setAttribute('stroke', state.color);

      var value = Math.round(circle.value() * 5423);
      circle.setText(value);

    }

  });

  // iniciando loaders quando a usuário chegar no elemento
  let dataAreaOffset = $('#data-area').offset();
  // stop serve para a animação não carregar mais que uma vez
  let stop = 0;

  $(window).scroll(function (e) {

    let scroll = $(window).scrollTop();

    if(scroll > (dataAreaOffset.top - 500) && stop == 0) {
      circleA.animate(1.0);
      circleB.animate(1.0);
      circleC.animate(1.0);
      circleD.animate(1.0);

      stop = 1;
    }

  });

  // Parallax

  // setTimeout serve para carregar primeiro as imagens
  setTimeout(function() {
    $('#data-area').parallax({imageSrc: '/static/img/cidadeparallax.png'});
    $('#apply-area').parallax({imageSrc: '/static/img/pattern.png'});
  }, 200);

  // Filtro portfólio

  $('.filter-btn').on('click', function() {

    let type = $(this).attr('id');
    let boxes = $('.project-box');

    $('.main-btn').removeClass('active');
    $(this).addClass('active');

    if(type == 'dsg-btn') {
      eachBoxes('dsg', boxes);
    } else if(type == 'dev-btn') {
      eachBoxes('dev', boxes);
    } else if(type == 'seo-btn') {
      eachBoxes('seo', boxes);
    } else {
      eachBoxes('all', boxes);
    }

  });

  function eachBoxes(type, boxes) {

    if(type == 'all') {
      $(boxes).fadeIn();
    } else {
      $(boxes).each(function() {
        if(!$(this).hasClass(type)) {
          $(this).fadeOut('slow');
        } else {
          $(this).fadeIn();
        }
      });
    }
  }

  // scroll para as seções

  let navBtn = $('.nav-item');

  let bannerSection = $('#mainSlider');
  let aboutSection = $('#about-area');
  let servicesSection = $('#services-area');
  let teamSection = $('#team-area');
  let portfolioSection = $('#portfolio-area');
  let contactSection = $('#contact-area');

  let scrollTo = '';

  $(navBtn).click(function() {

    let btnId = $(this).attr('id');

    if(btnId == 'about-menu') {
      scrollTo = aboutSection;
    } else if(btnId == 'services-menu') {
      scrollTo = servicesSection;
    } else if(btnId == 'team-menu') {
      scrollTo = teamSection;
    } else if(btnId == 'portfolio-menu') {
      scrollTo = portfolioSection;
    } else if(btnId == 'contact-menu') {
      scrollTo = contactSection;
    } else {
      scrollTo = bannerSection;
    }

    $([document.documentElement, document.body]).animate({
        scrollTop: $(scrollTo).offset().top - 70
    }, 1500);
  });

});


// FRONT END VALIDATION FORM
function validateEmail(email){
  const regex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
  return regex.test(email);

}

// FRONT END VALIDATION FORM
function formNovidade(){
  const email = document.getElementById("email-input").value;

  if (email == ""){
    swal('Opsss !', "Email não pode ser vázio...", "error")
    return false;
  }
  else if (!(validateEmail(email))){
    document.getElementById('email-input').value='';
    swal("Opsss !", "Email inválido!", "error");
    return false;
  }
  else{
    return true
}
}

// FRONT END VALIDATION FORM
function formContato(){
  const email = document.getElementById("id_email").value;
  const assunto = document.getElementById("id_assunto").value;
  const texto = document.getElementById("id_texto").value;

  if (email == ""){
    swal('Atenção!', "Email não pode ser vazio...")
    return false;
  }
  else if (!(validateEmail(email))){
    document.getElementById('id_email').value='';
    swal("Atenção!", "Email inválido!");
    return false;
  }

  else if (assunto == ""){
    swal('Atenção!', 'Informe o assunto...')
    return false;
  }

  else if (texto == ""){
    swal("Atenção", 'Digite a sua mensagem...')
    return false;
  }
  else{
    return true
}
}

// input masck (telefone)
$(document).ready(function(){
  $(".telefone").inputmask("(99) 99999-9999", {"onincomplete": function(){
      $(".telefone").val("");
      swal("Atenção!", "Telefone incompleto. Por favor revise! ");
      return false;
  }});
});



function formCadastro(){
  const nome = document.getElementById('id_nome').value;
  const sobrenome = document.getElementById('id_sobrenome').value;
  const telefone = document.getElementById('id_telefone').value;
  const email = document.getElementById('id-email-cadastro').value;
  const servico = document.getElementById('id_servico').value;

  var padrao = /[^a-zà-ú]/gi;

  var valida_nome = nome.match(padrao);
  var valida_sobrenome = sobrenome.match(padrao);



  if( valida_nome || !nome ) {
    swal('Atenção!', 'Informe o seu nome, apenas letras!')
    return false;
   }
  else if( valida_sobrenome || !sobrenome ){
    swal('Atenção!', 'Informe o seu sobrenome, apenas letras!')
  }

  else if (email == ""){
    swal('Atenção!', "Informe o seu email")
    return false;
  }

  else if (!(validateEmail(email))){
    document.getElementById('id-email-cadastro').value='';
    swal("Atenção!", "Email inválido!");
    return false;
  }

  else if (servico == ''){
    swal('Atenção!', 'Serviço selecionado é inválido!')
  }

  else{
      return true
}}