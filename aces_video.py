"""Open the live workspace in a dedicated Edge or Chrome app window."""
import os
import shutil
import subprocess
import sys
from pathlib import Path

def main():
    url = "https://app.beatpulse.com/"
    candidates = [shutil.which(name) for name in
                  ("msedge", "google-chrome", "chromium", "chromium-browser")]
    if sys.platform == "win32":
        for root in ("PROGRAMFILES", "PROGRAMFILES(X86)", "LOCALAPPDATA"):
            if os.environ.get(root):
                base = Path(os.environ[root])
                candidates.extend([base / "Microsoft/Edge/Application/msedge.exe",
                                   base / "Google/Chrome/Application/chrome.exe"])
    if sys.platform == "darwin":
        candidates.append("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
    browser = next((str(path) for path in candidates if path and Path(path).is_file()), None)
    if not browser:
        raise SystemExit("Install Microsoft Edge or Google Chrome and try again.")
    profile = Path.home() / ".aces-video" / "browser-profile"
    profile.mkdir(parents=True, exist_ok=True, mode=0o700)
    subprocess.Popen([browser, "--user-data-dir=" + str(profile), "--app=" + url])

if __name__ == "__main__":
    main()
