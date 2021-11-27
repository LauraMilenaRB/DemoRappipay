$(document).ready(function(){
    document.getElementById('section0').style.display = 'none';
});

var extracto=(function () {
    var map = new Map();

    //data is the base64 encoded string
    function base64ToArrayBuffer(id) {
        if(map!=null){
            var binaryString = window.atob(map.get(id));
            var binaryLen = binaryString.length;
            var bytes = new Uint8Array(binaryLen);
            for (var i = 0; i < binaryLen; i++) {
                var ascii = binaryString.charCodeAt(i);
                bytes[i] = ascii;
            }
            var blob = new Blob([bytes], {type: "application/pdf"});
            var link = window.URL.createObjectURL(blob);
            window.open(link,'', 'height=650,width=840');
        }
    }

	function addRow(item) {
        var markup = "<tr class=\"rowTable\"><td>" + item.id + "</td><td>" + item.date + "</td>"
        + "<td><a class=\"btn-check:checked\" id=\"extracto-"+item.date+"\" onclick=\"extracto.downloadpdf(id)\">Descargar PDF</a></td></tr>";
        $("#pdfs").append(markup);
        map.set("extracto-"+item.date,item.pdf);

    }

    function getextracto(){
        var contracto = document.getElementById('contractid').value
        if(contracto===""){
            alert("contrato invalido");
        }
        else{
            var promise = clientExtracto.getExtractos(contracto);
            promise.done(function(data){
                $(".rowTable").remove();

                data.map(addRow);
            }).fail(function(){
                alert(promise.responseText);
            });
        }
    }
    function mostrarBt(){
        document.getElementById('section0').style.display = 'block';
        $("#btsee").addClass("disabled");
    }
    return {
        getExtractos(){
            var getBt =mostrarBt();
            var getExtracto = getextracto();
        },
        downloadpdf(id){
            var arrrayBuffer = base64ToArrayBuffer(id);
        }
    };
}());