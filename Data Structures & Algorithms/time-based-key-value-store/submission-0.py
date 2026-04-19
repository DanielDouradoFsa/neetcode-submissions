class TimeMap:
    def __init__(self):
        self.timestamp_key_value = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamp_key_value[key].append({"value": value, "timestamp": timestamp})

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.timestamp_key_value:
            return ""
        key_timestamp_list = self.timestamp_key_value[key]
        l, r = 0, len(key_timestamp_list)-1
        while l <= r:
            m = (r+l)//2
            if key_timestamp_list[m]["timestamp"] <= timestamp:
                res = key_timestamp_list[m]["value"]
                l = m+1
            else:
                r = m-1
        return res