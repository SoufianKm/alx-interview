#!/usr/bin/python3
"""
method that determines if a given data
set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.

    Args:
    data (list of int): The data set represented by a list of integers.

    Returns:
    bool: True if data is a valid UTF-8 encoding, else False.
    """
    # Number of bytes remaining to be checked in the current UTF-8 character
    num_bytes = 0

    # Masks to check the most significant bits (MSBs) of the byte
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        # Apply a mask to get the 8 least significant bits
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte >> 5) == 0b110:  # 110xxxxx
                num_bytes = 1
            elif (byte >> 4) == 0b1110:  # 1110xxxx
                num_bytes = 2
            elif (byte >> 3) == 0b11110:  # 11110xxx
                num_bytes = 3
            elif (byte >> 7):  # 1xxxxxxx (single-byte char must be 0xxxxxxx)
                return False
        else:
            # Check that the byte starts with 10xxxxxx
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    # If we finish processing and num_bytes is not zero, then
    # it means there were missing bytes for a character
    return num_bytes == 0
