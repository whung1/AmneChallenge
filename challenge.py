from range_analyzer import RangeAnalyzer


if __name__ == "__main__":
    analyzer = RangeAnalyzer("input.txt")
    analyzer.get_windows_subranges_totals()
