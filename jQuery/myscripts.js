// $('h1').click(function () {
//   $(this).text("I was changed!")
// })
//
// $('input').eq(0).keypress(function(event) {
//   if(event.which === 13){
//     $('h3').toggleClass('turnBlue');
//   }
// })

// $('h1').on('mouseenter',function () {
//   $(this).toggleClass('turnBlue');
// })


$('input').eq(1).on('click',function () {
  $('.container').fadeOut(800);
})
