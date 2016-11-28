package com.loyaltysystem.customer;

import android.support.v7.widget.CardView;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.ProgressBar;
import android.widget.TextView;

import com.loyaltysystem.base.Base;
import com.loyaltysystem.transactions.TransactionsOuterClass;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

/**
 * Created by gcolella on 11/28/16.
 */

public class HistoryCards {

    static class HistoryCardViewHolder extends RecyclerView.ViewHolder {

        public CardView myCard;
        TextView text, points, time;
        ImageView image;

        public HistoryCardViewHolder(CardView v) {
            super(v);
            myCard = v;

            text = (TextView)myCard.findViewById(R.id.business_name);
            points = (TextView)myCard.findViewById(R.id.point_change);
            image = (ImageView)myCard.findViewById(R.id.business_image);
            time = (TextView)myCard.findViewById(R.id.transaction_time);

        }
    }

    static class HistoryAdapter extends RecyclerView.Adapter<HistoryCardViewHolder> {

        List<TransactionsOuterClass.Transaction> transactions;
        View.OnClickListener earnClicked;
        public HistoryAdapter(List<TransactionsOuterClass.Transaction> transactions) {
            super();
            this.transactions = new ArrayList<>(transactions);
        }

        @Override
        public HistoryCardViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {

            View v = LayoutInflater.from(parent.getContext())
                    .inflate(R.layout.history_card, parent, false);
            HistoryCardViewHolder h = new HistoryCardViewHolder((CardView)v);
            return h;
        }

        @Override
        public void onBindViewHolder(HistoryCardViewHolder holder, int position) {
            TransactionsOuterClass.Transaction t = transactions.get(position);

            BarcodeHandler.loadImage(t.getBusiness().getThumbnailurl(), holder.image);
            holder.text.setText(t.getBusiness().getName());
            if(t.getPointChange() > 0){
                holder.points.setText(""+t.getPointChange());
                holder.points.setTextColor(holder.points.getResources().getColor(R.color.green));
            } else {
                holder.points.setTextColor(holder.points.getResources().getColor(R.color.colorPrimaryDark));
                holder.points.setText("Spent "+ -t.getPointChange());
            }

            Date d = new Date(t.getTimeMs()*1000);
            holder.time.setText(d.toLocaleString());
        }

        @Override
        public int getItemCount() {
            return transactions.size();
        }
    }




}
