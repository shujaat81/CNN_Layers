import sys
def main():
    while True:
        # Uncomment this block to pass the first stage
        sys.stdout.write("$ ")
        # Wait for user input
        command, *args = input().split(" ")
        match command:
            case "exit":
                break
            case "echo":
                print(" ".join(args))
            case default:
                other = " ".join(args)
                sys.stdout.write(f"{command} {other}: command not found\n")
    return
if __name__ == "__main__":
    main()
