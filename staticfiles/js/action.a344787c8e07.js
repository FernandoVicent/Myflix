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
  arrows: true,
  prevArrow:"<img class='a-left control-c prev slick-prev' src='https://projeto-myflix.s3.amazonaws.com/icons/left-arrow.png'>",
  nextArrow:"<img class='a-right control-c next slick-next' src='https://projeto-myflix.s3.amazonaws.com/icons/right-arrow.png'>",
  responsive: [
    {
      breakpoint: 1200,
      settings: {
        arrows: true,
        centerMode: true,
        centerPadding: '20px',
        slidesToShow: 6,
      }
    },
    {
      breakpoint: 768,
      settings: {
        arrows: true,
        centerMode: true,
        centerPadding: '20px',
        slidesToShow: 6,
      }
    },
    {
      breakpoint: 480,
      settings: {
        arrows: true,
        centerMode: true,
        slidesToShow: 2,
      }
    }
  ]
});
