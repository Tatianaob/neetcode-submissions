class Solution:
    def isValid(self, s: str) -> bool:
        # while '[]' in s or '{}' in s or '[]' in s:
        #     s = s.replace('[]', '')
        #     s = s.replace('{}', '')
        #     s = s.replace('()', '')
        # return s == ''

        # creating an empty stack
        stack = []
        # create a dict: to map each parenthesis to each corresponding parenthesis
        couplesDict = {
            ']': '[',
            ')': '(',
            '}': '{'
        }
        for char in s:
            if char in couplesDict:
                if stack and stack[-1] == couplesDict[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False




        # populate the stack witht the parenthesis
        # check if the parenthesis from the string are in the dictionary and then append it to the stack
        # check if its corresponding value are in the dict if so, pop,
        # stack should be empty meaning each parenthesis found its couple. -> return true
        # stack should return false







      







        