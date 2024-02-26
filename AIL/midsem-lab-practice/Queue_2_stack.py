"""
Implementation of a queue in Python using two stacks.

queue
enqueue()
dequeue()
display()
"""


class Stack:
    def __init__(self, arr: list = []):
        self.arr = arr
        self.top = -1

    def push(self, ele):
        self.arr.append(ele)

    def pop(self):
        return self.arr.pop()

    def __str__(self):
        res = "Stack: "
        for ele in self.arr:
            res += str(ele) + " "
        return res


class QueueStack:
    def __init__(self, arr: list = []):
        self.s1 = Stack(arr)
        self.s2 = Stack()

    def __str__(self) -> str:
        res = "Queue: "
        for ele in self.s1.arr:
            res += str(ele) + " "
        return res

    def enqueue(self, ele):
        self.s1.push(ele)

    def dequeue(self):
        for _ in range(len(self.s1.arr) - 1):
            self.s2.push(self.s1.pop())
        popitem = self.s1.pop()
        for _ in range(len(self.s2.arr)):
            self.s1.push(self.s2.pop())
        return popitem


if __name__ == "__main__":
    q = QueueStack([22])
    print(q)
    q.enqueue(1)
    print(q)
    q.enqueue(2)
    print(q)
    q.dequeue()
    print(q)
    q.dequeue()
    print(q)
    q.dequeue()
    print(q)
