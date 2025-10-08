# Revision of quick sort

Quick sort is a 'divide-and-conquer' sorting algorithm that chooses a 'pivot' element and reorders the list so that all smaller elements go to the left of the pivot, and all larger elements go to the right. Recursively repeats the process for the left and the right halves.

The pivot() function reorganizes the portion of the list between the pivot_index and the end_index (inclusive) so that everything smaller than the pivot goes before it.

The quick_sort_helper() function is a recursive function that sorts the portion between the left and the right. Calls pivot() to partition the list around a pivot.

The worst case scenario for a mostly sorted list for quick sort is O(n^2).
