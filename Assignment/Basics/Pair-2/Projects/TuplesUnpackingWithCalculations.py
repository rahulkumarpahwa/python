# 4. Tuple Unpacking with Calculations
def calculate_box_volumes(boxes):
    """
    Given a list of tuples, where each tuple contains the dimensions (length, width, height) of a box,
    return a list of tuples where each tuple contains the original dimensions and the volume of the box.
    """
    result = []
    for box in boxes:
        length, width, height = box  # Unpack the tuple
        volume = length * width * height
        result.append((length, width, height, volume))
    return result

# Example Usage:
boxes = [(2, 3, 4), (5, 6, 7), (1, 2, 3)]
volumes = calculate_box_volumes(boxes)
print(volumes)  # Output: [(2, 3, 4, 24), (5, 6, 7, 210), (1, 2, 3, 6)]