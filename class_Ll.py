class Node:
    def __init__(self, data, _next=None):
        self.data = data
        self.next = _next

    def __eq__(self, other):
        return self.data == other

    def __int__(self):
        return self.data


 # iterator
class LinkedListIterator:
    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            item = self.current.data
            self.current = self.current.next
            return item


class Ll:
    def __init__(self):
        self.head = None

    def __iter__(self):
        return LinkedListIterator(self.head)

    def append(self, new_node):
        if self.head:
            temp_node = self.head
            while temp_node.next is not None:
                temp_node = temp_node.next

            temp_node.next = new_node
        else:
            self.head = new_node

    def is_empty(self):
        return self.head is None

    def __len__(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def __getitem__(self, index):
        pos = 0
        current = self.head
        if self.__len__() <= index:
            print('There is no such index')
            return None
        while pos is not index:
            current = current.next
            pos += 1
        return current.data

    def addFront(self, other):
        if self.head is None:
            self.head = Node(other)
        else:
            rest = self.head
            self.head = Node(other)
            self.head.next = rest

    def insert_at_end(self, item):
        if self.is_empty():
            self.append(item)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(item,None)

    def count_amount(self, search_for):
        current = self.head
        count = 0
        while current:
            if current.item == search_for:
                count += 1
            current = current.next
        return count

    def copy(self):
        result = Ll()
        buffer = self.head
        while buffer:
            result.append(buffer.item)
            buffer = buffer.next
        return result

    def insert(self, item, position):
        position = position-1
        if position > self.__len__() or position < 0:
            print('Maintain the correct position, the length of the array from 1 to', self.__len__())
            return None
        if position == 0:
            self.head = Node(item, self.head)
        elif position == self.__len__():
            self.insert_at_end(item)
        else:
            i = 0
            current = self.head
            while current.next:
                if i == position - 1:
                    current.next = Node(item, current.next)
                current = current.next
                i += 1

    def delete(self, value):

        current = self.head
        previous = None
        while current and current.item != value:
            previous = current
            current = current.next
        if current:
            if previous is None:
                self.head = self.head.next
            else:
                previous.next = current.next
        else:
            raise ValueError('Value not present in the LinkedList')

    def clear(self):
        temp = self.head
        if temp is None:
            raise IndexError('Empty LinkedList')
        while temp:
            self.head = temp.next
            temp = self.head

    def index(self, item):
        pos = 0
        current = self.head
        found = False
        while current and not found:
            if current.item == item:
                found = True
            else:
                current = current.next
                pos += 1
        if not found:
            raise ValueError('The number is not found in the letter')
        return pos

    def delete_index(self, index):
        index = index - 1
        i = 0
        current = self.head
        previous = None
        while current and i != index:
            previous = current
            current = current.next
            i += 1
        if current:
            if previous is None:
                self.head = self.head.next
            else:
                previous.next = current.next
        else:
            raise ValueError('Index not present in the LinkedList')

    def delete_between_pos(self, index1, index2):
        if index2 > self.__len__() or index1 > index2:
            raise ValueError('Index2 not present in the LinkedList and index2 mast be bigger than index1.')
        for i in range(index2 - index1 + 1):
            self.delete_index(index1)

    def pop(self):
        current = self.head
        if current is None:
            raise IndexError('Empty LinkedList')
        if current.next is None:
            self.clear()
            return
        while current.next:
            if current.next.next is None:
                current.next = None
            else:
                current = current.next

    def sum_or_swap(lelf, a):
        t = False
        for i in range(a.__len__() - 1):
            if a.__getitem__(i) * a.__getitem__(i + 1) < 0:
                t = True
            else:
                t = False
                break
        if t:
            my_list_1 = Ll()
            s = 0
            for i in range(a.__len__()):
                if a.__getitem__(i) > 0:
                    s = s + a.__getitem__(i)
            my_list_1.append(Node("The sum of positive elements \n"))
            my_list_1.append(Node(s))
            return my_list_1
        else:
            my_list_2 = Ll()
            my_list_2.append(Node("Negative and positive elements do not alternate in the array \n"))
            for i in range(a.__len__()):
                if a.__getitem__(i) < 0:
                    my_list_2.append(Node(a.__getitem__(i)))
            return my_list_2


