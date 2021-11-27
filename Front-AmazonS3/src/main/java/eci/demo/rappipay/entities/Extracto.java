package eci.demo.rappipay.entities;

import java.util.Date;

public class Extracto {

    private Integer id =null;
    private String name=null;
    private String date=null;
    private byte[] pdf=null;

    public Extracto() {
    }

    public Extracto(Integer id,String name, String date, byte[] pdf) {
        this.id=id;
        this.date=date;
        this.pdf=pdf;
        this.name=name;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }

    public byte[] getPdf() {
        return pdf;
    }

    public void setPdf(byte[] pdf) {
        this.pdf = pdf;
    }

    public String getName() {return name;}

    public void setName(String name) {this.name = name;}
}
