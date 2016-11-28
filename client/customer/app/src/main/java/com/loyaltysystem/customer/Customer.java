package com.loyaltysystem.customer;

import android.os.AsyncTask;
import android.util.Log;
import android.util.Pair;

import com.loyaltysystem.auth.Auth;
import com.loyaltysystem.base.Base;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.Executors;
import java.util.concurrent.ThreadPoolExecutor;

import io.grpc.CallOptions;
import io.grpc.Channel;
import io.grpc.ClientCall;
import io.grpc.ManagedChannel;
import io.grpc.Metadata;
import io.grpc.Status;
import io.grpc.okhttp.Headers;
import io.grpc.stub.ClientCallStreamObserver;
import io.grpc.stub.ClientCalls;
import io.grpc.stub.ClientResponseObserver;

/**
 * Created by gcolella on 10/31/16.
 */

public class Customer {

    private static Customer cust;

    public static boolean login(String username, String password){
        cust = new Customer(username, password);
        return true; //TODO(gcolella) check result.
    }

    public static Customer get(){
        return cust;
    }


    public Customer(String username, String password) {
        this.username = username;
        Pair<Auth.DoAuthResponse, ManagedChannel> p = LoyaltySys.authenticate(username, password);
        Auth.DoAuthResponse dar = p.first;
        channel = p.second;
        auth = dar.getAuth();
        profile = dar.getCustomer();
        client = LoyaltySys.connectCustomer();
    }

    public ConsumerClient.CustomerIdentifier customer(){
        return ConsumerClient.CustomerIdentifier.
                newBuilder().setCustomer(profile).build();
    }

    String username;
    CustomerServerGrpc.CustomerServerBlockingStub client;
    ManagedChannel channel;
    Auth.UserAuth auth;
    Base.Customer profile;


    public Canceller awaitAction(final ActionReceiver ar) {
        System.out.println("Awaiting action!");


        CallOptions co = CallOptions.DEFAULT.withExecutor(Executors.newSingleThreadExecutor());
        final ClientCall<ConsumerClient.AwaitReq,ConsumerClient.AwaitRsp> cc =
                channel.newCall(CustomerServerGrpc.METHOD_AWAIT_TRANSACTION, co);

        ClientCalls.asyncServerStreamingCall(cc, ConsumerClient.AwaitReq.newBuilder().setUserId(Customer.get().auth.getId()).build(),
                new ClientResponseObserver<ConsumerClient.AwaitReq,ConsumerClient.AwaitRsp>() {
                    @Override
                    public void beforeStart(ClientCallStreamObserver requestStream) {

                    }

                    @Override
                    public void onNext(ConsumerClient.AwaitRsp value) {
                        System.out.println("GOT RESPONSE");
                        if(value.getAction()){
                            ar.onAction(value);
                        }
                    }

                    @Override
                    public void onError(Throwable t) {

                    }

                    @Override
                    public void onCompleted() {

                    }
                });


       // LoyaltySys.
        Canceller c = new Canceller() {
            @Override
            public void cancel() {
                cc.cancel("User cancelled", null);
            }
        };

        return c;
    }


    public interface ActionReceiver {
        void onAction(ConsumerClient.AwaitRsp rsp);
    }

    public List<Balance> getBalances() {
        ConsumerClient.Balances resp = null;

        resp = client.getBalances(
                ConsumerClient.BalanceRequest.newBuilder()
                        .setCustomerId(auth.getId())
                        .build());


        List<Balance> balances = new ArrayList<Balance>();
        for(Base.AccountBalance ab : resp.getBalancesList()){
            balances.add(new Balance(ab.getBusiness().getName(), ab.getBusiness().getThumbnailurl(), ab.getBusiness().getId(), ab.getPointBalance()));
        }
        return balances;
    }
    public class Balance {
        String businessName, businessThumbnail;
        long businessId;
        int balance;

        public Balance(String businessName, String businessThumbnail, long businessId, int balance) {
            this.businessName = businessName;
            this.businessId = businessId;
            this.balance = balance;
            this.businessThumbnail = businessThumbnail;
        }
    }

    public interface Canceller {
        void cancel();
    }
}
