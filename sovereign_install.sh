#!/bin/bash
# Identify latest successful FINAL-STRIKE run
RUN_ID=$(gh run list --workflow="Apexyx Soul Forge FINAL-STRIKE" --limit 1 --status success --json databaseId -q '.[0].databaseId')

if [ -z "$RUN_ID" ]; then
    echo "⚠️ Forge still burning. Check status with: gh run watch"
    exit 1
fi

echo "🚀 Downloading Sovereign Binary (ID: $RUN_ID)..."
mkdir -p ~/Sovereign_Install
gh run download $RUN_ID --name Apexyx-Sovereign-FINAL --dir ~/Sovereign_Install

APK_FILE=$(find ~/Sovereign_Install -name "*.apk" | head -n 1)
echo "⚡ Initiating Permanent Install..."
# Pixel 8 Pro / Android 14 Bypass
termux-open "$APK_FILE"
