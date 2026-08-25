class MinStack:
    def __init__(self):
        self.stacka = []
        self.stackb = []

    def push(self, val: int) -> None:
        self.stacka.append(val)
        if not self.stackb or self.stackb[-1]>=val: #equal to sign very important here
            self.stackb.append(val)

    def pop(self) -> None:
        val = self.stacka[-1]
        self.stacka.pop()
        if self.stackb[-1] == val:
            self.stackb.pop()

    def top(self) -> int:
        return self.stacka[-1]

    def getMin(self) -> int:
        return self.stackb[-1]
