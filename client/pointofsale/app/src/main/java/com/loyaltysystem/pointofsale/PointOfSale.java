package com.loyaltysystem.pointofsale;

import com.loyaltysystem.auth.Auth;
import com.loyaltysystem.base.Base;

/**
 * Created by gcolella on 10/31/16.
 */

public class PointOfSale {

    PointOfSaleGrpc.PointOfSaleBlockingStub client;
    Auth.UserAuth savedAuth;

    public PointOfSale(String username, String password){
        client = LoyaltySys.Connect();
        savedAuth = LoyaltySys.authenticate(username, password);
    }

    public boolean accrue(int userId, int points) {
        return client.accrue(PosClient.AccrualRequest.newBuilder()
                .setBusinessId(savedAuth.getAuthorizedBusiness())
                .setCustomerId(userId)
                .setPointAmount(points).build()
        ).getSuccess();
    }

}
