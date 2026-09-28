import unittest
from todolist import Todo, TodoList

class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.todo1 = Todo("Buy milk")
        self.todo2 = Todo("Clean room")
        self.todo3 = Todo("Go to the gym")

        self.todos = TodoList("Today's Todos")
        self.todos.add(self.todo1)
        self.todos.add(self.todo2)
        self.todos.add(self.todo3)

    # your tests go here

    def test_length(self):
        # Contract: A TodoList containing three Todos reports a length of 3.
        self.assertEqual(3, len(self.todos))

    def test_to_list(self):
        # Contract: to_list() exposes the Todos as a list in the same collection order.
        self.assertEqual(self.todos.to_list(), [self.todo1, self.todo2, self.todo3])

    def test_first(self):
        # Contract: return the exact object stored at the first position
        self.assertIs(self.todos.first(), self.todo1)

    def test_last(self):
        # Contract: last() returns the final Todo in collection order.
        self.assertIs(self.todos.last(), self.todo3)

    def test_all_done(self):
        #Contract: all_done should be false.
        self.assertFalse(self.todos.all_done())

    def test_add_invalid(self):
        #Contract: This action must terminate by raising TypeError.
        with self.assertRaises(TypeError):
            self.todos.add(1) #Notice how its "Python will raise a TypeError if you do this wrong line"

        with self.assertRaises(TypeError):
            self.todos.add("hi")

    def test_todo_at(self):
        #Contract: return the Todo at a valid index, or raise IndexError when the index identifies no Todo
        self.assertEqual(self.todo1, self.todos.todo_at(0))
        self.assertEqual(self.todo3, self.todos.todo_at(2))
        with self.assertRaises(IndexError):
            self.todos.todo_at(3)


    def test_mark_done_at(self):

        #Contract: should change exactly one Todo’s done state and leave the others unchanged.

        with self.assertRaises(IndexError):
            self.todos.mark_done_at(6)

        self.todos.mark_done_at(1)
        self.assertFalse(self.todo1.done)
        self.assertTrue(self.todo2.done)
        self.assertFalse(self.todo3.done)

    def test_mark_undone_at(self):
        #Contract: selected Todo changes from done to undone, while the others stay done.

        with self.assertRaises(IndexError):
            self.todos.mark_undone_at(6)

        self.todo1.done = True
        self.todo2.done = True
        self.todo3.done = True
        
        self.todos.mark_undone_at(1)
        self.assertTrue(self.todo1.done)
        self.assertFalse(self.todo2.done)
        self.assertTrue(self.todo3.done)
        

    def test_mark_all_done(self):
        #Contract: change the whole collection
        self.todos.mark_all_done()
        self.assertTrue(self.todo1.done)
        self.assertTrue(self.todo2.done)
        self.assertTrue(self.todo3.done)
        self.assertTrue(self.todos.all_done())


    def test_remove_at(self):
        #Contract: targeted deletion + preservation of the survivors + order preservation + invalid-index exception
        with self.assertRaises(IndexError):
            self.todos.remove_at(6)

        self.todos.remove_at(1)
        self.assertEqual(self.todos.to_list(),[self.todo1, self.todo3])

    def test_str(self):

        #Contract: __str__ turns the current TodoList state into a textual representation. 
        #Different states should project to different strings.
        string = (
        "----- Today's Todos -----\n"
        "[ ] Buy milk\n"
        "[ ] Clean room\n"
        "[ ] Go to the gym"
        )
        self.assertEqual(string, str(self.todos))

    def test_str_done_todo(self):

        string = (
        "----- Today's Todos -----\n"
        "[ ] Buy milk\n"
        "[X] Clean room\n"
        "[ ] Go to the gym"
        )
        self.todos.mark_done_at(1)
        self.assertEqual(string, str(self.todos))

    def test_str_all_done_todos(self):

        string = (
        "----- Today's Todos -----\n"
        "[X] Buy milk\n"
        "[X] Clean room\n"
        "[X] Go to the gym"
         )
        self.todos.mark_all_done()
        self.assertEqual(string, str(self.todos))

    def test_each(self):
        #Contract: each iterates over the elements in todos
        result = []
        self.todos.each(result.append)

        self.assertEqual([self.todo1, self.todo2, self.todo3], result)

    def test_select(self):
        #Contract: select() traverses the source TodoList, asks a predicate about each Todo, 
        #and builds a new TodoList from the objects for which the predicate is true.

        self.todo1.done = True
        selected = self.todos.select(lambda todo: todo.done)
        self.assertEqual("----- Today's Todos -----\n[X] Buy milk", str(selected))


    
if __name__ == "__main__":
    unittest.main()