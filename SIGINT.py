import signal
import time
def long_running_task():
    try:
        print("Long running task started.")
        for i in range(10):
            time.sleep(1)  
            print(f"Task progress: {i + 1}/10")
    except KeyboardInterrupt:
        print("\nReceived Ctrl+C. Exiting gracefully.")
    finally:
        print("Cleanup or additional exit logic goes here.")
signal.signal(signal.SIGINT, signal.default_int_handler)
long_running_task()
