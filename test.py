import pytest
from stack import Stack

def test_push_and_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    assert stack.pop() == 1

def test_peek():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.peek() == 2
    assert stack.peek() == 2

def test_is_empty():
    stack = Stack()
    assert stack.is_empty() == True
    stack.push(1)
    assert stack.is_empty() == False

def test_size():
    stack = Stack()
    assert stack.size() == 0
    stack.push(1)
    stack.push(2)
    assert stack.size() == 2

# Bonus tests
def test_stack_with_limit():
    stack = Stack(limit=2)
    stack.push(1)
    stack.push(2)
    with pytest.raises(Exception):
        stack.push(3)

def test_search():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.search(2) == 1
    assert stack.search(4) == -1

def test_full_and_empty():
    stack = Stack(limit=2)
    assert stack.is_empty() == True
    assert stack.is_full() == False
    stack.push(1)
    stack.push(2)
    assert stack.is_empty() == False
    assert stack.is_full() == True