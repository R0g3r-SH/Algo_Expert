def maxArea(height):
        l  = 0 
        r = len(height)-1
        marea = 0 
        while l <r:
            width = r-l
            area = min(height[l],height[r]) * width
            marea = max(marea,area)
            if height[l]>height[r]:
                r-=1
            elif height[l]<height[r]:
                l+=1
            else:
                r-=1
                l+=1
        return marea