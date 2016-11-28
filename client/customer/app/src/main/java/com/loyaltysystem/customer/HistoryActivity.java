package com.loyaltysystem.customer;

import android.content.Intent;
import android.os.Build;
import android.os.Bundle;
import android.support.annotation.RequiresApi;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.support.v7.widget.Toolbar;
import android.view.View;

import com.loyaltysystem.transactions.TransactionsOuterClass;

import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class HistoryActivity extends AppCompatActivity {

    HistoryCards.HistoryAdapter adapter;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_history);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        adapter = new HistoryCards.HistoryAdapter(history());
        RecyclerView rv = (RecyclerView)findViewById(R.id.history_recycler);
        rv.setAdapter(adapter);

        RecyclerView.LayoutManager mLayoutManager = new LinearLayoutManager(this);
        rv.setLayoutManager(mLayoutManager);
    }

    private List<TransactionsOuterClass.Transaction> history(){
        return Customer.get().getTransactions();
    }

    public void onResume(){
        super.onResume();
        updateBalances();
    }

    public void updateBalances(){
        adapter.transactions.clear();
        adapter.transactions.addAll(history());
        Collections.sort(adapter.transactions, new Comparator<TransactionsOuterClass.Transaction>() {
            @RequiresApi(api = Build.VERSION_CODES.KITKAT)
            @Override
            public int compare(TransactionsOuterClass.Transaction transaction, TransactionsOuterClass.Transaction t1) {
                return Long.compare(t1.getTimeMs(), transaction.getTimeMs());
            }
        });
        adapter.notifyDataSetChanged();
    }

}
