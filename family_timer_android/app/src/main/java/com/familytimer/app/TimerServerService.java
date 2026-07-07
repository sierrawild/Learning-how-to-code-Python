package com.familytimer.app;

import android.app.Notification;
import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.app.Service;
import android.content.Intent;
import android.os.Build;
import android.os.IBinder;

import java.io.BufferedReader;
import java.io.OutputStream;
import java.io.InputStreamReader;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.URLDecoder;
import java.util.HashMap;
import java.util.Map;

public class TimerServerService extends Service {
    private static final String CHANNEL_ID = "timer_server";
    private volatile boolean running;
    private ServerSocket serverSocket;

    @Override
    public void onCreate() {
        super.onCreate();
        createChannel();
        startForeground(10, notification("Ready for parent timers"));
        running = true;
        new Thread(this::runServer, "family-timer-server").start();
    }

    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        return START_STICKY;
    }

    private void runServer() {
        try {
            serverSocket = new ServerSocket(8765);
            while (running) {
                Socket socket = serverSocket.accept();
                handle(socket);
            }
        } catch (Exception ignored) {
        }
    }

    private void handle(Socket socket) {
        try (Socket closeable = socket) {
            BufferedReader reader = new BufferedReader(new InputStreamReader(closeable.getInputStream()));
            String requestLine = reader.readLine();
            if (requestLine == null || !requestLine.startsWith("GET /timer?")) {
                respond(closeable, 404, "Not found");
                return;
            }

            String query = requestLine.substring("GET /timer?".length(), requestLine.indexOf(" HTTP/"));
            Map<String, String> params = parseQuery(query);
            int seconds = Integer.parseInt(params.getOrDefault("seconds", "60"));
            String message = params.getOrDefault("message", "Time to finish this game");

            Intent intent = new Intent(this, TimerOverlayService.class);
            intent.putExtra(TimerOverlayService.EXTRA_SECONDS, Math.max(1, seconds));
            intent.putExtra(TimerOverlayService.EXTRA_MESSAGE, message);
            if (Build.VERSION.SDK_INT >= 26) {
                startForegroundService(intent);
            } else {
                startService(intent);
            }
            respond(closeable, 200, "OK");
        } catch (Exception ignored) {
        }
    }

    private Map<String, String> parseQuery(String query) throws Exception {
        Map<String, String> params = new HashMap<>();
        for (String pair : query.split("&")) {
            String[] parts = pair.split("=", 2);
            String key = URLDecoder.decode(parts[0], "UTF-8");
            String value = parts.length > 1 ? URLDecoder.decode(parts[1], "UTF-8") : "";
            params.put(key, value);
        }
        return params;
    }

    private void respond(Socket socket, int code, String body) throws Exception {
        String status = code == 200 ? "OK" : "ERROR";
        String response = "HTTP/1.1 " + code + " " + status + "\r\n"
                + "Content-Type: text/plain\r\n"
                + "Content-Length: " + body.length() + "\r\n"
                + "Connection: close\r\n\r\n"
                + body;
        OutputStream output = socket.getOutputStream();
        output.write(response.getBytes("UTF-8"));
        output.flush();
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
                    "Timer listener",
                    NotificationManager.IMPORTANCE_LOW);
            getSystemService(NotificationManager.class).createNotificationChannel(channel);
        }
    }

    @Override
    public void onDestroy() {
        running = false;
        try {
            if (serverSocket != null) {
                serverSocket.close();
            }
        } catch (Exception ignored) {
        }
        super.onDestroy();
    }

    @Override
    public IBinder onBind(Intent intent) {
        return null;
    }
}
