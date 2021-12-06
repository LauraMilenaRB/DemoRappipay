var clientExtracto = (
    function(){
        function successS3Object(listS3,contratoId){
            const url= "https://demo-rappipay-s3.s3.amazonaws.com/";
            var list = [];
            var listS3=listS3.filter(x => x.Size!=0);
            var idnum=1;
            listS3.map(x => list.push({"id":idnum,"date":x.LastModified, "urlPDF": url.concat(x.Key)}))
            return list;
        }
        return{
            getExtractos(contratoId){

                AWS.config.update({accessKeyId: 'AKIAVFHJMDPBUAIK7CEO',
                                    secretAccessKey: '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',
                                    region: 'us-east-1'
                })
                var s3 = new AWS.S3()
                const myBucket = 'demo-rappipay-s3'
                var bucketParams = {
                  Bucket : myBucket,
                  Prefix: contratoId.trim().concat('/')
                };
                s3.listObjectsV2(bucketParams, function(err, data) {
                  if (err) {
                    console.log("Error", err);
                    return null;
                  } else {
                    console.log("Success", data);
                    if(data.Contents.length>1){
                        return successS3Object(data.Contents);
                    }
                    return [];
                  }
                });
            }
        };
    }
());