import pygame


class Timer:
    """
    A reusable timer for Pygame projects.

    Measures elapsed time in configurable intervals (milliseconds).
    The default interval is 1000ms (one second).

    start() begins measuring time from the moment it is called.
    update() updates the timer and returns the number of complete intervals (seconds) that have passed
    since the timer started.
    tick() returns True when the number of elapsed intervals changes,
    and False otherwise. For example, fires every second.

    Useful for triggering events after a certain amount of time.
    Something happens every second tick() or after 3s (return from update())
    """
    def __init__(self, interval=1000):
        if interval <= 0:
            raise ValueError("Interval must be greater than zero")
        
        self.start_time = 0
        self.current_time = 0
        self.running = False
        self.last_interval = 0
        self.elapsed = 0
        self.interval = interval
        
    # start timer
    def start(self):
        if self.running == False:
            self.running = True
            self.start_time = pygame.time.get_ticks()
        
    # zero timer
    def stop(self):
        self.running = False
        self.start_time = 0
        self.current_time = 0
        self.last_interval = 0
        self.elapsed = 0
    

    # update timer
    def update(self):
        if self.running:
            self.current_time = pygame.time.get_ticks()
            
            time_passed = self.current_time - self.start_time
            self.elapsed = time_passed // self.interval
            return self.elapsed
        else:
            return None
    
    # return true each second
    def tick(self):
        if self.elapsed != self.last_interval:
            self.last_interval = self.elapsed
            return True
        else:
            return False
        