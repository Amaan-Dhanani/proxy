import subprocess
import sys

def run_container(browser_choice):
    # 1. Force remove existing containers to prevent name conflicts
    print(f"Cleaning up old instances of {browser_choice}...")
    subprocess.run(["docker", "rm", "-f", "chromium"], capture_output=True)
    subprocess.run(["docker", "rm", "-f", "neko-firefox"], capture_output=True)

    if browser_choice == "chromium":
        cmd = [
            "docker", "run", "-d",
            "--name=chromium",
            "-e", "PUID=1000",
            "-e", "PGID=1000",
            "-e", "TZ=Etc/UTC",
            "-p", "3000:3000",
            "-v", "/path/to/chromium/config:/config",
            "--shm-size=1gb",
            "--restart", "unless-stopped",
            "lscr.io/linuxserver/chromium:latest"
        ]
    elif browser_choice == "firefox":
        cmd = [
            "docker", "run", "-d",
            "--name=neko-firefox",
            "-p", "8080:8080",
            "-p", "56000-56100:56000-56100/udp",
            "-e", "NEKO_WEBRTC_EPR=56000-56100",
            "-e", "NEKO_WEBRTC_NAT1TO1=127.0.0.1",
            "-e", "NEKO_MEMBER_MULTIUSER_USER_PASSWORD=neko",
            "-e", "NEKO_MEMBER_MULTIUSER_ADMIN_PASSWORD=admin",
            "--restart", "unless-stopped",
            "ghcr.io/m1k1o/neko/firefox:latest"
        ]
    else:
        print("Invalid choice.")
        return

    subprocess.run(cmd)
    print(f"Successfully started {browser_choice}!")

if __name__ == "__main__":
    print("Select Browser:\n1. Chromium\n2. Firefox (Neko)")
    choice = input("Enter 1 or 2: ")
    
    selected = "chromium" if choice == "1" else "firefox"
    run_container(selected)

    # Your loop
    while True:
        print("motivation is key!")
