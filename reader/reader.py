import os
import time

# Path to the shared directory
shared_dir = "/app/data/"

def get_latest_file():
    try:
        # List only .txt files in the shared directory
        files = [f for f in os.listdir(shared_dir) if f.endswith(".txt")]
        
        if not files:
            return None

        # Find the latest file by creation time
        latest_file = max(files, key=lambda x: os.path.getctime(os.path.join(shared_dir, x)))
        return os.path.join(shared_dir, latest_file)
    
    except FileNotFoundError:
        print(f"Directory {shared_dir} not found.")
        return None

if __name__ == "__main__":
    while True:
        latest_file = get_latest_file()
        if latest_file:
            try:
                with open(latest_file, 'r') as f:
                    content = f.read()
                    print(f"Latest file content ({latest_file}): {content}")
            except Exception as e:
                print(f"Error reading {latest_file}: {e}")
        else:
            print("No files found.")
        
        time.sleep(10)  # Check every minute
