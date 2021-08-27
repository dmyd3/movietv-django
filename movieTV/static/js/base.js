
$(document).ready(function () {

    $('#sidebarCollapse').on('click', DoShrunk );

    $('.multiple-items').slick({
        infinite: true,
        slidesToShow: 3,
        slidesToScroll: 1,
        dots: true,
        //appendArrows:$('#ex1'),
        prevArrow:'<button type="button" class="slick-prev">\
            <span class="carousel-control-prev-icon" aria-hidden="true"></span></button>',
        nextArrow:'<button type="button" class="slick-next">\
            <span class="carousel-control-next-icon" aria-hidden="true"></span></button>',
    });

});

function DoShrunk(){
    $('#sidebar').toggleClass('shrunken');
    $('.fixed-top2').toggleClass('shrunken');
    $('.base-content').toggleClass('shrunken');
    console.log("SHRUNK");
}
