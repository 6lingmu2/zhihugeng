import time
import sys
import os
from pyngrok import ngrok
from pyngrok.conf import PyngrokConfig

project = r"d:\比赛\商业精英\网址"
ngrok_dir = os.path.join(project, ".ngrok")
os.makedirs(ngrok_dir, exist_ok=True)

cfg = PyngrokConfig(
    ngrok_path=os.path.join(ngrok_dir, "ngrok.exe"),
    config_path=os.path.join(ngrok_dir, "ngrok.yml"),
)

port = 8765
try:
    tunnel = ngrok.connect(port, "http", pyngrok_config=cfg)
    print("PUBLIC_URL=" + tunnel.public_url, flush=True)
    while True:
        time.sleep(30)
except Exception as e:
    print("ERROR: " + str(e), flush=True)
    sys.exit(1)
