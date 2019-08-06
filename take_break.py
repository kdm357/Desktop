"""
Set an alarm to take a break by playing a youtube video
"""

import webbrowser
import time

def main():
    """
    test function for words library
    :return: nohing
    """
    video_address = "https://www.youtube.com/watch?v=rvPRaxR7HOE"
    total = 0

    while total < 3:

        # Delay
        time.sleep(3600) # 1 Hour
        webbrowser.open(video_address)
        total += 1
        print("it is time to take a break:  ", time.ctime())

if __name__ == '__main__':
    main()
    exit(0)