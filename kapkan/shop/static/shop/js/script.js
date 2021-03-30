$(document).ready(function() {
  // Owl Carousel
  var owl = $(".owl-carousel");
  owl.owlCarousel({
    items: 3,
    margin: 10,
    loop: false,
    rewind: true,
    nav: true,
    navClass: [ 'owl-prev', 'owl-next' ],
    mouseDrag: true,
    dots: true,
    autoplay: true,
    autoplayTimeout: 5000,
    smartSpeed: 2000,
    autoplayHoverPause: true,
  });
});

