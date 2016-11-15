package com.loyaltysystem.pointofsale;

import com.loyaltysystem.auth.Auth;
import com.loyaltysystem.auth.LoginGrpc;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;

/**
 * Created by gcolella on 10/31/16.
 */

public class LoyaltySys {

    static final String HOST = "104.236.205.162";
    static final int PORT = 50051;


    public static PointOfSaleGrpc.PointOfSaleBlockingStub Connect(){
        ManagedChannel mc = ManagedChannelBuilder.forAddress(HOST, PORT).usePlaintext(true).build();
        PointOfSaleGrpc.PointOfSaleBlockingStub pos = PointOfSaleGrpc.newBlockingStub(mc);
        return pos;
    }

    public static Auth.DoAuthResponse authenticate(String username, String password) {
        ManagedChannel mc = ManagedChannelBuilder.forAddress(HOST, PORT).usePlaintext(true).build();
        LoginGrpc.LoginBlockingStub login = LoginGrpc.newBlockingStub(mc);

        // Start the authentication flow and recieve a challenge from the server.
        Auth.StartAuthResponse started = login.startAuth(
                Auth.StartAuthRequest.newBuilder().setUsername(username).build());

        String hashed = hash(password, started.getNonce());

        Auth.DoAuthResponse resp = login.doAuth(
                Auth.DoAuthRequest.newBuilder().setHashToken(hashed).setId(started.getId()).build()
        );

        if(!resp.getSuccess()) {
            System.err.println("DID NOT AUTHENTICATE.");
        }

        return resp;
    }


    private static String hash(String password, String nonce) {
        try {
            // Hash the password.
            MessageDigest md = MessageDigest.getInstance("SHA-256");
            md.update(password.getBytes());

            // Then add the salt.
            MessageDigest salted = MessageDigest.getInstance("SHA-256");
            salted.update(nonce.getBytes());
            salted.update(md.digest());

            return new String(salted.digest());


        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
            throw new RuntimeException(e);
        }
    }
}
