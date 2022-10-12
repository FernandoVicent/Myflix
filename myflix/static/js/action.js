$('.apresentacao-slider').slick({
  slidesToShow: 1,
  autoplay: true,
  arrows: false,
  autoplaySpeed: 3000,
});

$('.carousel-asistidos').slick({
  centerMode: true,
  centerPadding: '40px',
  slidesToShow: 6,
  responsive: [
    {
      breakpoint: 1200,
      settings: {
        arrows: false,
        centerMode: true,
        centerPadding: '20px',
        slidesToShow: 3
      }
    },
    {
      breakpoint: 768,
      settings: {
        arrows: false,
        centerMode: true,
        centerPadding: '40px',
        slidesToShow: 3
      }
    },
    {
      breakpoint: 480,
      settings: {
        arrows: false,
        centerMode: true,
        centerPadding: '5px',
        slidesToShow: 4
      }
    }
  ]
});
