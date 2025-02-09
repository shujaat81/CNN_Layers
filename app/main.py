import sys


def main():
    # Uncomment this block to pass the first stage
    while True:
        sys.stdout.write("$ ")

        # Wait for user input
        command, *args = input().split(" ")

        match command:
            case "exit":
                break
            case "echo":
                print("".join(args))
            case default:
                sys.stdout.write(f"{command}: command not found\n")
        
        


if __name__ == "__main__":
    main()
