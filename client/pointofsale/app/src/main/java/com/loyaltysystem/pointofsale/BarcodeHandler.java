package com.loyaltysystem.pointofsale;

import android.app.Activity;
import android.content.Intent;
import android.net.Uri;

import static android.app.Activity.RESULT_CANCELED;
import static android.app.Activity.RESULT_OK;

/**
 * Created by gcolella on 11/14/16.
 */

public class BarcodeHandler {
    public static final int SCAN_INTENT = 94;
    public static final String OTHER = "OTHER";
    public static final String CANCEL = "CANCEL";

    public static void startScan(Activity act) {
        try {
            Intent intent = new Intent("com.google.zxing.client.android.SCAN");
            intent.putExtra("SCAN_MODE", "QR_CODE_MODE"); // "PRODUCT_MODE for bar codes
            intent.putExtra("RESULT_DISPLAY_DURATION_MS", 0L);
            intent.putExtra("SCAN_WIDTH", 3000);
            intent.putExtra("SCAN_HEIGHT", 10000);

            act.startActivityForResult(intent, SCAN_INTENT);

        } catch (Exception e) {

            Uri marketUri = Uri.parse("market://details?id=com.google.zxing.client.android");
            Intent marketIntent = new Intent(Intent.ACTION_VIEW, marketUri);
            act.startActivity(marketIntent);

        }
    }

    public static String onActivityResult(int requestCode, int resultCode, Intent data) {
        if (requestCode == SCAN_INTENT) {

            if (resultCode == RESULT_OK) {
                String contents = data.getStringExtra("SCAN_RESULT");
                return contents;
            }
            if(resultCode == RESULT_CANCELED){
                //handle cancel
                return CANCEL;
            }
        }
        return OTHER;
    }
}
