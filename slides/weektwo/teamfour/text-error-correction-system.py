"""A simple text error correction system using checksums."""

# Helper hashing function
def simple_checksum(s):
    """Return a simple numeric checksum for a string."""
    return str(abs(hash(s)) % (10**8))

# 1: Encode each line with a checksum
def encode_text(text):
    """Encode each line of text with a duplicate and checksum."""
    encoded = []
    for line in text.splitlines():
        checksum = simple_checksum(line)
        # Store the original line, its duplicate, and the checksum together
        encoded.append(f"{line}|||{line}|||{checksum}")
    return encoded

# 2: Decode, verify, and correct if needed
def decode_text(encoded_lines):
    """Verify and attempt to correct encoded lines using checksums."""
    for line in encoded_lines:
        line = line.strip()
        original, duplicate, checksum = line.split("|||")
        if simple_checksum(original) == checksum:
            print(f"OK: {original}")
        elif simple_checksum(duplicate) == checksum:
            print(f"Corrupted line: {original}")
            print(f"Corrected line: {duplicate}")

# Example usage
if __name__== "__main__":
    text = "Professor Kapfhammer is the best professor!"
    encoded_lines = encode_text(text)
    for l in encoded_lines:
        print(f"Encoded line: {l}")

    corrupted_lines = encoded_lines.copy()
    if corrupted_lines:
        original, duplicate, checksum = corrupted_lines[0].split("|||")
        corrupted = "X" + original[1:]
        corrupted_lines[0] = f"{corrupted}|||{duplicate}|||{checksum}"

    decode_text(corrupted_lines)

# Run this script with uv
# uv run text-error-correction-system.py

# issei test commit to see this
