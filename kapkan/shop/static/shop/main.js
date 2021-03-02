var map;
var marker;
function initMap ()
  {
  map = new ymaps.Map("yandexmap", {
    center: [53.905451, 27.494883],
    zoom: 12
    });
  marker = new ymaps.Placemark([53.905451, 27.494883], {
    hintContent: 'Расположение',
    balloonContent: 'Это наша организация'
    });
  map.geoObjects.add(marker);
  }
ymaps.ready(initMap);

$('.js-captcha-refresh').click(function(){
    $form = $(this).parents('form');

    $.getJSON($(this).data('url'), {}, function(json) {
        // This should update your captcha image src and captcha hidden input
    });

    return false;
});

$('.captcha').click(function () {
    $.getJSON("/captcha/refresh/", function (result) {
        $('.captcha').attr('src', result['image_url']);
        $('#id_captcha_0').val(result['key'])
    });
});