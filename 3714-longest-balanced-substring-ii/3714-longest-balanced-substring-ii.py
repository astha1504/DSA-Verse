class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 1 
        cnt = 1
        for i in range(1, n):
            if s[i] == s[i-1]:
                cnt += 1
            else:
                ans = max(ans, cnt)
                cnt = 1
        ans = max(ans, cnt)

        # -------- helper for 2-char balance --------
        def two_char(x, y):
            nonlocal ans
            diff = 0
            seen = {0: -1}

            for i, ch in enumerate(s):
                if ch != x and ch != y:
                    diff = 0
                    seen = {0: i}
                    continue

                if ch == x:
                    diff += 1
                else:
                    diff -= 1

                if diff in seen:
                    ans = max(ans, i - seen[diff])
                else:
                    seen[diff] = i

        two_char('a','b')
        two_char('a','c')
        two_char('b','c')

        # -------- case 3: all three equal --------
        a=b=c=0
        seen = {(0,0):-1}

        for i,ch in enumerate(s):
            if ch=='a': a+=1
            elif ch=='b': b+=1
            else: c+=1

            key = (a-b, a-c)

            if key in seen:
                ans = max(ans, i-seen[key])
            else:
                seen[key] = i

        return ans
