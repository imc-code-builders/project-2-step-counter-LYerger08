"""
Step Counter Tests

Run this file to test your implementation in project_work.py
Each function is tested individually so you can debug step by step.

Usage: python tests.py
"""

import os
import sys
from project_work import get_changes, count_peaks, count_steps, STEP_THRESHOLD
from data.utils import read_csv


def test_get_changes():
    """Test the get_changes function."""
    print("\n🧪 Testing get_changes()...")

    try:
        # Test with simple known data
        test_magnitudes = [10, 15, 12, 18, 16]
        expected_changes = [5, -3, 6, -2]  # 15-10, 12-15, 18-12, 16-18

        result = get_changes(test_magnitudes)

        # Check that we got a list
        if not isinstance(result, list):
            print("❌ FAIL: get_changes should return a list")
            return False

        # Check length
        expected_length = len(test_magnitudes) - 1
        if len(result) != expected_length:
            print(f"❌ FAIL: Expected {expected_length} changes, got {len(result)}")
            print("💡 Hint: Changes list should have one fewer element than magnitudes")
            return False

        # Check values
        if result != expected_changes:
            print(f"❌ FAIL: Expected {expected_changes}, got {result}")
            print("💡 Hint: change = magnitudes[i+1] - magnitudes[i]")
            return False

        # Test with empty and single-element lists
        if get_changes([]) != []:
            print("❌ FAIL: get_changes([]) should return []")
            return False
        if get_changes([42]) != []:
            print("❌ FAIL: get_changes([42]) should return []")
            return False

        print("✅ PASS: get_changes() works correctly!")
        return True

    except Exception as e:
        print(f"❌ FAIL: Error in get_changes(): {e}")
        print("💡 Hint: Check your loop logic")
        return False


def test_count_peaks():
    """Test the count_peaks function."""
    print("\n🧪 Testing count_peaks()...")

    try:
        # Test with known data
        test_changes = [50, -30, 150, 75, -10, 200, -50]
        threshold = 100
        expected_count = 2  # Only 150 and 200 are > 100

        result = count_peaks(test_changes, threshold)

        # Check that we got an integer
        if not isinstance(result, int):
            print("❌ FAIL: count_peaks should return an integer")
            return False

        if result != expected_count:
            print(f"❌ FAIL: Expected {expected_count} peaks above {threshold}, got {result}")
            print("💡 Hint: Count values that are GREATER THAN the threshold")
            return False

        # Test edge cases
        if count_peaks([], 100) != 0:
            print("❌ FAIL: count_peaks([], 100) should return 0")
            return False

        if count_peaks([50, 75], 100) != 0:
            print("❌ FAIL: count_peaks([50, 75], 100) should return 0")
            return False

        if count_peaks([150, 200], 100) != 2:
            print("❌ FAIL: count_peaks([150, 200], 100) should return 2")
            return False

        print("✅ PASS: count_peaks() works correctly!")
        return True

    except Exception as e:
        print(f"❌ FAIL: Error in count_peaks(): {e}")
        print("💡 Hint: Check your counting logic")
        return False


def test_count_steps():
    """Test the count_steps function."""
    print("\n🧪 Testing count_steps()...")

    try:
        # Test with simple known data
        test_magnitudes = [1000, 1150, 1050, 1200, 1000]  # Changes: [150, -100, 150, -200]
        threshold = 120
        expected_count = 2  # Two changes (150, 150) are > 120

        result = count_steps(test_magnitudes, threshold)

        # Check that we got an integer
        if not isinstance(result, int):
            print("❌ FAIL: count_steps should return an integer")
            return False

        if result != expected_count:
            print(f"❌ FAIL: Expected {expected_count} steps, got {result}")
            print("💡 Hint: Use get_changes() and count_peaks() together")
            return False

        # Test with real data
        if os.path.exists("data/sample_data.csv"):
            times, magnitudes = read_csv("data/sample_data.csv")
            steps = count_steps(magnitudes, STEP_THRESHOLD)

            if steps <= 0:
                print("❌ FAIL: Should detect some steps in the sample data")
                return False
            if steps > 20:  # Sanity check - shouldn't be too many steps
                print(f"❌ FAIL: Detected {steps} steps - seems too high")
                print("💡 Hint: Check your threshold and logic")
                return False

        print("✅ PASS: count_steps() works correctly!")
        return True

    except Exception as e:
        print(f"❌ FAIL: Error in count_steps(): {e}")
        print("💡 Hint: Make sure you're using the other functions you implemented")
        return False


def test_integration():
    """Test the complete workflow with sample data."""
    print("\n🧪 Testing complete integration...")

    try:
        if not os.path.exists("data/sample_data.csv"):
            print("⚠️  SKIP: sample_data.csv not found - skipping integration test")
            return True

        # Test the complete workflow
        times, magnitudes = read_csv("data/sample_data.csv")
        changes = get_changes(magnitudes)
        peaks = count_peaks(changes, STEP_THRESHOLD)
        steps = count_steps(magnitudes, STEP_THRESHOLD)

        # The count_steps result should match count_peaks result
        if steps != peaks:
            print(f"❌ FAIL: count_steps ({steps}) doesn't match count_peaks ({peaks})")
            print("💡 Hint: count_steps should use get_changes and count_peaks")
            return False
        
        if steps == 0:
            print(f"❌ FAIL: count_steps should return a value great than zero")
            return False

        # Results should be reasonable
        if len(times) != len(magnitudes):
            print("❌ FAIL: Times and magnitudes should have same length")
            return False

        if len(changes) != len(magnitudes) - 1:
            print("❌ FAIL: Changes should have one fewer element than magnitudes")
            return False

        print(f"✅ PASS: Complete integration works!")
        print(f"📊 Results: {len(magnitudes)} data points, {steps} steps detected")
        return True

    except Exception as e:
        print(f"❌ FAIL: Integration test error: {e}")
        return False


def run_all_tests():
    """Run all tests and provide a summary."""
    print("🚀 Running Step Counter Tests\n")
    print("=" * 50)

    tests = [
        test_get_changes,
        test_count_peaks,
        test_count_steps,
        test_integration
    ]

    passed = 0
    total = len(tests)

    for test in tests:
        if test():
            passed += 1

    print("\n" + "=" * 50)
    print(f"📋 SUMMARY: {passed}/{total} tests passed")

    if passed == total:
        print("🎉 Congratulations! All tests pass!")
        print("🔬 Try running your project_work.py to see the results")
        print("📊 You can also experiment with plotting using utils.py")
    else:
        print("🔧 Keep working on the failing functions")
        print("💡 Each test gives hints about what might be wrong")

    return passed == total


if __name__ == "__main__":
    run_all_tests()
