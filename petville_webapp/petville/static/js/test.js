$(document).ready(function(){
$(function() {setTimeout(function() {$("#menu").hide('blind', {}, 30)}, 30);}); 
$(function() {setTimeout(function() {$("#h_div").hide('blind', {}, 30)}, 30);}); 
$('#menu').hover(function(){$('#h_div').show();}, function(){$('#h_div').hide();});
$('#dropd').on('change', function(){
    $(this).val(); 
    $("#menu").show();
});
},);

 