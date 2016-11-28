package com.loyaltysystem.pointofsale;

import android.content.Intent;
import android.graphics.Point;
import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        TextView info = (TextView)findViewById(R.id.shopInfo);

        String businessName = PointOfSale.get().businessInfo(PointOfSale.get().savedAuth.getAuthorizedBusiness()).getName();
        info.setText(
                "Welcome, "+businessName+ " ("+PointOfSale.get().profile.getName() +")"
        );

        Button accrue = (Button)findViewById(R.id.accrue_button);

        accrue.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent myIntent = new Intent(MainActivity.this, ScanUserActivity.class);
                myIntent.putExtra("points", Integer.parseInt(
                        ((EditText)findViewById(R.id.pointsEdit)).getText().toString()));
                MainActivity.this.startActivity(myIntent);
            }
        });

        Button redeem = (Button)findViewById(R.id.redeem_button);
        redeem.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent myIntent = new Intent(MainActivity.this, ScanUserActivity.class);
                myIntent.putExtra("points", -100);
                MainActivity.this.startActivity(myIntent);
            }
        });


    }

}
