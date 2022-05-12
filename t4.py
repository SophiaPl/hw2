class List:

    def __init__(self, *l: list):
        if l:
            if isinstance(l[0], list):
                self.list = l[0]
            else:
                raise TypeError('List() argument must be a list')
        else:
            self.list = []

    def insert(self, index, item):
        if len(self.list) >= index:
            self.list.insert(index, item)
        else:
            raise IndexError('List index out of range')

    def get(self, index):
        if len(self.list) >= index:
            return self.list[index]
        else:
            raise IndexError('List index out of range')

    def delete(self, index):
        if len(self.list) >= index:
            self.list.pop(index)
        else:
            raise IndexError('List index out of range')

    def find(self, item):
        try:
            for i in self.list:
                if i == item:
                    return self.list.index(i)
        except ValueError:
            return None

    def return_list(self):
        return self.list

    def size(self):
        return len(self.list)


class Stack:

    def __init__(self, *args):
        if not args:
            self.stack = []
        else:
            raise TypeError('Stack() takes no positional argument')

    def push(self, item):
        self.stack.append(item)

    def pull(self):
        if self.stack:
            self.stack.pop()
        return None

    def return_stack(self):
        return self.stack

    def size(self):
        return len(self.stack)


class Queue:

    def __init__(self, *args):
        if not args:
            self.queue = []
        else:
            raise TypeError('Stack() takes no positional argument')

    def push(self, item):
        self.queue.append(item)

    def pull(self):
        if self.queue:
            self.queue.pop(0)
        return None

    def return_queue(self):
        return self.queue

    def size(self):
        return len(self.queue)
