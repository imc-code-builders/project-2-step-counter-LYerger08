from data.utils import read_csv

STEP_THRESHOLD = 120


def get_changes(magnitudes):
    """Calculate changes between consecutive values.

    Args:
        magnitudes: A list of acceleration readings in chronological order.
    Returns:
        A list containing the change in acceleration between each pair of consecutive readings.
    
    NOTE: Your return list should always be one element smaller than the input list. Why is that?
    EXAMPLE: if magnitudes = [100, 200, 50, 100], this function should return [100, -150, 50]
    """

    changes = []
    for i in range(len(magnitudes)-1):
        changes.append(magnitudes[i+1]- magnitudes[i])
    # TODO: For each pair, calculate: next_value - current_value

    return changes


def count_peaks(changes, threshold):
    """Count how many changes are above threshold.

    Args:
        changes: A list of changes in acceleration in chronological order.
        threshold: A number above which we consider an acceleration change to indicate a step.
    Returns:
        The number of acceleration changes greater than the threshold.
    
    EXAMPLE: if changes = [800, 100, 900, 400] and threshold = 700, this function should return 2.
    """

    step_count = 0

    # TODO: Count changes greater than or equal to threshold
    for change in changes:
        if change >= threshold:
            step_count+=1

    return step_count


def count_steps(magnitudes, threshold=STEP_THRESHOLD):
    """Main function: use other functions to count steps.
    
    Args:
        magnitudes: A list of acceleration readings in chronological order.
        threshold: the minimum acceleration change that is considered a step.

    Returns:
        The number of steps the user took.
    """

    # TODO: Use get_changes() and count_peaks()
    changes = get_changes(magnitudes)
    steps = count_peaks(changes, threshold)   
    return steps


if __name__ == "__main__":
    try:
        times, magnitudes = read_csv("data/sample_data.csv")
        step_count = count_steps(magnitudes)
        print(f"Loaded {len(magnitudes)} data points")
        print(f"Detected {step_count} steps")
    except Exception as e:
        print(f"Error: {e}")
        print("Run tests.py to see what needs to be fixed.")
