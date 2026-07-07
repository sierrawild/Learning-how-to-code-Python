package com.familytimer.app;

import android.app.Activity;
import android.graphics.Color;
import android.os.Bundle;
import android.view.Gravity;
import android.view.Window;
import android.view.WindowManager;
import android.widget.LinearLayout;
import android.widget.TextView;

public class TimeUpActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        requestWindowFeature(Window.FEATURE_NO_TITLE);
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN, WindowManager.LayoutParams.FLAG_FULLSCREEN);
        if (android.os.Build.VERSION.SDK_INT >= 27) {
            setShowWhenLocked(true);
            setTurnScreenOn(true);
        }

        LinearLayout root = new LinearLayout(this);
        root.setOrientation(LinearLayout.VERTICAL);
        root.setGravity(Gravity.CENTER);
        root.setPadding(36, 36, 36, 36);
        root.setBackgroundColor(Color.rgb(15, 23, 42));

        TextView title = new TextView(this);
        title.setText("Time's up");
        title.setTextColor(Color.WHITE);
        title.setTextSize(44);
        title.setGravity(Gravity.CENTER);

        TextView message = new TextView(this);
        message.setText("Please finish what you are doing and bring the tablet to a parent.");
        message.setTextColor(Color.rgb(226, 232, 240));
        message.setTextSize(22);
        message.setGravity(Gravity.CENTER);
        message.setPadding(0, 24, 0, 0);

        root.addView(title);
        root.addView(message);
        setContentView(root);
    }
}
