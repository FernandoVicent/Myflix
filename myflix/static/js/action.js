$('.apresentacao-slider').slick({
  slidesToShow: 1,
  slidesToScroll: 1,
  autoplay: true,
  arrows: true,
  autoplaySpeed: 3000,
});

$('.carousel-asistidos').slick({
  centerMode: true,
  centerPadding: '40px',
  slidesToShow: 8,
  responsive: [
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
        centerPadding: '40px',
        slidesToShow: 1
      }
    }
  ]
});
$('.terror').slick({
  centerMode: true,
  centerPadding: '40px',
  slidesToShow: 8,
  responsive: [
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
        centerPadding: '40px',
        slidesToShow: 1
      }
    }
  ]
});