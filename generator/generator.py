import os
import random
import time
from datetime import datetime

output_dir = "/app/shared_files/"
#  b
def generate_random_text():
    text = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz ', k=50))
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = f"text_{timestamp}.txt"
    with open(os.path.join(output_dir + file_name), 'w') as f:
        f.write(text)
    print(f"Generated file: {file_name}")

if __name__ == "__main__":
    while True:
        generate_random_text()
        time.sleep(30)  # Wait 1 minute before generating the next file
