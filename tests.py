import algorithms
import pytest
import random


def test_quick_sort():
    """Test quick sort."""
    array = [random.randint(0, 100) for i in range(10)]
    copy_of_array = array[:]
    algorithms.quick_sort(array, 0, len(array) - 1)
    assert array == sorted(copy_of_array), "Quick sort failed."


def test_merge_sort():
    """Test merge sort."""
    array = [random.randint(0, 100) for i in range(10)]
    copy_of_array = array[:]
    algorithms.merge_sort(array, 0, len(array) - 1)
    assert array == sorted(copy_of_array), "Merge sort failed."


def test_bubble_sort():
    """Test bubble sort."""
    array = [random.randint(0, 100) for i in range(10)]
    copy_of_array = array[:]
    algorithms.bubble_sort(array)
    assert array == sorted(copy_of_array), "Bubble sort failed."


def test_insertion_sort():
    """Test insertion sort."""
    array = [random.randint(0, 100) for i in range(10)]
    copy_of_array = array[:]
    algorithms.insertion_sort(array)
    assert array == sorted(copy_of_array), "Insertion sort failed."


def test_count_sort():
    """Test count sort."""
    array = [random.randint(0, 100) for i in range(10)]
    copy_of_array = array[:]
    algorithms.count_sort(array)
    assert array == sorted(copy_of_array), "Count sort failed."


if __name__ == "__main__":
    pytest.main(["-v", "tests.py"])
