package edu.aygo.logservice;

import com.google.gson.Gson;

import static spark.Spark.*;

public class Api {

    //public static user cadenaService = new CadenaService();
    /*http://localhost:8080/cadena/hola*/
    public static void main(String[] args){
        Gson gson = new Gson();
        port(getPort());

        get("/", (req, res) -> {
            return "hello from sparkjava.com";
        });

        get("/cadena/:valor", (req, res) -> {
            res.type("application/json");
            return null;//cadenaService.addCadena(req.params(":valor"));
        },gson ::toJson);
    }

    private static int getPort() {
        if (System.getenv("PORT") != null) {
            return Integer.parseInt(System.getenv("PORT"));
        }
        return 4567;
    }
}