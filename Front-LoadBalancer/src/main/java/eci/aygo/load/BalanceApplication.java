package eci.aygo.load;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;


@SpringBootApplication
public class BalanceApplication {

    public static int cliente = 1;

    public static void main(String[] args)throws Exception {
        SpringApplication.run(BalanceApplication.class, args);
    }
}