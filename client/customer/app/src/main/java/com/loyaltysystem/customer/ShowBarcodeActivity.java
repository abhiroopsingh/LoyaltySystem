package com.loyaltysystem.customer;

import android.annotation.SuppressLint;
import android.content.Context;
import android.os.Vibrator;
import android.support.v7.app.ActionBar;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.os.Handler;
import android.view.MotionEvent;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.Toast;

/**
 * An example full-screen activity that shows and hides the system UI (i.e.
 * status bar and navigation/system bar) with user interaction.
 */
public class ShowBarcodeActivity extends AppCompatActivity {

    Customer.Canceller c;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_show_barcode);


    }

    @Override
    public void onPostResume(){
        super.onPostResume();
        loadQR();
    }

    @Override
    protected void onPause() {
        if(c != null){
            c.cancel();
        }
        super.onPause();
    }

    public void loadQR(){
        ImageView bc = (ImageView)findViewById(R.id.barcodeView);
        BarcodeHandler.loadQrCode(Customer.get().customer(), bc);

        Button cancel = (Button)findViewById(R.id.cancelButton);
        cancel.setOnClickListener(
                new View.OnClickListener() {
                    @Override
                    public void onClick(View view) {
                        finish();
                    }
                }
        );

        c = Customer.get().awaitAction(new Customer.ActionReceiver() {
            @Override
            public void onAction(ConsumerClient.AwaitRsp rsp) {
                if(rsp.getPointChange() > 0) {
                    Toast.makeText(ShowBarcodeActivity.this, "Earned " + rsp.getPointChange() + " from " + rsp.getBusinessName(), Toast.LENGTH_LONG).show();
                } else {
                    Toast.makeText(ShowBarcodeActivity.this, "Spent "+rsp.getPointChange()+" at "+rsp.getBusinessName(), Toast.LENGTH_LONG).show();
                }
                Vibrator v = (Vibrator) getApplicationContext().getSystemService(Context.VIBRATOR_SERVICE);
                // Vibrate for 500 milliseconds
                v.vibrate(500);

                finish();
            }
        });
    }
    @Override
    protected void onPostCreate(Bundle savedInstanceState) {
        super.onPostCreate(savedInstanceState);
    }
}
