package com.loyaltysystem.pointofsale;

import android.content.Intent;
import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.google.common.io.BaseEncoding;
import com.google.protobuf.InvalidProtocolBufferException;
import com.loyaltysystem.customer.ConsumerClient;

public class ScanUserActivity extends AppCompatActivity {


    Button exec;
    EditText points;
    TextView name;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_scan_user);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        name = (TextView)findViewById(R.id.awardingName);
        points = (EditText)findViewById(R.id.pointsEdit);
        exec = (Button)findViewById(R.id.execAward);



        BarcodeHandler.startScan(this);

    }

    protected void accrueUser(final ConsumerClient.CustomerIdentifier customer){

        int pointN = getIntent().getExtras().getInt("points");
        PointOfSale.get().accrue((int)customer.getCustomer().getId(), pointN);

        Toast.makeText(ScanUserActivity.this,
                "Awarded customer "+customer.getCustomer().getName()+" "+pointN+" points.",
                Toast.LENGTH_LONG).show();
        finish();
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        String bc = BarcodeHandler.onActivityResult(requestCode, resultCode, data);
        if(bc.equals(BarcodeHandler.CANCEL)){
            Toast.makeText(this, "Cancelled", Toast.LENGTH_SHORT).show();
        }
        if(bc.equals(BarcodeHandler.OTHER)){
            return;
        }

        System.err.println("~~~:"+bc);
        try {

            byte[] decoded = BaseEncoding.base64().decode(bc);
            ConsumerClient.CustomerIdentifier ident = ConsumerClient.CustomerIdentifier.parseFrom(decoded);
            System.err.println(ident.toString());
            accrueUser(ident);
        } catch (InvalidProtocolBufferException e) {
            e.printStackTrace();
        }
    }

}
