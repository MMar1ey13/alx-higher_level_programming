#!/usr/bin/python3

import sys

def main():
    argv = sys.argv[1:]
    argc = len(argv)

    if argc == 0:
        print("Number of argument(s): 0.")
    else:
        plural = "s" if argc > 1 else ""
        print(f"Number of argument(s): {argc}. Argument{plural}:")

        for i, arg in enumerate(argv, start=1):
            print(f"{i}: {arg}")

 if __name__ == "__main__":
     main()
