# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
# Example:
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.

# class MinStack(object):
#
#     def __init__(self):
#         self.l = []
#
#
#     def push(self, x):
#         min_x = self.getMin()
#         if min_x == None or x < min_x:
#             min_x = x
#         self.l.append((x, min_x));
#
#     def pop(self):
#         self.l.pop()
#
#
#     def top(self):
#         if len(self.l) == 0:
#             return None
#         else:
#             return self.l[len(self.l) - 1][0]
#
#
#     def getMin(self):
#         if len(self.l) == 0:
#             return None
#         else:
#             return self.l[len(self.l) - 1][1]



class MinStach(object):

    def __init__(self):
        self.l = []

    def push(self, x):
        min_x = self.getMin()
        if min_x == None or x < min_x:
            min_x = x
        self.l.append((x, min_x))

    def pop(self):
        self.l.pop()

    def top(self):
        if len(self.l) == 0:
            return None
        else:
            return self.l[len(self.l) -1][0]

    def getMin(self):
        if self.l == 0:
            return None
        else:
            #get the last item in a tupple
            return self.l[len(self.l) -1][1]




# Your MinStack object will be instantiated and called as such:
obj = MinStack()

l = [20, 3, 4, 2, 1, 60, 34, 12, 8]
for i in l:
    obj.push(i)

obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()


# obj.push(30)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
#
#
# obj.push(10)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
#
#
# obj.push(60)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()