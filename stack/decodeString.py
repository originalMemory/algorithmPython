# coding=utf-8
"""
@project : algorithmPython
@ide     : PyCharm
@file    : decodeString
@author  : illusion
@desc    : 394. 字符串解码 https://leetcode-cn.com/problems/decode-string/
@create  : 2021/5/27 1:45 下午:19
"""
class Solution:
    def decodeStringAssist(self, s: str) -> str:
        stack, res, multi = [], "", 0
        for char in s:
            if char.isdigit():
                multi = multi * 10 + int(char)
            elif char == '[':
                stack.append((res, multi))
                res, multi = "", 0
            elif char == ']':
                last_res, last_multi = stack.pop()
                res = last_res + res * last_multi
            else:
                res += char
        return res

    def dfs(self, s: str, index: int) -> str:
        res, multi = "", 0
        i = index
        while i < len(s):
            c = s[i]
            if c.isdigit():
                multi = multi * 10 + int(c)
            elif c == '[':
                i, str2 = self.dfs(s, i + 1)
                res += str2 * multi
                multi = 0
            elif c == ']':
                return i, res
            else:
                res += c
            i += 1
        return res


if __name__ == "__main__":
    s = Solution()
    value = s.dfs("3[z]2[2[y]pq4[2[jk]e1[f]]]ef", 0)
    s1 = "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef"
    print(value, value == s1)
    print(s1)
