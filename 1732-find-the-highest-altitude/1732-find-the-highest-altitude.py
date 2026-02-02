class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt=0
        hei=0
        for g in gain:
            alt+=g
            hei=max(hei,alt)
        return hei    
            