import os
from collections.abc import Iterable, Iterator
class Iterator2(Iterator):
    _index: int = None
    _reverse: bool = False
    def __init__(self, collection, reverse: bool = False):
        self._collection = collection
        print("inicializa iterator")
        self._reverse = reverse
        self._index = -1 if reverse else 0

    def __next__(self):
        print("obtiene siguiente elemento")
        try:
            result = self._collection[self._index]
            self._index += -1 if self._reverse else 1
            return result
        except IndexError:
            print("<eol>")
            raise StopIteration

class Collection(Iterable):
    def __init__(self):
        self._items = []

    def __len__(self):
        return len(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __iter__(self):
        return Iterator2(self._items)

    def get_reverse_iterator(self):
        return Iterator2(self._items, True)
    
    def add_item(self, item):
        print("Agrega item %s" % (item))
        self._items.append(item)

    


os.system("clear")

#*--------- Crea colección
collection = Collection()
collection.add_item('Item 1')
collection.add_item('Item 2')
collection.add_item('Item 3')

#*-------- La recorre

for item in collection:
     print(item)
print("\n")



print("Imprimiendo al reverso:")
rever=collection.get_reverse_iterator()
for item in rever:
    print(item)


print("\n")

