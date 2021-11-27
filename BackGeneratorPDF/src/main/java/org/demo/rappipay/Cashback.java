package org.demo.rappipay;

import org.mongodb.morphia.annotations.Entity;
import org.mongodb.morphia.annotations.Id;
import org.mongodb.morphia.annotations.Property;
import java.sql.Timestamp;

@Entity ( "Cashback" )
public class Cashback {

    @Id
    private Integer id;
    @Property ( "value" )
    private String value;
    @Property ( "dateRegister" )
    private Timestamp dateRegister;



    public Cashback(Integer id,String val, Timestamp date){
        this.id=id;
        value=val;
        dateRegister=date;
    }

    public Cashback(){
    }

    public String getValue() {
        return value;
    }

    public Timestamp getDateRegister() {
        return dateRegister;
    }
}
