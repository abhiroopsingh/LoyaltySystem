package com.loyaltysystem.customer;

import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.AsyncTask;
import android.util.Log;
import android.widget.ImageView;

import com.google.common.io.BaseEncoding;
import com.google.zxing.BarcodeFormat;
import com.google.zxing.MultiFormatWriter;
import com.google.zxing.WriterException;
import com.google.zxing.common.BitMatrix;

import java.io.InputStream;

import static android.graphics.Color.BLACK;
import static android.graphics.Color.WHITE;

/**
 * Created by gcolella on 11/13/16.
 */

public class BarcodeHandler {


    public static void loadQrCode(ConsumerClient.CustomerIdentifier ident, ImageView view) {
        String cont = BaseEncoding.base64().encode(ident.toByteArray());
        loadQrCode(cont, view);
    }

    static int WIDTH = 400;
    public static void loadQrCode(String codeContents, ImageView view){
        DownloadImageTask dit = new DownloadImageTask(view);
        System.out.println("CODE:"+codeContents);
        String url = "https://chart.googleapis.com/chart?cht=qr&chs="+WIDTH+"x"+WIDTH+"&chl="+codeContents;
        dit.execute(url);
    }
    
    public static void loadImage(String url, ImageView view) {
        DownloadImageTask dit = new DownloadImageTask(view);
        dit.execute(url);
    }


    private static class DownloadImageTask extends AsyncTask<String, Void, Bitmap> {
        ImageView bmImage;

        public DownloadImageTask(ImageView bmImage) {
            this.bmImage = bmImage;
        }

        protected Bitmap doInBackground(String... urls) {
            String urldisplay = urls[0];
            Bitmap mIcon11 = null;
            try {
                InputStream in = new java.net.URL(urldisplay).openStream();
                mIcon11 = BitmapFactory.decodeStream(in);
            } catch (Exception e) {
                Log.e("Error", e.getMessage());
                e.printStackTrace();
            }
            return mIcon11;
        }

        protected void onPostExecute(Bitmap result) {
            bmImage.setImageBitmap(result);
        }
    }
}
