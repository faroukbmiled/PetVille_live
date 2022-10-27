$(document).ready(function () {
    $('.checkboxclass').SumoSelect({placeholder: '-- Your services --', csvDispCount: 4 });
    });
$(document).ready(function(){
$('#slc2').hide();
$("#editbtn").click(function () {
    $('#slc1').fadeOut("fast");
    $('#slc2').fadeIn("slow");

});
$("#backbtn").click(function () {
    $('#slc2').fadeOut("fast");
    $('#slc1').fadeIn("slow");

});
},);
 