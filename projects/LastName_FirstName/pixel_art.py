import os
import sys
import time

# Enable ANSI escape codes in Windows terminals
if os.name == 'nt':
    os.system('color')
    # Try to enable virtual terminal processing on Windows
    try:
        import ctypes
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    except:
        pass

def get_ansi_color(char):
    """Map input character to ANSI color code."""
    colors = {
        'r': '\033[41m',  # Red background
        'b': '\033[44m',  # Blue background
        'g': '\033[42m',  # Green background
        'y': '\033[43m',  # Yellow background
        'w': '\033[47m',  # White background
        '.': '\033[40m'   # Black (empty)
    }
    return colors.get(char, '\033[40m')

def print_grid(grid):
    """Print the grid with ANSI colors."""
    reset = '\033[0m'
    output_lines = []
    print("Generated grid:")
    for row in grid:
        line = ''.join(f'{get_ansi_color(cell)}  {reset}' for cell in row)
        print(line)
        # For file output, save the actual characters
        output_lines.append(''.join(cell for cell in row))
    print()  # Extra line for readability
    
    # Save output to file (without ANSI codes) with timestamp
    import datetime
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f'output_{timestamp}.txt'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"Generated at: {datetime.datetime.now()}\n")
        for line in output_lines:
            f.write(line + '\n')
    print(f"Output saved to {filename}")
    
    # Also save to last_output.txt for easy checking
    with open('last_output.txt', 'w', encoding='utf-8') as f:
        f.write(f"Generated at: {datetime.datetime.now()}\n")
        for line in output_lines:
            f.write(line + '\n')

def get_sample_heart():
    """Return a 5x5 heart pattern as a list of lists."""
    return [
        list('.rr..'),
        list('rrrrr'),
        list('rrrrr'),
        list('.rrr.'),
        list('..r..')
    ]

def main():
    print("Console Pixel Art Generator")
    print("Use: r=red, b=blue, g=green, y=yellow, w=white, .=empty")
    print("Enter 'sample' for a predefined heart pattern.")
    
    while True:
        try:
            size = input("Enter grid size (e.g., 5 for 5x5, 0 to exit): ").strip()
            if size == '0':
                print("Exiting...")
                break

            if size.lower() == 'sample':
                grid = get_sample_heart()
                print("\nSample Heart Pattern:")
                print_grid(grid)
                continue

            size = int(size)
            if size < 1 or size > 10:  # Keep small for terminal
                print("Size must be 1-10.")
                continue

            grid = []
            print(f"Enter {size} rows of {size} chars (r,b,g,y,w,.)")
            valid = True
            for i in range(size):
                row = input(f"Row {i+1}: ").strip()
                if len(row) != size or not all(c in 'rbgwy.' for c in row):
                    print("Invalid row. Use r,b,g,y,w,. and match size.")
                    valid = False
                    break
                grid.append(list(row))

            if valid and len(grid) == size:
                print("\nYour Pixel Art:")
                print_grid(grid)
                time.sleep(0.5)  # Brief pause for effect
            else:
                print("Input was invalid. Please try again.")
        except ValueError:
            print("Invalid input. Enter a number or 'sample'.")
        except KeyboardInterrupt:
            print("\nExiting...")
            break

if __name__ == "__main__":
    main()