class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Convert the given Roman numeral string to an integer.

        Parameters:
            s (str): The Roman numeral string to be converted.

        Returns:
            int: The integer value of the Roman numeral.

        Examples:
            >>> solution = Solution()
            >>> solution.romanToInt("III")
            3
            >>> solution.romanToInt("LVIII")
            58
            >>> solution.romanToInt("MCMXCIV")
            1994
        """
        m = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }

        result = 0
        s_len = len(s)

        for i in range(s_len):
            if i < len(s) - 1 and m[s[i]] < m[s[i + 1]]:
                result -= m[s[i]]
            else:
                result += m[s[i]]

        return result
    
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)