import os
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

def get_available_filename(base_name, max_attempts=10):
    if not os.path.exists(base_name):
        return base_name

    file_root, file_ext = os.path.splitext(base_name)
    counter = 1

    while counter <= max_attempts:
        new_name = f"{file_root}_{counter}{file_ext}"
        if not os.path.exists(new_name):
            return new_name
        counter += 1
    
    raise Exception("Unable to generate a unique filename after several attempts.")

def generate_numbers(x, y, filename="output.txt"):
    try:
        if not filename.endswith(".txt"):  # Enforce .txt extension
            filename += ".txt"

        if x > y:
            raise ValueError("The starting number must not be greater than the ending number.")
        
        filename = get_available_filename(filename)

        with open(filename, "w") as file:
            for number in range(x, y + 1):
                file.write(f"{number}\n")

        print(f"\n{Fore.GREEN}✔️ Numbers between {x} and {y} have been written to '{filename}' successfully!")
    except ValueError as ve:
        print(f"{Fore.RED}❌ {ve}")
    except PermissionError:
        print(f"{Fore.RED}❌ Permission denied while trying to write to the file.")
    except Exception as e:
        print(f"{Fore.RED}❌ An error occurred: {e}")

def main():
    print(f"""
    {Fore.CYAN}╔════════════════════════════════════════════╗
    {Fore.CYAN}║               NumCraft                     ║
    {Fore.CYAN}║    Generate numbers for your payloads      ║
    {Fore.CYAN}╚════════════════════════════════════════════╝

    ──────────────────────────────────────────────
       🎯 Tool Features:
       - Generates numbers between two values
       - Saves the list in a text file
       - Handles file naming conflicts automatically
    ──────────────────────────────────────────────
    """)

    try:
        x = int(input(f"{Fore.YELLOW}🔢 Enter the starting number : "))
        y = int(input(f"{Fore.YELLOW}🔢 Enter the ending number : "))
        filename = input(f"{Fore.YELLOW}📂 Enter the output file name (default: output.txt): ").strip() or "output.txt"

        print(f"\n{Fore.BLUE}🚀 Generating numbers...\n")
        generate_numbers(x, y, filename)

        print(f"\n{Fore.GREEN}✨ Thank you for using NumCraft. Stay secure! ✨")
        print(f"{Fore.GREEN}Created by HACKNB")
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}❌ Operation canceled by user. Goodbye!")
    except Exception as e:
        print(f"\n{Fore.RED}❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

