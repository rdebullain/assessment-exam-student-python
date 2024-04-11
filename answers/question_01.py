"""
Adjust the function 'equal_slices' from question_00 to return number of pieces left as well.

Examples:
    equal_slices(11, 5, 2) ➞ (True, 1)
    # 5 people x 2 slices each = 10 slices < 11 slices 

    equal_slices(11, 5, 3) ➞ (False,None)
    # 5 people x 3 slices each = 15 slices > 11 slicess

    equal_slices(8, 3, 2) ➞ (True, 2)

    equal_slices(8, 3, 3) ➞ (False, None)

    equal_slices(24, 12, 2) ➞ (True, 0)

Notes:
 - Return (True, total_slices) if there are zero people.
 - All parameters are integers.

"""
def equal_slices(total_slices, no_recipients, slices_each):
    if total_slices - (no_recipients * slices_each) >= 0:
        x = True
        y = (total_slices % (no_recipients * slices_each))
        return (x, y)
    elif total_slices - (no_recipients * slices_each) < 0:
        x = False
        y = None
        return (x, y)
    elif no_recipients == 0:
        x = True
        y = total_slices
        return (x, y)

print(equal_slices(11, 5, 2))
print(equal_slices(11, 5, 3))
print(equal_slices(8, 3, 2))
print(equal_slices(8, 3, 3))
print(equal_slices(24, 12, 2))