"""
This module lets you practice the ACCUMULATOR pattern
in its simplest classic forms:
   SUMMING:       total = total + number

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Derek Grayless.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.
import math


def main():
    """ Calls the   TEST   functions in this module. """
    test_sum_cosines()
    test_sum_square_roots()


def test_sum_cosines():
    """ Tests the   sum_cosines   function. """
    # ------------------------------------------------------------------
    # Done: 2. Implement this function.
    #   It TESTS the  sum_cosines  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_cosines   function:')
    print('--------------------------------------------------')

    expected = 1.540302
    answer = sum_cosines(2)
    print('Test 1 expected:', expected)
    print('     actual:', answer)

    expected1 = 1.124155
    answer1 = sum_cosines(3)
    print('Test 2 expected:', expected1)
    print('     actual:', answer1)

    expected2 = .724351
    answer2 = sum_cosines(7)
    print('Test 3 expected:', expected2)
    print('     actual:', answer2)

def sum_cosines(n):
    """
    What comes in:  A non-negative integer n.
    What goes out:  The sum of the cosines of the integers
       0, 1, 2, 3, ... n, inclusive, for the given n.
    Side effects:   None.
    Example:
      If n is 3, this function returns
        cos(0) + cos(1) + cos(2) + cos(3)   which is about 0.13416.
    """
    # ------------------------------------------------------------------
    # Done: 3. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #   That is called TEST-DRIVEN DEVELOPMENT (TDD).
    #
    #   No fair running the code of  sum_cosines  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # ------------------------------------------------------------------

    # remember dont use sum as variable because there is a sum function in math
    add = 0
    for k in range(n):
       add = add + math.cos(k)
    return add


def test_sum_square_roots():
    """ Tests the   sum_square_roots   function. """
    # ------------------------------------------------------------------
    # Done: 4. Implement this function.
    #   It TESTS the  sum_square_roots  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_square_roots   function:')
    print('--------------------------------------------------')

    expected = 8.692130
    answer = sum_square_roots(4)
    print('Test 1 expected:', expected)
    print('     actual:', answer)

    expected1 = 11.85440766
    answer1 = sum_square_roots(5)
    print('Test 2 expected:', expected1)
    print('     actual:', answer1)

    expected2 = 15.31850928
    answer2 = sum_square_roots(6)
    print('Test 3 expected:', expected2)
    print('     actual:', answer2)

def sum_square_roots(n):
    """
    What comes in:  A non-negative integer n.
    What goes out:  The sum of the square roots of the integers
       2, 4, 6, 8, ... 2n    inclusive, for the given n.
           So if n is 7, the last term of the sum is
           the square root of 14 (not 7).
    Side effects:   None.
    Example:
      If n is 5, this function returns
         sqrt(2) + sqrt(4) + sqrt(6) + sqrt(8) + sqrt(10),
      which is about 11.854408.
    """
    # ------------------------------------------------------------------
    # Done: 5. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #   That is called TEST-DRIVEN DEVELOPMENT (TDD).
    #
    #   No fair running the code of  sum_square_roots  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # ------------------------------------------------------------------
    #range (2, (2*n)+1, 2)
    # firt 2 is lower boundary
    # (2*n)+1 is the upper boundary which in Test one would be (2*3)+1 so it will run three times without reaching boun
    # dary, last 2 is saying have the index increment by 2

    add = 0
    for k in range(2, (2*n)+1, 2):
        add = add + math.sqrt(k)
    return add

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
