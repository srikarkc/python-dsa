# Quicksort

You choose a pivot point and then sort the elements around it

`[4, 3, 1, 2, 5]`

In the above list; 4 is first the pivot point. Then compare each element after (e.g. 3 is smaller than 4). If the element is smaller; then swap in the list. (e.g. 1 is smaller than 3 so swap)

`[4, 1, 3, 2, 5]`

Then, 2 is smaller than 4 as well so swap with 3

`[4, 1, 2, 3, 5]`

5 is greater than 4 so leave it.

Then the last step is to swap the 4 with the last less than item.

`[3, 1, 2, 4, 5]`

Now, everything less than 4 is to the left of 4 and everything greater is to the right of 4.

Then, we run quick sort again on all the elements to the left of 4 and on all of the elements to the right of 4.
