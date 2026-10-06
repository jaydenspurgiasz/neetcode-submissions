'''
Calculate the time a car will reach dest
-If it reaches dest before the car ahead of it -> join that fleet

Otherwise its not in the fleet ahead of it
-Other cars can join its fleet
'''

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []
        for i in range(len(position)):
            time.append((target - position[i]) / speed[i]) 
        
        time = [t for p, t in sorted(zip(position, time), reverse=True)]
        #print(time)

        s = [time[0]]
    
        for i in range(1, len(time)):
            #print(s)
            if time[i] > s[-1]:
                s.append(time[i])


        return len(s)
        