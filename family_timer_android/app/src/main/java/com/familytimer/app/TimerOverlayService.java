package com.familytimer.app;

import android.app.Notification;
import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.app.Service;
import android.app.admin.DevicePolicyManager;
import android.content.ComponentName;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Color;
import android.graphics.PixelFormat;
import android.os.Build;
import android.os.CountDownTimer;
import android.os.IBinder;
import android.provider.Settings;
import android.view.Gravity;
import android.view.WindowManager;
import android.widget.LinearLayout;
import android.widget.TextView;

import java.util.Locale;

public class TimerOverlayService extends Service {
    public static final String EXTRA_SECONDS = "seconds";
    public static final String EXTRA_MESSAGE = "message";
    private static final String CHANNEL_ID = "timer_overlay";

    private WindowManager windowManager;
    private LinearLayout overlay;
    private TextView timeView;
    private CountDownTimer timer;

    @Override
    public void onCreate() {
        super.onCreate();
        createChannel();
        startForeground(11, notification("Timer is visible"));
        windowManager = (WindowManager) getSystemService(WINDOW_SERVICE);
    }

    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        int seconds = intent != null ? intent.getIntExtra(EXTRA_SECONDS, 60) : 60;
        String message = intent != null ? intent.getStringExtra(EXTRA_MESSAGE) : "Time to finish this game";
        if (message == null || message.trim().isEmpty()) {
            message = "Time to finish this game";
        }
        showOverlay(Math.max(1, seconds), message);
        return START_NOT_STICKY;
    }

    private void showOverlay(int seconds, String message) {
        if (Build.VERSION.SDK_INT >= 23 && !Settings.canDrawOverlays(this)) {
            return;
        }
        removeOverlay();

        overlay = new LinearLayout(this);
        overlay.setOrientation(LinearLayout.VERTICAL);
        overlay.setGravity(Gravity.CENTER);
        overlay.setPadding(28, 20, 28, 20);
        overlay.setBackgroundResource(com.familytimer.app.R.drawable.rounded_timer_panel);

        TextView messageView = new TextView(this);
        messageView.setText(message);
        messageView.setTextColor(Color.rgb(15, 23, 42));
        messageView.setTextSize(18);
        messageView.setGravity(Gravity.CENTER);

        timeView = new TextView(this);
        timeView.setTextColor(Color.rgb(190, 24, 93));
        timeView.setTextSize(42);
        timeView.setGravity(Gravity.CENTER);
        timeView.setPadding(0, 8, 0, 0);

        overlay.addView(messageView);
        overlay.addView(timeView);

        int type = Build.VERSION.SDK_INT >= 26
                ? WindowManager.LayoutParams.TYPE_APPLICATION_OVERLAY
                : WindowManager.LayoutParams.TYPE_PHONE;
        WindowManager.LayoutParams params = new WindowManager.LayoutParams(
                WindowManager.LayoutParams.WRAP_CONTENT,
                WindowManager.LayoutParams.WRAP_CONTENT,
                type,
                WindowManager.LayoutParams.FLAG_NOT_FOCUSABLE
                        | WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON
                        | WindowManager.LayoutParams.FLAG_LAYOUT_IN_SCREEN,
                PixelFormat.TRANSLUCENT);
        params.gravity = Gravity.TOP | Gravity.CENTER_HORIZONTAL;
        params.y = 70;
        windowManager.addView(overlay, params);

        timer = new CountDownTimer(seconds * 1000L, 1000L) {
            @Override
            public void onTick(long millisUntilFinished) {
                timeView.setText(formatTime((int) Math.ceil(millisUntilFinished / 1000.0)));
            }

            @Override
            public void onFinish() {
                timeView.setText("TIME'S UP");
                openTimeUpScreen();
                maybeLockTablet();
            }
        };
        timer.start();
    }

    private String formatTime(int totalSeconds) {
        int minutes = totalSeconds / 60;
        int seconds = totalSeconds % 60;
        return String.format(Locale.UK, "%02d:%02d", minutes, seconds);
    }

    private void openTimeUpScreen() {
        Intent intent = new Intent(this, TimeUpActivity.class);
        intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_CLEAR_TOP);
        startActivity(intent);
    }

    private void maybeLockTablet() {
        SharedPreferences prefs = getSharedPreferences(MainActivity.PREFS, MODE_PRIVATE);
        if (!prefs.getBoolean(MainActivity.KEY_LOCK_ON_FINISH, false)) {
            return;
        }

        DevicePolicyManager manager = (DevicePolicyManager) getSystemService(Context.DEVICE_POLICY_SERVICE);
        ComponentName admin = new ComponentName(this, TimerDeviceAdminReceiver.class);
        if (manager != null && manager.isAdminActive(admin)) {
            manager.lockNow();
        }
    }

    private Notification notification(String text) {
        Notification.Builder builder = Build.VERSION.SDK_INT >= 26
                ? new Notification.Builder(this, CHANNEL_ID)
                : new Notification.Builder(this);
        return builder
                .setContentTitle("Family Timer")
                .setContentText(text)
                .setSmallIcon(android.R.drawable.ic_lock_idle_alarm)
                .setOngoing(true)
                .build();
    }

    private void createChannel() {
        if (Build.VERSION.SDK_INT >= 26) {
            NotificationChannel channel = new NotificationChannel(
                    CHANNEL_ID,
                    "Floating timer",
                    NotificationManager.IMPORTANCE_LOW);
            getSystemService(NotificationManager.class).createNotificationChannel(channel);
        }
    }

    private void removeOverlay() {
        if (timer != null) {
            timer.cancel();
            timer = null;
        }
        if (overlay != null) {
            windowManager.removeView(overlay);
            overlay = null;
        }
    }

    @Override
    public void onDestroy() {
        removeOverlay();
        super.onDestroy();
    }

    @Override
    public IBinder onBind(Intent intent) {
        return null;
    }
}
