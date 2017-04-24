
class RangeAnalyzer:
    def __init__(self, file):
        """
        :param file: path to the file to read
        """
        f = open(file, 'r')
        self.n, self.k = [int(i) for i in f.readline().rstrip().split(' ')]  # n = size of list, k = window size
        self.ranges = f.readline().rstrip().split(' ')  # actual list
        f.close()

    def get_windows_subranges_totals(self):
        """
        For N values, and a fixed window size K, outputs the  
        For each window of K values, from left to right, gives the number of increasing subranges within the window
        minus the number of decreasing subranges within the window.
        
        
        An increasing subrange is defined as a contiguous range of indices [a,b], a < b , where each element is larger than the previous element. 
        A decreasing subrange is similarly defined, except each element is smaller than the next.
        
        TODO: Make function return a list
        """

        # A window of days is defined as a contiguous range of days.
        # Thus, there are exactly N-K+1 windows where this metric needs to be computed.
        for i in range(self.n-self.k+1):
            # Tracks whether the current subrange is increasing or decreasing,
            # 1 for increasing, -1 for decreasing, 0 for same value
            # and the range, using trend_start to trend_end
            trend = 0
            trend_start = i
            trend_end = i
            window_sum = 0

            # Since the size of the current window is i to i+k, we only range from (i, i+k - 1)
            # since we would not want to peek outside the current window as we reach the right edge
            # to calculate increasing or decreasing
            for j in range(i, i+self.k-1):
                cur_interval = self.calculate_interval(self.ranges[j], self.ranges[j+1])
                if trend == cur_interval:  # its the same trend
                    # continue tracking the trend
                    trend_end = j+1
                if trend != cur_interval:  # our trend ends here since not increasing or decreasing anymore
                    window_sum += trend * sum(range(trend_end-trend_start+1))
                    # Set our new trend
                    trend = cur_interval
                    trend_start = j
                    trend_end = j+1
            window_sum += trend * sum(range(trend_end - trend_start + 1)) # sum the remaining trend
            print(window_sum)

    @staticmethod
    def calculate_interval(x, y):
        """
        Returns value according to whether the interval between x and y is increasing, decreasing, or equal
        
        :type x: int 
        :type y: int 
        :return: 1 if x>y, -1 if x<y, 0 if x = y
        """
        if x > y:
            return -1  # x is less than y, its decreasing
        if x < y:
            return 1  # x is greater than y, its increasing
        elif x == y:
            return 0  # no interval change
