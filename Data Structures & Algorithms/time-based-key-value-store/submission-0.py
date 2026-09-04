class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        l,r = 0, (len(self.timemap[key])-1)
        result = ""


        while l<=r:
            mid = (l+r)//2

            if self.timemap[key][mid][0] <= timestamp:
                result = self.timemap[key][mid][1]
                l = mid+1

            else:
                r = mid-1


        return result




