from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess
from datetime import datetime

def run_pipeline():
    print(f"\n⏰ Scheduled run at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    subprocess.run(["python3", "etl_pipeline.py", "--source", "all", "--mode", "incremental"])

scheduler = BlockingScheduler()
scheduler.add_job(run_pipeline, "interval", minutes=2)

print("📅 Scheduler running. Pipeline triggers every 2 minutes. Ctrl+C to stop.")
scheduler.start()
