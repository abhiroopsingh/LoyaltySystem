package com.loyaltysystem.customer;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.GridLayoutManager;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import com.loyaltysystem.base.Base;

import java.util.List;

public class BalancesDemo extends AppCompatActivity {


    BalancesCards.BalancesAdapter adapter;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_balances_demo);

        Button earn = ((Button)findViewById(R.id.earnButton));
        earn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                BalancesDemo.this.startActivity(new Intent(getApplicationContext(), ShowBarcodeActivity.class));
            }
        });
        adapter = new BalancesCards.BalancesAdapter(balances());
        RecyclerView rv = (RecyclerView)findViewById(R.id.my_recycler_view);
        rv.setAdapter(adapter);

        RecyclerView.LayoutManager mLayoutManager = new LinearLayoutManager(this);
        rv.setLayoutManager(mLayoutManager);

    }

    @Override
    protected void onPostResume() {
        super.onPostResume();
        updateBalances();
    }

    public void updateBalances(){
        adapter.balances.clear();
        adapter.balances.addAll(balances());
        adapter.notifyDataSetChanged();
    }
    public List<Customer.Balance> balances(){
        return Customer.get().getBalances();
    }
}
