$('.container-principais').slick({
  slidesToShow: 1,
  autoplay: true,
  arrows: false,
  autoplaySpeed: 3000,
});
$('.carousel-filmes').slick({
  dots: false,
  infinite: true,
  speed: 1200,
  slidesToShow: 5,
  slidesToScroll: 1,
  responsive: [
    {
      breakpoint: 1024,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 3,
        infinite: true,
        dots: false
      }
    },
    {
      breakpoint: 600,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 2
      }
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 1
      }
    }
    // You can unslick at a given breakpoint now by adding:
    // settings: "unslick"
    // instead of a settings object
  ]
});



// $('.carousel-filmes').slick({
//   centerMode: true,
//   centerPadding: '50px',
//   slidesToShow: 6,
//   arrows: true,
//   prevArrow:"<img class='a-left control-c prev slick-prev' src='https://projeto-myflix.s3.amazonaws.com/icons/left-arrow.png'>",
//   nextArrow:"<img class='a-right control-c next slick-next' src='https://projeto-myflix.s3.amazonaws.com/icons/right-arrow.png'>",
//   responsive: [
//   {
//       breakpoint: 1400,
//       settings: {
//         arrows: true,
//         centerMode: true,
//         slidesToShow: 5,
//       }
//     },
//     {
//       breakpoint: 1200,
//       settings: {
//         arrows: true,
//         centerMode: true,
//         slidesToShow: 4,
//       }
//     },
//     {
//       breakpoint: 992,
//       settings: {
//         arrows: true,
//         centerMode: true,
        
//         slidesToShow: 4,
//       }
//     },
//     {
//       breakpoint: 768,
//       settings: {
//         arrows: true,
//         centerMode: true,
        
//         slidesToShow: 3,
//       }
//     },
//     {
//       breakpoint: 600,
//       settings: {
//         arrows: true,
//         centerMode: true,
//         slidesToShow: 2,
//       }
//     },
//     {
//       breakpoint: 480,
//       settings: {
//         arrows: true,
//         centerMode: true,
//         slidesToShow: 2,
//       }
//     },
//   ]
// });
