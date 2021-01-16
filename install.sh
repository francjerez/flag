#!/bin/bash

unm=$(logname)
uid=$(id -u $unm)
src=$(dirname "$0")
usr="/Users/$unm"
lib="$usr/Library"
plf="$lib/LaunchAgents/com.luxafor.flag.plist"

# Header
echo -e "\nInstalling..."

# Install agent
mkdir -p "$lib/LaunchAgents" 
cp "$src/com.luxafor.flag.plist" "$lib/LaunchAgents" 2>/dev/null
sed -i "" "s/<UID>/$unm/g" "$plf"
chown root "$plf"
chgrp wheel "$plf"
chmod 644 "$plf"
echo "-> $plf"

# Install script
mkdir -p "$lib/Scripts"
cp "$src/flag.py" "$lib/Scripts" 2>/dev/null
echo "-> $lib/Scripts/flag.py"

# Install hook
defaults write com.apple.loginwindow LogoutHook "$usr/.logouthook"
echo -e $"#!/bin/bash\n\n/usr/bin/python3 $lib/Scripts/flag.py logout" > "$usr/.logouthook"
chmod +x "$usr/.logouthook"
echo "-> $usr/.logouthook"

# Launch agent 
launchctl bootstrap gui/"${uid}" "$plf" 2>/dev/null 

# Footer
echo "All done!"
