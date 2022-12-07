with open ("input.txt", "r") as f:
    input = f.read()

def marker_position(signal: str, size: int) -> int:
    for i in range(len(signal)):
        if len(set(signal[i: i + size])) == size:
            return i + 1

print(f"Part 1: {marker_position(input, 4)}")
print(f"Part 2: {marker_position(input, 14)}")