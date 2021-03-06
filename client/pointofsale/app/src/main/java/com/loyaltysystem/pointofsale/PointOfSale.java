package com.loyaltysystem.pointofsale;

import com.loyaltysystem.auth.Auth;
import com.loyaltysystem.base.Base;

/**
 * Created by gcolella on 10/31/16.
 */

public class PointOfSale {

    private static PointOfSale pos;

    public static PointOfSale get() {
        return pos;
    }

    public static boolean login(String username, String password){
        pos = new PointOfSale(username, password);
        return true; // TODO(gcolella): check the authentication result here.
    }

    PointOfSaleGrpc.PointOfSaleBlockingStub client;
    Auth.UserAuth savedAuth;
    Base.Customer profile;

    public PointOfSale(String username, String password){
        client = LoyaltySys.Connect();
        Auth.DoAuthResponse dar = LoyaltySys.authenticate(username, password);
        savedAuth = dar.getAuth();
        profile = dar.getCustomer();
    }

    public boolean accrue(int userId, int points) {
        return client.accrue(PosClient.AccrualRequest.newBuilder()
                .setBusinessId(savedAuth.getAuthorizedBusiness())
                .setCustomerId(userId)
                .setPointAmount(points).build()
        ).getSuccess();
    }

    public PosClient.BusinessInfo businessInfo(long business) {
        return client.getBusinessInfo(PosClient.InfoReq.newBuilder().setId(business).build());
    }

}
