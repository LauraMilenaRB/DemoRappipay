package eci.demo.rappipay.services;

import eci.demo.rappipay.entities.Extracto;
import java.io.IOException;
import java.util.ArrayList;

public interface ExtractoService {
    ArrayList<Extracto> getExtractos(Integer contratoId) throws IOException;
}
