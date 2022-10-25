$(document).ready(function () {
    $('.checkboxclass').SumoSelect({placeholder: '-- Your services --', csvDispCount: 4 });
    });
$(document).ready(function(){
$('#section2').hide();
$(function() {setTimeout(function() {$("#pass2").hide('blind', {}, 0)}, 0);}); 
$(function() {setTimeout(function() {$("#menu").hide('blind', {}, 30)}, 30);}); 
$(function() {setTimeout(function() {$("#h_div").hide('blind', {}, 35)}, 35);}); 
$('#menu').hover(function(){$('#h_div').fadeIn("slow");}, function(){$('#h_div').fadeOut("fast");});
$('#password').keypress(function() {
    $('#pass2').fadeIn("slow");
    $(this).focus();
    });
$('#dropd').on('change', function(){
    $(this).val(); 
    $("#menu").fadeIn('slow');
});
$("#next").click(function () {
    $('#section1').fadeOut("fast");
    $('#section2').fadeIn("slow");

});
$('#next').prop('disabled',true);  
$('#password2').keyup(function(){  
    $('.submit').prop('disabled', this.value == "" ? true : false);  
});
$("#backto").click(function () {
    $('#section2').hide();
    $('#section1').fadeIn("slow");
});
},);
 