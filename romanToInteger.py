class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Convert Roman number to an integer
        """
        # Dictionary to store Roman numbers and their integer values
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        # Initialize variables
        result = 0
        prev_value = 0

        for char in s:  # Iterate through each character in the input string
            curr_value = roman_dict[char]  # Integer value of the current Roman number
            # If current value is greater than previous value
            # (for cases like IV, IX, XL, XC, CD, CM)
            if curr_value > prev_value:
                result += curr_value - 2 * prev_value  # Subtract twice the previous value
            else:
                result += curr_value  # Add the current value to the result
            prev_value = curr_value  # Set the current value as the previous value

        return result