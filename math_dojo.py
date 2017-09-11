class MathDojo(object):

    def __init__(self):
        self.result = 0

    def add(self,*deedles):
        for deedle in deedles: #iterating through passed parameters
            if isinstance(deedle,list): #checking to see if iteration is a list
                for meeble in deedle: #adding each iteration to self.result
                    self.result += meeble
            else:
                self.result += deedle #deedle is NOT a list, is an integer so add it
        return self

    def subtract(self,*doodles):
        for doodle in doodles:
            if isinstance(doodle,list): #checking if doodle is a list or not
                for noodle in doodle: #iterating through doodle if it IS a list
                    self.result -= noodle
            else: #doodle is an integer
                self.result -= doodle
        return self

md = MathDojo()
print(md.add(2).add(2,5).subtract(3,2).result)
print(md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result)
