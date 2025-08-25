import time
import os


interval=int(input("What time interval do you need ? "))


# Timers in seconds
WATER_REMINDER_INTERVAL = interval  # It was to be for 1 hour but for demo I have kept it for 10 sec


# --- Sound Alert Function ---
def play_sound(message):
    """
    Plays a simple beep sound and prints a message.
    The method for playing sound is OS-dependent.
    """
    print(f"\n🔔 ALERT: {message}\n")
    if os.name == 'nt':  # For Windows
        import winsound
        winsound.Beep(1000, 1000)  # Beep at 1000 Hz for 500 ms
        pass


# --- Main App Logic ---
def run_reminder_app():
    """
    Starts the water and food reminder application.
    """
    print("💧Water Reminder App ⏰")
    print("-----------------------------------")
    print("Press Ctrl+C at any time to stop the app.")



    # Get the user's start time
    start_time = time.time()
    next_water_time = start_time + WATER_REMINDER_INTERVAL

    try:
        while True:
            current_time = time.time()

            # Check for water reminder
            if current_time >= next_water_time:
                play_sound("Time to drink some water! 💧")
                next_water_time += WATER_REMINDER_INTERVAL
                

    except KeyboardInterrupt:
        end_time = time.time()
        print("\n-----------------------------------")
        print("⏹️ Reminder App Stopped. Have a great day!")


# --- Run the application ---
if __name__ == "__main__":
    run_reminder_app()
