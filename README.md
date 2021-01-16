# Flag

Flag is a very small Python 3.x module managed by `launchd`, tested on (and designed for) macOS Big Sur.

The tool is intended to help you control a single USB connected [Luxafor Flag](https://luxafor.com/flag-usb-busylight-availability-indicator/) device from the *Do Not Disturb* (DND) switch[/es] you can find both in the *Control Center* and, when enabled from the *System Preferences*, in the *Menu Bar*. 

For further efficiency, you may want to create a keyboard shortcut like this one: <kbd>ctrl</kbd> + <kbd>alt</kbd> + <kbd>cmd</kbd> + <kbd>space</kbd>

## Installation

Flag requires the HID API to talk with your Luxafor device, something you can easily achieve with just `pip`:

```
$ sudo -H pip3 install hidapi
```

Now you are ready to deploy the three components of this repository (the user agent, the Python script and the logout hook):

```
$ sudo -H ./install.sh
```

The installer automatically loads the `LaunchAgent` for you, so everything should be working by now.

## One more thing

Enjoy. :)
