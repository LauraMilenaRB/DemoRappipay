package eci.aygo.load;

import java.util.logging.Level;
import java.util.logging.Logger;

import java.net.URI;
import org.apache.http.HttpEntity;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClientBuilder;
import org.apache.http.util.EntityUtils;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;


@RestController
public class BalanceController {
    String client1 = "http://172.17.0.1:34001/cadena/";
    String client2 = "http://172.17.0.1:34002/cadena/";
    String client3 = "http://172.17.0.1:34003/cadena/";

    private String loadbalancer(){
        String urlClient = "";
        if(BalanceApplication.cliente == 1){
            urlClient = client1;
            BalanceApplication.cliente = 2;
        }
        else if(BalanceApplication.cliente == 2){
            urlClient = client2;
            BalanceApplication.cliente = 3;
        }
        else{
            urlClient = client3;
            BalanceApplication.cliente = 1;
        }
        return urlClient;
    }

    @RequestMapping(value="/loadbalancer")
    public ResponseEntity<String> addCadena(@RequestBody String cadena) {
        String stringurl = loadbalancer()+cadena;
        System.out.println("SOLICITUD A: "+stringurl);
        try {
            CloseableHttpClient httpClient = HttpClientBuilder.create().build();
            try {
                HttpGet request = new HttpGet(stringurl);
                CloseableHttpResponse respuesta = httpClient.execute(request);
                HttpEntity entity = respuesta.getEntity();
                String responseString = EntityUtils.toString(entity, "UTF-8");
                System.out.println("Respuesta: "+responseString);
                return new ResponseEntity<String>(responseString, HttpStatus.ACCEPTED);
            } catch (Exception ex) {
                return new ResponseEntity<String>(ex.getLocalizedMessage(), HttpStatus.NOT_FOUND);
            } finally {
                httpClient.close();
            }
        } catch (Exception ex) {
            Logger.getLogger(BalanceController.class.getName()).log(Level.SEVERE, null, ex);
            return new ResponseEntity<String>(ex.getLocalizedMessage(), HttpStatus.NOT_FOUND);
        }
    }
}