import time

# --- Simple functions for the app ---

def water_reminder():
    """Prints a message for the water reminder."""
    print("\n💧 Time to drink water! 💧")

def food_reminder():
    """Prints a message for the food reminder."""
    print("\n🍽️ Time to eat something! 🍽️")

# --- Main App Logic ---

def start_reminder_app():
    """Starts the main reminder loop."""
    print("Reminder App Started. Press Ctrl+C to stop.")

    # Get the starting time for our timers
    start_time = time.time()
    
    # Calculate the next time for each reminder
    next_water_time = start_time + 10  # 1 hour
    next_food_time = start_time + 15   # 3 hours

    try:
        while True:
            current_time = time.time()

            # Check if it's time for a water reminder
            if current_time >= next_water_time:
                water_reminder()
                # Reset from current time (avoids drift)
                next_water_time = current_time + 3600

            # Check if it's time for a food reminder
            if current_time >= next_food_time:
                food_reminder()
                # Reset from current time (avoids drift)
                next_food_time = current_time + 10800

            # Wait for 1 second before checking again
            time.sleep(1)

    except KeyboardInterrupt:
        print("\n\n⏹️ Reminder App Stopped. Have a great day!\n")

# --- Run the app ---
if __name__ == "__main__":
    start_reminder_app()
