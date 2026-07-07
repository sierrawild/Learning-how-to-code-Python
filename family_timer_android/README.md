# Family Timer Android

Family Timer is a sideloadable Android app with two modes:

- Parent mode runs on a phone and sends a timer to the tablet over the same Wi-Fi.
- Child Tablet mode runs on the tablet, listens for timers, and shows a floating countdown over games.

## Important Android limitation

A normal sideloaded app cannot create a truly uncloseable window. Android allows the floating countdown if the tablet grants "Display over other apps", but the app can still be stopped through system settings. For a stronger setup, use Samsung parental controls, app pinning, or Android Device Owner/kiosk setup.

This first version is designed as a practical warning timer. It can also request Device Admin permission so the tablet can be locked when the timer reaches zero.

## Build

1. Install Android Studio.
2. Open this `family_timer_android` folder.
3. Let Android Studio sync Gradle.
4. Build the app with `Build > Build Bundle(s) / APK(s) > Build APK(s)`.
5. Sideload the APK onto the parent phone and the Samsung tablet.

## Tablet setup

1. Open Family Timer on the tablet.
2. Choose `Child Tablet`.
3. Grant notification permission if asked.
4. Tap `Allow floating timer` and enable display over other apps.
5. Leave the app installed and let it run in the background.
6. Note the tablet IP address shown in the app.

## Parent phone setup

1. Open Family Timer on the phone.
2. Choose `Parent Phone`.
3. Enter the tablet IP address.
4. Pick a timer duration and send it.

Both devices must be on the same Wi-Fi network for this local version.
