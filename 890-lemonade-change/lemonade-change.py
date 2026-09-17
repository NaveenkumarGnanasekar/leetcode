class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five = 0 
        ten =0 
        for i in bills:
            if i ==5:
                five +=1
            elif i ==10 :
                if five == 0 :
                    return False 
                five -=1
                ten +=1
            elif i ==20 :
                if ten >0 and  five > 0 :
                    five -=1
                    ten -=1
                elif five >= 3 :
                    five -=3
                else :
                    return False

        return True 