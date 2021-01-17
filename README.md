# Flag
![flags](https://user-images.githubusercontent.com/3150023/104853573-10b47280-5902-11eb-844a-9a53353f8561.png)

Flag is a very small Python 3.x module managed by `launchd`, tested on (and designed for) macOS Big Sur.

## Details

The tool is intended to help you control a single USB connected [Luxafor Flag](https://luxafor.com/flag-usb-busylight-availability-indicator/) device from the *Do Not Disturb* (DND) switch you can find both in the *Control Center* and, when enabled from the *System Preferences*, in the *Menu Bar*: 

![menubar](https://user-images.githubusercontent.com/3150023/104853609-4c4f3c80-5902-11eb-920f-312f9b6aa392.png)

For further efficiency, you may want to create a keyboard shorcut, like this one:

![keyboard](https://user-images.githubusercontent.com/3150023/104853614-583afe80-5902-11eb-9586-ed2fa43335c9.png)

## Installation

Flag requires the HID API to talk with your Luxafor device, something you can easily achieve with just `pip`:

```
$ sudo -H pip3 install hidapi
```

To deploy the three components of this repository (the user agent, the Python script and the logout hook):

```
$ sudo -H ./install.sh
```

The installer automatically loads the `LaunchAgent` for you, so everything should be working by now.

## One more thing

Enjoy. :)
