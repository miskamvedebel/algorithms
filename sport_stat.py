class RunnerStat():
    def __init__(self, res) -> None:
        self.res = res
        self.empty = self.res == ''
        self._calc_stat()
    
    def _calc_stat(self) -> None:
        if not self.empty:
            self._res = self.res.split(', ')
            self._res_seconds = []
            for rr in self._res:
                tmp = rr.split("|")
                s = 0
                for i in range(0, len(tmp), 1):
                    s += int(tmp[i]) * (60 ** (2-i))
                
                self._res_seconds.append(s)
            
            self.mn = min(self._res_seconds)
            self.mx = max(self._res_seconds)
            self.N = len(self._res_seconds)
            self.even = self.N % 2 == 0
            self.avg = sum(self._res_seconds) / self.N
            self.range = self.mx - self.mn
            self.sorted_arr = sorted(self._res_seconds)
            self.median = self.sorted_arr[self.N // 2] if not self.even else (self.sorted_arr[self.N // 2] + self.sorted_arr[self.N // 2 - 1]) / 2
    
    def _format_to_string(self, value: int) -> str:
        h = value // 3600
        m = (value - h * 3600) // 60
        s = value - h * 3600 - m * 60
        return f"{int(h):02}|{int(m):02}|{int(s):02}"
        

    def print_stat(self) -> str:
        if self.empty:
            return ''
        rng = self._format_to_string(self.range)
        avg = self._format_to_string(self.avg)
        median = self._format_to_string(self.median)
        return f"Range: {rng} Average: {avg} Median: {median}"


# st = RunnerStat("01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17")
# print(st.print_stat())

st = RunnerStat('')
print(st.print_stat())