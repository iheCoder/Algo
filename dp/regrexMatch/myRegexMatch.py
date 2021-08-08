class Solution:
    # 我想把所有情况考虑到，可是很难很难，复杂度超出我的水平
    def isMatch(self, s: str, p: str) -> bool:
        #
        n = len(p)
        sn = len(s)
        if n == 0 or sn == 0:
            return False
        j = 0
        for i in range(1, n):
            # * 时，匹配0到n个pattern前字符
            if p[i] == '*':
                # fi定义为.*前面的字符
                fi = p[i - 1]
                for k in range(j, sn):
                    if s[k] != fi:
                        j = k
                        break
                # 若*匹配之后，pattern到最后，可是字符串没到最后，返回False
                if i==n-1 and j!=sn-1:
                    return False
                elif i==n-1 and j==sn-1:
                    return True
            # . 时，匹配1个pattern前字符，若不匹配返回False，若匹配而且是pattern，字符串最后的，返回True
            elif p[i] == '.':
                # err1: 没有考虑到若*是全部匹配也会导致j==sn，但这属于匹配
                # 只有当p[i]仍然存在. 或者存在字母，超出字符串范围才会return False
                fi = p[i - 1]
                if fi != s[j]:
                    return False
                if i == n - 1 and j == sn-1:
                    return True
            else:
                # pattern为字符时，只有当pattern该字符不匹配且后面为字符或者为空的时候才返回False
                if p[i] != s[j] and (i == n - 1 or p[i + 1] != '*' or p[i + 1] != '.'):
                    return False
                elif p[i]==s[j] and i==n-1:
                    return True
            j += 1
        return True


if __name__ == '__main__':
    s = Solution()
    s1 = "aab"
    p1 = "c*a*b"
    sl = [s1]
    pl = [p1]
    print(s.isMatch(s1, p1))
    # for s,p in sl,pl:
