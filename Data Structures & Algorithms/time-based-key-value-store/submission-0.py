class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""

        entries = self.data[key]

        left = 0
        right = len(entries) - 1
        answer = ""

        while left <= right:
            middle = left + (right - left) // 2
            stored_timestamp, stored_value = entries[middle]

            if stored_timestamp <= timestamp:
                answer = stored_value
                left = middle + 1
            else:
                right = middle - 1

        return answer

