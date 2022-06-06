$('[data-fancybox="images"]').fancybox({
  buttons : [
    'slideShow',
    'zoom',
    'fullScreen',
    'close'
  ],
  loop: true,
  gutter : 10,
  keyboard: true,
  arrows: true,
  infobar: true,
  smallBtn: true,
  toolbar: true,
  protect: true,
  modal: false,
  idleTime: 3,
  animationEffect: "zoom-in-out",
  animationDuration: 500,
  transitionEffect: "slide",
  transitionDuration: 1200,
  slideClass: "myClass",
  baseClass: "myclass",
   slideShow: {
    autoStart: false,
    speed: 6000
  },
youtube : {
  controls : 0,
  showinfo : 0
},
  thumbs : {
    autoStart : false
  }
});
