from parser import parse_log
class LogAnalyzer:
    def __init__(self):
        self._logs=[]
        self._level_counts = {}
        self._message_counts = {}
    
    def add_log(self, line: str):
        try:
            entry = parse_log(line)
            if entry: 
                self._logs.append(entry)
                self._level_counts[entry.level] = self._level_counts.get(entry.level, 0) + 1
                self._message_counts[entry.message] = self._message_counts.get(entry.message, 0) + 1
        except Exception as e:
            print(f"Failed to add log: {e}")

    def get_level_summary(self) -> dict:
        return dict(self._level_counts)

    def get_top_messages(self, n: int) -> list:
        if not isinstance(n, int) or n <= 0:
            raise ValueError("n must be a positive integer")
        # if n <= 0:
        #     return []

        sorted_messages = sorted(self._message_counts.items(), key=lambda item: item[1], reverse=True)
        return sorted_messages[:n]

