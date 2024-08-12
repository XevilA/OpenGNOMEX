# playground_cli.py
from core import execute_code

def main():
    print("Welcome to Open GnomeX Playground (CLI Version)")
    print("Enter your Python code below (type 'exit' to quit):\n")

    while True:
        # Collect code input from the user
        code_lines = []
        while True:
            line = input(">>> ")
            if line == "exit":
                print("Exiting Open GnomeX Playground. Goodbye!")
                return
            elif line.strip() == "":
                break
            code_lines.append(line)

        # Combine the collected lines into a single code block
        code = "\n".join(code_lines)

        # Execute the code and capture the output
        output = execute_code(code)

        # Display the output
        print("\nOutput:\n" + output + "\n")

if __name__ == "__main__":
    main()
