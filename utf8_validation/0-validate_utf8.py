#!/usr/bin/python3
def validUTF8(data):
    """Initialize a variable to keep track of the number"""
    continuation_bytes = 0

    for byte in data:
        """Convert the byte to its binary representation with 8 bits"""
        byte_str = format(byte, '08b')

        if continuation_bytes > 0:
            """ If a byte is a continuation bytedecrement the expected count"""
            if not byte_str.startswith('10'):
                return False
            continuation_bytes -= 1
        else:
            """Check the first few bits of the byte to determine the length"""
            if byte_str.startswith('0'):
                continue
            elif byte_str.startswith('110'):
                continuation_bytes = 1
            elif byte_str.startswith('1110'):
                continuation_bytes = 2
            elif byte_str.startswith('11110'):
                continuation_bytes = 3
            else:
                return False

    """ All continuation bytes matched, return True"""
    return continuation_bytes == 0
