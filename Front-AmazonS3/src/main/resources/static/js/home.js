$(document).ready(function(){
    document.getElementById('section0').style.display = 'none';
});
var home=(function () {
    function mostrarTC(){
        document.getElementById('section0').style.display = 'block';
    }
    return {
        mostrarTC(){
            var mostrar =mostrarTC();
        }
    };
}());

