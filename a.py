import subprocess

# 1. Force remove the old container if it exists
subprocess.run(["docker", "rm", "-f", "chromium"], capture_output=True)

# 2. Run the new container
docker_cmd = [
    "docker", "run", "-d",
    "--name=chromium",
    "-e", "PUID=1000",
    "-e", "PGID=1000",
    "-e", "TZ=Etc/UTC",
    "-e", "SELKIES_UI_SHOW_SIDEBAR=true",
    "-p", "3000:3000",
    "-p", "3001:3001",
    "-v", "/path/to/chromium/config:/config",
    "--shm-size=1gb",
    "--restart", "unless-stopped",
    "lscr.io/linuxserver/chromium:latest"
]
subprocess.run(docker_cmd)

x = True

while (x):
    print("motivation is key!")