class ContiguousList:
    def __init__(self, capacity):
        """
        Initialize a ContiguousList with a specified capacity.
        
        Attributes:
            capacity (int): Initial capacity of the list.
            size (int): Current number of elements in the list.
            list (list): Underlying array to store list elements.
        """
        self.capacity = capacity
        self.size = 0
        self.list = [None] * capacity

    def is_empty(self):
        """Check if the list is empty."""
        return self.size == 0

    def is_full(self):
        """Check if the list is full."""
        return self.size == self.capacity

    def resize(self):
        """
        Resize the underlying array to double its current capacity when full.
        """
        new_capacity = self.capacity * 2
        new_list = [None] * new_capacity
        # Copy elements to new list
        for i in range(self.size):
            new_list[i] = self.list[i]
        self.list = new_list
        self.capacity = new_capacity

    def insert(self, element):
        """
        Insert an element at the end of the list, resizing if full.
        
        Args:
            element: Element to be added to the list.
        """
        if self.is_full():
            self.resize()
        self.list[self.size] = element
        self.size += 1

    def remove(self, position):
        """
        Remove the element at a specified position, shifting subsequent elements.
        
        Args:
            position (int): Position of the element to remove.
        
        Raises:
            Exception: If the list is empty.
            IndexError: If the position is out of bounds.
        """
        if self.is_empty():
            raise Exception("List is empty")
        if position < 0 or position >= self.size:
            raise IndexError("Invalid position")
        
        # Shift elements left to fill the gap
        for i in range(position, self.size - 1):
            self.list[i] = self.list[i + 1]
        self.list[self.size - 1] = None  # Clear the last element
        self.size -= 1

    def get(self, position):
        """
        Retrieve the element at a specified position.
        
        Args:
            position (int): Position of the element to retrieve.
        
        Raises:
            IndexError: If the position is out of bounds.
        
        Returns:
            The element at the specified position.
        """
        if position < 0 or position >= self.size:
            raise IndexError("Invalid position")
        return self.list[position]

    def list_size(self):
        """Return the current size of the list."""
        return self.size

# Testing the ContiguousList class
def run_tests():
    print("Starting tests...")
    
    # Test initialization
    clist = ContiguousList(2)
    assert clist.is_empty() == True, "Test Failed: List should be empty initially"
    assert clist.list_size() == 0, "Test Failed: Size should be 0 initially"

    # Test insert and resize
    clist.insert(1)
    clist.insert(2)
    assert clist.list_size() == 2, "Test Failed: Size should be 2 after two inserts"
    clist.insert(3)
    assert clist.list_size() == 3, "Test Failed: Size should be 3 after inserting another element"
    assert clist.capacity == 4, "Test Failed: Capacity should have doubled to 4"

    # Test get
    assert clist.get(0) == 1, "Test Failed: Element at position 0 should be 1"
    assert clist.get(1) == 2, "Test Failed: Element at position 1 should be 2"
    assert clist.get(2) == 3, "Test Failed: Element at position 2 should be 3"

    # Test remove
    clist.remove(1)  # Remove element at position 1
    assert clist.list_size() == 2, "Test Failed: Size should be 2 after removing one element"
    assert clist.get(1) == 3, "Test Failed: Element at new position 1 should be 3"

    # Test is_full and is_empty
    assert clist.is_full() == False, "Test Failed: List should not be full"
    assert clist.is_empty() == False, "Test Failed: List should not be empty after insertions"
    
    # Test remove on empty list raises Exception
    try:
        empty_list = ContiguousList(1)
        empty_list.remove(0)
    except Exception as e:
        assert str(e) == "List is empty", "Test Failed: Removing from empty list should raise 'List is empty'"
    
    print("All tests passed successfully.")

# Run the tests
if __name__ == "__main__":
    run_tests()
