#!/bin/bash
echo "🚀 Reech is initiating the Sovereign Purge..."

# 1. Purge Buildozer/Android Bloat (The highest leverage move)
echo "🧹 Clearing Buildozer cache and hidden Android artifacts..."
rm -rf ~/.buildozer/
rm -rf .buildozer/
rm -rf ~/.gradle/
rm -rf .gradle/

# 2. Cleanup Apt and System Packages
echo "🧹 Scrubbing system package cache..."
sudo apt-get autoremove -y
sudo apt-get autoclean -y
sudo apt-get clean

# 3. Eliminate Zombie Logs and Temp Files
echo "🧹 Purging dead logs and temporary assets..."
rm -rf ~/debian_core.log
find . -name "*.log" -delete
sudo rm -rf /tmp/*
sudo rm -rf /var/tmp/*

# 4. Deep-Clean Git (if applicable)
echo "🧹 Optimizing Git database..."
git gc --prune=now --aggressive

echo "✅ Purge Complete. Environment is now Optimal and Nurturing."
df -h | grep '^/'
