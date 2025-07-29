import json
import random
import time
import csv

# loaded commands from JSON file
with open("commands.json", "r") as f:
    commands = json.load(f)

# kept track of command history to avoid repeats
command_history = []
current = None
start_time = time.time()

# grabbed a random command, made sure it wasn't the same as the last
def get_random_command():
    global current
    while True:
        cmd = random.choice(commands)
        if not command_history or cmd["command"] != command_history[-1]["command"]:
            command_history.append(cmd)
            current = cmd
            return cmd

# displayed the main info nicely
def show_command(cmd):
    print(f"\nCommand: {cmd['command']}")
    print(f"Summary: {cmd['summary']}")
    print("[e] Explanation  [r] Refresh  [x] Export History  [h] Help  [q] Quit")

# showed explanation if user wanted more detail
def show_explanation(cmd):
    print(f"\nExplanation for {cmd['command']}:\n{cmd['explanation']}")

# let user export history to CSV file
def export_history_to_csv():
    with open("command_history.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["command", "summary", "explanation"])
        writer.writeheader()
        writer.writerows(command_history)
    print("\n Command history saved to 'command_history.csv'.")

# showed help menu again
def show_help():
    print("\nInfraTool Help Menu")
    print("start - Start the tool")
    print("e - Show explanation")
    print("r - Refresh new command")
    print("x - Export command history")
    print("h - Help menu")
    print("q - Quit\n")

# displayed reflection message if app had been running for a while
def show_reflection_if_needed():
    global start_time
    if time.time() - start_time > 10:  # 1200 is 20 minuites, 5 is 5 seconds
        print("\n You've been using InfraTool for a while.")
        print("“Mastery is built in moments of reflection. Take a breath and keep going strong.”")
        print("You can export your session with [x] or keep exploring.\n")
        start_time = time.time()  # reset timer

# ran the main tool loop
def main():
    print("Welcome to InfraTool — A DevOps CLI Helper Tool")
    print("Type 'start' to begin. Type 'h' if you ever get stuck.")

    while True:
        show_reflection_if_needed()
        cmd = input("\n> ").strip().lower()

        if cmd == "start":
            c = get_random_command()
            show_command(c)
        elif cmd == "e" and current:
            show_explanation(current)
        elif cmd == "r":
            c = get_random_command()
            show_command(c)
        elif cmd == "x":
            export_history_to_csv()
        elif cmd == "h":
            show_help()
        elif cmd == "q":
            print("Thanks for using InfraTool.")
            break
        else:
            print("Oops — didn’t catch that. Type 'h' for help.")

# ran the whole thing
if __name__ == "__main__":
    main()
