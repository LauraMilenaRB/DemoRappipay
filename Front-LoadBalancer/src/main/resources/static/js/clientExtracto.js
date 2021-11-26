var clientExtracto = (function(){
    var apiUrl= "http://"+document.location.hostname+":80";
    return{
    	getExtractos(contrato){
            return $.ajax({
                url:  apiUrl+"/extractos",
                type: "POST",
                data: contrato,
                contentType: "application/json"});
        }
    };
}());