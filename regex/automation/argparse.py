import argparse

parser = argparse.ArgumentParser(description="Simple greeting App")

parser.add_argument("name", help="Enter your Name")
parser.add_argument("-a","--age", help="Enter your Age")
parser.add_argument("-v",'--verbose', action= "store_true",help="Enable verbose mode")

args = parser.parse_args()

print(f"Hello {args.name}")

if args.age:
    print(f"You are {args.age} year old")




    