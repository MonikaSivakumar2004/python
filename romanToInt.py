class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        ans = 0
        for i in range(len(s)):
            if i < len(s) - 1 and m[s[i]] < m[s[i + 1]]:
                ans -= m[s[i]]
            else:
                ans += m[s[i]]

        return ans
if __name__ == "__main__":
    roman_numeral = input("Enter a Roman numeral: ")
    solution = Solution()
    result = solution.romanToInt(roman_numeral)
    print(f"The integer value of the Roman numeral {roman_numeral} is: {result}")
