$(document).ready(function(){
    document.getElementById('section0').style.display = 'none';
});

var extracto=(function () {
	function addRow(item) {
        var markup = "<tr class=\"rowTable\"><td>" + item.id + "</td><td>" + item.date + "</td>"
        + "<td><a class=\"btn btn-primary\" id=\"bt"+item.id +"\">Descargar PDF</a></td></tr>";
        $("#pdfs").append(markup);
    }

    function getextracto(){
        var contracto = "1018488905"
        if(contracto===""){
            alert("contrato invalido");
        }
        else{
            var promise = clientExtracto.getExtractos(contracto);
            promise.done(function(data){
                $(".rowTable").remove("tr");
                JSON.parse(data).map(addRow);
            }).fail(function(){
                alert(promes.responseText);
            });
        }
    }
    function mostrarBt(){
        document.getElementById('section0').style.display = 'block';
    }
    return {
        getExtractos(){
            var getBt =mostrarBt();
            var getExtracto = getextracto();
        },
        downloadpdf(id){
            //var beanId = $(id).data('id');
            alert('Bean value:' + id);
        }
    };
}());