import os
import sys

def analyze_and_hook(apk_path):
    print("🔍 [ANDROGUARD] Analyzing APK Structure...")
    # Using the androguard requirement we just verified
    os.system(f"androguard analyze {apk_path} > analysis_report.txt")
    
    print("🎯 [REECH] Correlating with Hooker Dynamic Scripts...")
    # If SSL pinning is detected in report, prioritize just_trust_me.js
    os.system("python3 hooker.py --script js/just_trust_me.js")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        analyze_and_hook(sys.argv[1])
