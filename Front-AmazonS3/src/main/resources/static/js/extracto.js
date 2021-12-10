$(document).ready(function(){
    document.getElementById('section0').style.display = 'none';
});
var extracto=(function () {
    var map = new Map();
    var s3 ;
    const myBucket = 'demo-rappipay-s3'

    function base64ToArrayBuffer(keyPDF) {
        var bucketParams = {
            Bucket : myBucket,
            Key: keyPDF
        };
        var promise = s3.getSignedUrlPromise('getObject', bucketParams);
        promise.then(function(url) {
           window.open(url,'', 'height=700,width=840');
        }, function(err) {
            alert("Error", err);
        });
    }

	function addRow(item) {
        var markup = "<tr class=\"rowTable\"><td>" + item.id + "</td><td>" + item.date + "</td>"
        + "<td><a class=\"btn-check:checked\" id=\""+item.keyPDF+"\" onclick=\"extracto.downloadpdf(id)\">Descargar PDF</a></td></tr>";
        $("#pdfs").append(markup);

    }
    function successS3Object(listS3,contratoId){
        var list = [];
        var listS3=listS3.filter(x => x.Size!=0);
        var idnum=1;
        listS3.map(x => list.push({"id":idnum++,"date":x.LastModified.toString().replace(" (hora estándar de Colombia)",""), "keyPDF": x.Key}))
        return list;
    }

    function getextracto(){
        var contract = document.getElementById('contractid').value
        var statement= "statements/";
        if(contract===""){
            alert("contrato invalido");
        }
        else{
            AWS.config.update({accessKeyId: 'AKIAVFHJMDPBUAIK7CEO',
                                secretAccessKey: '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',
                                region: 'us-east-1'
            })
            s3 = new AWS.S3()
            var bucketParams = {
                Bucket : myBucket,
                Prefix: statement.concat(contract.trim().concat('/'))
            };
            s3.listObjectsV2(bucketParams, function(err, data) {
              if (err) {
                alert("Error", err);
              } else {
                $(".rowTable").remove();
                console.log(data.Contents)
                if(data.Contents.length>1){
                    successS3Object(data.Contents,contract).map(addRow);
                }
              }
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