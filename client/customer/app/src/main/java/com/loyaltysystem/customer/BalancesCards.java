package com.loyaltysystem.customer;

import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.net.Uri;
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

import java.io.IOException;
import java.net.URL;
import java.util.List;

/**
 * Created by gcolella on 11/14/16.
 */

public class BalancesCards {
    static final int REDEEM_POINTS = 100;

    static class BalanceCardViewHolder extends RecyclerView.ViewHolder {

        public CardView myCard;
        TextView text, points;
        ImageView image;
        ProgressBar pbar;
        Button redeemButton;
        public BalanceCardViewHolder(CardView v) {
            super(v);
            myCard = v;

            text = (TextView)myCard.findViewById(R.id.business_name);
            points = (TextView)myCard.findViewById(R.id.point_balance);
            image = (ImageView)myCard.findViewById(R.id.business_image);
            pbar = (ProgressBar)myCard.findViewById(R.id.point_progress);
            redeemButton = (Button)myCard.findViewById(R.id.redeembutton);
        }
    }

    static class BalancesAdapter extends RecyclerView.Adapter<BalanceCardViewHolder> {

        List<Customer.Balance> balances;
        View.OnClickListener earnClicked;
        public BalancesAdapter(List<Customer.Balance> balances, View.OnClickListener earnClicked) {
            super();
            this.balances = balances;
            earnClicked = earnClicked;
        }

        @Override
        public BalanceCardViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {

            View v = LayoutInflater.from(parent.getContext())
                    .inflate(R.layout.balance_card, parent, false);
            BalanceCardViewHolder bh = new BalanceCardViewHolder((CardView)v);
            return bh;
        }

        @Override
        public void onBindViewHolder(BalanceCardViewHolder holder, int position) {
            Customer.Balance ab = balances.get(position);
            holder.text.setText(ab.businessName);
            holder.points.setText(ab.balance+" points");
            holder.pbar.setMax(REDEEM_POINTS);
            if(ab.balance < REDEEM_POINTS) {
                holder.pbar.setProgress(ab.balance);
                holder.redeemButton.setEnabled(false);
            } else {
                holder.redeemButton.setEnabled(true);
                holder.pbar.setProgress(REDEEM_POINTS);
            }

            holder.redeemButton.setOnClickListener(earnClicked);

            BarcodeHandler.loadImage(ab.businessThumbnail, holder.image);
        }

        @Override
        public int getItemCount() {
            return balances.size();
        }
    }

}
