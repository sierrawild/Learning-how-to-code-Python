package com.familytimer.app;

import android.Manifest;
import android.app.Activity;
import android.app.admin.DevicePolicyManager;
import android.content.ComponentName;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.content.pm.PackageManager;
import android.graphics.Color;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.provider.Settings;
import android.text.InputType;
import android.view.Gravity;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.ScrollView;
import android.widget.TextView;
import android.widget.Toast;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.Inet4Address;
import java.net.NetworkInterface;
import java.net.URL;
import java.net.URLEncoder;
import java.util.Collections;
import java.util.Locale;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class MainActivity extends Activity {
    static final String PREFS = "family_timer";
    static final String KEY_MODE = "mode";
    static final String MODE_PARENT = "parent";
    static final String MODE_CHILD = "child";
    static final String KEY_LOCK_ON_FINISH = "lock_on_finish";

    private final ExecutorService executor = Executors.newSingleThreadExecutor();
    private SharedPreferences prefs;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        prefs = getSharedPreferences(PREFS, MODE_PRIVATE);
        String mode = prefs.getString(KEY_MODE, "");
        if (MODE_PARENT.equals(mode)) {
            showParent();
        } else if (MODE_CHILD.equals(mode)) {
            showChild();
        } else {
            showModePicker();
        }
    }

    private void showModePicker() {
        LinearLayout root = baseLayout();
        root.addView(title("Family Timer"));
        root.addView(body("Use Parent Phone on your phone and Child Tablet on the Samsung tablet."));
        root.addView(button("Parent Phone", v -> {
            prefs.edit().putString(KEY_MODE, MODE_PARENT).apply();
            showParent();
        }));
        root.addView(button("Child Tablet", v -> {
            prefs.edit().putString(KEY_MODE, MODE_CHILD).apply();
            showChild();
        }));
        setContentView(scroll(root));
    }

    private void showParent() {
        LinearLayout root = baseLayout();
        root.addView(title("Parent Phone"));
        root.addView(body("Enter the tablet IP address shown on the tablet, then send a timer."));

        EditText ip = input("Tablet IP address, e.g. 192.168.1.42", InputType.TYPE_CLASS_TEXT);
        EditText minutes = input("Minutes", InputType.TYPE_CLASS_NUMBER);
        EditText message = input("Message, e.g. Time to finish this game", InputType.TYPE_CLASS_TEXT);
        message.setText("Time to finish this game");

        root.addView(ip);
        root.addView(minutes);
        root.addView(message);
        root.addView(button("Send Timer", v -> sendTimer(ip, minutes, message)));

        LinearLayout quick = new LinearLayout(this);
        quick.setOrientation(LinearLayout.HORIZONTAL);
        quick.setGravity(Gravity.CENTER);
        quick.addView(smallButton("5 min", v -> quickSend(ip, message, 5)));
        quick.addView(smallButton("10 min", v -> quickSend(ip, message, 10)));
        quick.addView(smallButton("15 min", v -> quickSend(ip, message, 15)));
        root.addView(quick);

        root.addView(button("Change Mode", v -> {
            prefs.edit().remove(KEY_MODE).apply();
            showModePicker();
        }));
        setContentView(scroll(root));
    }

    private void showChild() {
        startTimerServer();

        LinearLayout root = baseLayout();
        root.addView(title("Child Tablet"));
        root.addView(body("Keep both devices on the same Wi-Fi. Parent phones send timers to this tablet."));
        root.addView(label("Tablet IP address"));
        root.addView(body(getLocalIpAddress()));

        root.addView(button("Allow Floating Timer", v -> {
            Intent intent = new Intent(Settings.ACTION_MANAGE_OVERLAY_PERMISSION,
                    Uri.parse("package:" + getPackageName()));
            startActivity(intent);
        }));

        if (Build.VERSION.SDK_INT >= 33) {
            root.addView(button("Allow Notifications", v ->
                    requestPermissions(new String[]{Manifest.permission.POST_NOTIFICATIONS}, 30)));
        }

        CheckBox lockOnFinish = new CheckBox(this);
        lockOnFinish.setText("Lock tablet when timer ends");
        lockOnFinish.setTextSize(18);
        lockOnFinish.setChecked(prefs.getBoolean(KEY_LOCK_ON_FINISH, false));
        lockOnFinish.setOnCheckedChangeListener((buttonView, isChecked) ->
                prefs.edit().putBoolean(KEY_LOCK_ON_FINISH, isChecked).apply());
        root.addView(lockOnFinish);

        root.addView(button("Enable Lock Permission", v -> {
            ComponentName admin = new ComponentName(this, TimerDeviceAdminReceiver.class);
            Intent intent = new Intent(DevicePolicyManager.ACTION_ADD_DEVICE_ADMIN);
            intent.putExtra(DevicePolicyManager.EXTRA_DEVICE_ADMIN, admin);
            intent.putExtra(DevicePolicyManager.EXTRA_ADD_EXPLANATION,
                    "Family Timer can lock the tablet when time is up.");
            startActivity(intent);
        }));

        root.addView(button("Test 30 Second Timer", v -> {
            Intent intent = new Intent(this, TimerOverlayService.class);
            intent.putExtra(TimerOverlayService.EXTRA_SECONDS, 30);
            intent.putExtra(TimerOverlayService.EXTRA_MESSAGE, "Test timer");
            startService(intent);
        }));

        root.addView(button("Change Mode", v -> {
            prefs.edit().remove(KEY_MODE).apply();
            showModePicker();
        }));
        setContentView(scroll(root));
    }

    private void quickSend(EditText ip, EditText message, int minutes) {
        EditText temp = new EditText(this);
        temp.setText(String.valueOf(minutes));
        sendTimer(ip, temp, message);
    }

    private void sendTimer(EditText ip, EditText minutes, EditText message) {
        String host = ip.getText().toString().trim();
        String minutesText = minutes.getText().toString().trim();
        if (host.isEmpty() || minutesText.isEmpty()) {
            toast("Enter the tablet IP and minutes first.");
            return;
        }

        int seconds;
        try {
            seconds = Math.max(1, Integer.parseInt(minutesText)) * 60;
        } catch (NumberFormatException e) {
            toast("Minutes must be a number.");
            return;
        }

        String note = message.getText().toString().trim();
        executor.execute(() -> {
            try {
                String encoded = URLEncoder.encode(note, "UTF-8");
                URL url = new URL("http://" + host + ":8765/timer?seconds=" + seconds + "&message=" + encoded);
                HttpURLConnection connection = (HttpURLConnection) url.openConnection();
                connection.setConnectTimeout(4000);
                connection.setReadTimeout(4000);
                connection.setRequestMethod("GET");

                int code = connection.getResponseCode();
                BufferedReader reader = new BufferedReader(new InputStreamReader(
                        code >= 200 && code < 300 ? connection.getInputStream() : connection.getErrorStream()));
                String response = reader.readLine();
                runOnUiThread(() -> toast(code >= 200 && code < 300 ? "Timer sent." : "Tablet error: " + response));
            } catch (Exception e) {
                runOnUiThread(() -> toast("Could not reach tablet. Check Wi-Fi and IP address."));
            }
        });
    }

    private void startTimerServer() {
        Intent intent = new Intent(this, TimerServerService.class);
        if (Build.VERSION.SDK_INT >= 26) {
            startForegroundService(intent);
        } else {
            startService(intent);
        }
    }

    private String getLocalIpAddress() {
        try {
            for (NetworkInterface networkInterface : Collections.list(NetworkInterface.getNetworkInterfaces())) {
                for (java.net.InetAddress address : Collections.list(networkInterface.getInetAddresses())) {
                    if (!address.isLoopbackAddress() && address instanceof Inet4Address) {
                        return address.getHostAddress();
                    }
                }
            }
        } catch (Exception ignored) {
        }
        return "IP address not found. Check Wi-Fi is connected.";
    }

    private ScrollView scroll(View child) {
        ScrollView scroll = new ScrollView(this);
        scroll.addView(child);
        return scroll;
    }

    private LinearLayout baseLayout() {
        LinearLayout root = new LinearLayout(this);
        root.setOrientation(LinearLayout.VERTICAL);
        root.setPadding(36, 36, 36, 36);
        root.setBackgroundColor(Color.rgb(248, 250, 252));
        return root;
    }

    private TextView title(String text) {
        TextView view = new TextView(this);
        view.setText(text);
        view.setTextSize(30);
        view.setTextColor(Color.rgb(15, 23, 42));
        view.setGravity(Gravity.CENTER_HORIZONTAL);
        view.setPadding(0, 10, 0, 18);
        return view;
    }

    private TextView label(String text) {
        TextView view = body(text);
        view.setTextColor(Color.rgb(71, 85, 105));
        return view;
    }

    private TextView body(String text) {
        TextView view = new TextView(this);
        view.setText(text);
        view.setTextSize(18);
        view.setTextColor(Color.rgb(30, 41, 59));
        view.setPadding(0, 8, 0, 14);
        return view;
    }

    private EditText input(String hint, int inputType) {
        EditText editText = new EditText(this);
        editText.setHint(hint);
        editText.setTextSize(18);
        editText.setSingleLine(true);
        editText.setInputType(inputType);
        editText.setPadding(12, 10, 12, 10);
        editText.setLayoutParams(new LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.MATCH_PARENT, LinearLayout.LayoutParams.WRAP_CONTENT));
        return editText;
    }

    private Button button(String text, View.OnClickListener listener) {
        Button button = new Button(this);
        button.setText(text);
        button.setTextSize(18);
        button.setAllCaps(false);
        button.setOnClickListener(listener);
        button.setLayoutParams(new LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.MATCH_PARENT, LinearLayout.LayoutParams.WRAP_CONTENT));
        return button;
    }

    private Button smallButton(String text, View.OnClickListener listener) {
        Button button = button(text, listener);
        LinearLayout.LayoutParams params = new LinearLayout.LayoutParams(0, LinearLayout.LayoutParams.WRAP_CONTENT, 1);
        params.setMargins(4, 4, 4, 4);
        button.setLayoutParams(params);
        return button;
    }

    private void toast(String message) {
        Toast.makeText(this, message, Toast.LENGTH_LONG).show();
    }

    @Override
    public void onRequestPermissionsResult(int requestCode, String[] permissions, int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);
        if (requestCode == 30 && grantResults.length > 0 && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
            toast("Notifications enabled.");
        }
    }
}
