package com.loyaltysystem.pointofsale;

import android.graphics.Point;
import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        final PointOfSale pos = new PointOfSale("testbusiness", "password");

        Button accrue = (Button)findViewById(R.id.accrue_button);
        final EditText amt = (EditText)findViewById(R.id.pointsbox);
        final EditText cust = (EditText)findViewById(R.id.customerbox);

        accrue.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                pos.accrue(Integer.parseInt(cust.getText().toString()), Integer.parseInt(amt.getText().toString()));
            }
        });
    }

}
