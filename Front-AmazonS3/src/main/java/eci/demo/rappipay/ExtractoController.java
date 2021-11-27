package eci.demo.rappipay;

import java.util.ArrayList;
import eci.demo.rappipay.entities.Extracto;
import eci.demo.rappipay.services.ExtractoService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.beans.factory.annotation.Autowired;


@RestController
public class ExtractoController {

    @Autowired
    private ExtractoService extractoService;

    @RequestMapping(value="/extractos")
    public ResponseEntity<ArrayList<Extracto>> getExtractos(@RequestBody Integer contratoId) {
        try {
            ArrayList<Extracto> result=extractoService.getExtractos(contratoId);
            //System.out.println("pruebaresultado"+result.get(0).getPdf());
            return new ResponseEntity<>(result, HttpStatus.ACCEPTED);
        } catch (Exception ex) {
            ex.printStackTrace();
            return new ResponseEntity<>(new ArrayList<>(), HttpStatus.BAD_REQUEST);
        }
    }

}