# Flag
![flags](https://user-images.githubusercontent.com/3150023/104853775-56256f80-5903-11eb-9f8d-5507905a28af.png)

Flag is a very small Python 3.x module managed by `launchd`, tested on (and designed for) macOS Big Sur.

## Details

The tool is intended to help you control a single USB connected [Luxafor Flag](https://luxafor.com/flag-usb-busylight-availability-indicator/) device from the *Do Not Disturb* switch you can find both in the *Control Center* and, when enabled from the *System Preferences*, in the *Menu Bar*: 

![menubar](https://user-images.githubusercontent.com/3150023/104853832-b74d4300-5903-11eb-85fe-6d4400feaa31.png)

For further efficiency, you may want to create a keyboard shorcut, like this one:

![keyboard](https://user-images.githubusercontent.com/3150023/104854213-c503c800-5905-11eb-84e2-ab2fc81c8287.png)

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
