$(document).ready(function(){
$(function() {setTimeout(function() {$("#menu").hide('blind', {}, 30)}, 30);}); 
$(function() {setTimeout(function() {$("#h_div").hide('blind', {}, 35)}, 35);}); 
$('#menu').hover(function(){$('#h_div').fadeIn("slow");}, function(){$('#h_div').fadeOut("slow");});
$('#dropd').on('change', function(){
    $(this).val(); 
    $("#menu").fadeIn('slow');
});
},);

 