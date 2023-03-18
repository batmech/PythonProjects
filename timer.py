import time

class CountdownTimer:
    
    def __init__(self, seconds):
        self.seconds = seconds
        self.is_running = False
        
    def start(self):
        self.is_running = True
        while self.seconds:
            mins, secs = divmod(self.seconds, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            self.seconds -= 1
            if not self.is_running:
                break
        
    def stop(self):
        self.is_running = False
        self.seconds = 0
        print("Timer stopped.")
        
    def pause(self):
        self.is_running = False
        print("Timer paused.")
        
    def resume(self):
        self.is_running = True
        print("Timer resumed.")
        self.start()
        
def get_input():
    while True:
        try:
            seconds = int(input("Enter the number of seconds to countdown: "))
            return seconds
        except ValueError:
            print("Invalid input. Please enter a number.")
        
def main():
    seconds = get_input()
    timer = CountdownTimer(seconds)
    print("Timer started. Press Ctrl+C to stop.")
    
    try:
        timer.start()
    except KeyboardInterrupt:
        print("\nTimer interrupted by user.")
    
    choice = input("Press r to reset the timer, p to pause, or q to quit: ")
    
    while choice not in ['r', 'p', 'q']:
        choice = input("Invalid input. Press r to reset the timer, p to pause, or q to quit: ")
    
    if choice == 'r':
        timer.stop()
        main()
    elif choice == 'p':
        timer.pause()
        choice = input("Press r to resume or q to quit: ")
        while choice not in ['r', 'q']:
            choice = input("Invalid input. Press r to resume or q to quit: ")
        if choice == 'r':
            timer.resume()
    elif choice == 'q':
        timer.stop()

if __name__ == '__main__':
    main()
