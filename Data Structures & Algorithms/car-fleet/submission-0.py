class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        coupling=list(zip(position,speed))
        coupling.sort(key=lambda x : x[0], reverse=True)
        for position,speed in coupling:
            arrival_time=(target-position)/speed
            if not stack:
                stack.append(arrival_time)
            else:
                if arrival_time<=stack[-1]:
                    continue
                else:
                    stack.append(arrival_time)
        
        return len(stack)