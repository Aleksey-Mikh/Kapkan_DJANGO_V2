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