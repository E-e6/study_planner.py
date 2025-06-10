import sys

if __name__ == "__main__":
    if len(sys.argv) < 3 or sys.argv[1] != "tokenize":
        print("Usage: python main.py tokenize <filename>")
        sys.exit(1)
    filename = sys.argv[2]
    try:
        with open(filename, 'r') as f:
            content = f.read()
        if content.strip() == "":
            print("EOF  null")  # Two spaces between EOF and null
    except FileNotFoundError:
        print(f"File not found: {filename}")
        sys.exit(1)
# trigger commit
