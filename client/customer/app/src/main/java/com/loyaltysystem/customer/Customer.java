package com.loyaltysystem.customer;

import android.os.AsyncTask;
import android.util.Log;

import com.loyaltysystem.auth.Auth;
import com.loyaltysystem.base.Base;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

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
        Auth.DoAuthResponse dar = LoyaltySys.authenticate(username, password);
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
    Auth.UserAuth auth;
    Base.Customer profile;


    private class AwaitTask extends AsyncTask<Void, Void, ConsumerClient.AwaitRsp> {

        ActionReceiver receiver;
        Iterator<ConsumerClient.AwaitRsp> responses;

        public AwaitTask(Iterator<ConsumerClient.AwaitRsp> responses, ActionReceiver ar) {
            receiver = ar;
            this.responses = responses;
        }

        protected ConsumerClient.AwaitRsp doInBackground(Void... urls) {
            while(responses.hasNext()){
                ConsumerClient.AwaitRsp arsp = responses.next();
                System.err.println("Received response "+arsp.toString());
                if(arsp.getAction()){
                    return arsp;
                }
            }
            return null;
        }

        protected void onPostExecute(ConsumerClient.AwaitRsp result) {
            receiver.onAction(result);
        }
    }

    public void awaitAction(ActionReceiver ar) {
        new AwaitTask(client.awaitTransaction(ConsumerClient.AwaitReq.newBuilder().setUserId(auth.getId()).build()),
                ar).execute();
    }


    public static interface ActionReceiver {
        void onAction(ConsumerClient.AwaitRsp rsp);
    }

    public List<Balance> getBalances() {
        ConsumerClient.Balances resp = client.getBalances(
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
}
