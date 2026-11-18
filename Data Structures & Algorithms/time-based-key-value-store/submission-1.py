class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = {}
        self.store[key][timestamp]=value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        else:
            largestt=0
            for t in self.store[key].keys():
                if t<=timestamp and t>=largestt:
                    largestt=t
            if largestt==0:
                return ""
            return self.store[key][largestt]
