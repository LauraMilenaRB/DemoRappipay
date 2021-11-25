var extracto=(function () {
	function addRow(item) {
        var markup = "<tr class=\"rowTable\"><td>" + item.id + "</td><td>" + item.dateRegister + "</td>"
        + "<td><a class=\"btn btn-primary\" id=\"bt"+item.id +"\">Descargar PDF</a></td></tr>";
        $("#pdfs").append(markup);
    }

    function getextracto(){
        var contracto = "numero de contrato"
        if(contracto===""){
            alert("contrato invalido");
        }
        else{
            var promise = apiclient.getExtracto(contracto);
            promise.done(function(data){
                $(".rowTable").remove("tr");
                JSON.parse(data).map(addRow);

            }).fail(function(){
                alert(promes.responseText);
            });
        }
    }
    return {
        getExtractos(){
            var test =getextracto();
        },
        downloadpdf(id){
            //var beanId = $(id).data('id');
            alert('Bean value:' + id);
        }
    };
}());