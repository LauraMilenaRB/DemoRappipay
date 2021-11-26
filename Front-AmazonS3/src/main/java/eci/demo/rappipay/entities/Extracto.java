package eci.demo.rappipay.entities;

import java.io.File;
import java.util.Date;

public class Extracto {
    private Integer id =null;
    private Date date=null;
    private File pdf=null;

    public Extracto() {
    }

    public Extracto(Integer id, Date date, File pdf) {
        this.id=id;
        this.date=date;
        this.pdf=pdf;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public Date getDate() {
        return date;
    }

    public void setDate(Date date) {
        this.date = date;
    }

    public File getPdf() {
        return pdf;
    }

    public void setPdf(File pdf) {
        this.pdf = pdf;
    }
}
