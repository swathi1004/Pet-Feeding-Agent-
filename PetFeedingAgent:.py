import time

class PetFeedingAgent:
    def __init__(self):
        self.last_fed_time = None  # Store last feeding time
    
    def get_current_time(self):
        """Returns the current time in seconds."""
        return time.time()
    
    def time_since_last_feed(self):
        """Calculates the time since the last feeding in hours."""
        if self.last_fed_time is None:
            return float('inf')  # If never fed, return infinite time
        elapsed_time = self.get_current_time() - self.last_fed_time
        return elapsed_time / 3600  # Convert seconds to hours
    
    def sense_environment(self):
        """Checks if the pet needs food (not fed in last 6 hours)."""
        return self.time_since_last_feed() >= 6

    def feed_pet(self):
        """Feeds the pet and updates last fed time."""
        print(" Dispensing food for the pet...")
        self.last_fed_time = self.get_current_time()

    def stay_inactive(self):
        """Remains inactive if feeding is not needed."""
        print(" Pet has been fed recently. No action needed.")

    def act(self):
        """Main function that decides whether to feed the pet or stay inactive."""
        if self.sense_environment():
            self.feed_pet()
        else:
            self.stay_inactive()

def main():
    agent = PetFeedingAgent()
    
    while True:
        print("\n Checking pet feeding status...")
        agent.act()
        print(" Waiting for the next check (1 hour)...")
        time.sleep(3600)  # Wait for 1 hour before checking again

if __name__ == "__main__":
    main()

