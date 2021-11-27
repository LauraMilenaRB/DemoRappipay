package eci.demo.rappipay.impl;

import com.amazonaws.AmazonServiceException;
import com.amazonaws.auth.AWSCredentials;
import com.amazonaws.auth.AWSStaticCredentialsProvider;
import com.amazonaws.auth.BasicAWSCredentials;
import com.amazonaws.regions.Regions;
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3ClientBuilder;
import com.amazonaws.services.s3.model.*;
import eci.demo.rappipay.entities.Extracto;
import eci.demo.rappipay.services.ExtractoService;
import org.apache.commons.io.FileUtils;
import org.apache.commons.io.IOUtils;
import org.springframework.stereotype.Service;
import java.io.File;
import java.io.IOException;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.Files;

@Service
public class ExtractoServiceImpl implements ExtractoService {

    private String bucketName = "demo-rappipay-s3";
    private AWSCredentials credentials = new BasicAWSCredentials("AKIAVFHJMDPBUAIK7CEO", "zt9D0XyQ2sQWCpRezhvLnwqNAbUOSf1KGh8vziDG");
    private ArrayList<Extracto> listExtractos = new ArrayList<Extracto>();

    @Override
    public ArrayList<Extracto> getExtractos(Integer contratoId) throws IOException {
        S3Object fullObject = null, objectPortion = null, headerOverrideObject = null;

        try {
            AmazonS3 s3client = AmazonS3ClientBuilder
                    .standard()
                    .withCredentials(new AWSStaticCredentialsProvider(credentials))
                    .withRegion(Regions.US_EAST_1)
                    .build();

            ListObjectsV2Request listObjectsRequest = new ListObjectsV2Request().withBucketName(bucketName)
                    .withPrefix(contratoId+"/").withDelimiter("/");
            ListObjectsV2Result listing = s3client.listObjectsV2(listObjectsRequest);

            Integer id=1;
            for (S3ObjectSummary summary : listing.getObjectSummaries()) {
                String folderFilename = summary.getKey();
                String[] file = folderFilename.split("\\/");
                if (file.length > 1) {
                    String dateString= file[1].split("-")[1].split("\\.")[0];
                    SimpleDateFormat newDateFormat = new SimpleDateFormat("yyyyMMdd");
                    Date myDate = newDateFormat.parse(dateString);
                    newDateFormat.applyPattern("yyyy-MM-dd");
                    String myDateString = newDateFormat.format(myDate);
                    S3Object s3object = s3client.getObject(bucketName, summary.getKey());
                    S3ObjectInputStream inputStream = s3object.getObjectContent();
                    //File newFile= new File("src/main/resources/static/generateFiles/" + file[1]);
                    //FileUtils.copyInputStreamToFile(inputStream, newFile);
                    listExtractos.add(new Extracto(id,file[1],myDateString, IOUtils.toByteArray(inputStream)));
                    id+=1;
                }
            }
        } catch (AmazonServiceException | IOException | ParseException e) {
            e.printStackTrace();
        } finally {
            if (fullObject != null) {
                fullObject.close();
            }
            if (objectPortion != null) {
                objectPortion.close();
            }
            if (headerOverrideObject != null) {
                headerOverrideObject.close();
            }
        }
        return listExtractos;
    }

}
