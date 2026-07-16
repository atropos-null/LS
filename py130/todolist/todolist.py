

class Todo:

    TRUE_COMPLETED = "X"
    FALSE_COMPLETED = " "

    def __init__(self, title):
        self.title = title
        self.done = False

    def __str__(self):
        if self._done:
            return f"[{Todo.TRUE_COMPLETED}] {self.title}"
        return f"[{Todo.FALSE_COMPLETED}] {self.title}"
        
    def title(self):
        return self._title
    
    @property
    def done(self):
        return self._done
    
    @done.setter
    def done(self, bool_value):
        self._done = bool_value


    def __eq__(self, other):
        if not isinstance(other, Todo):
            return NotImplemented
        return self.title == other.title and self.done == other.done
    

class TodoList:

    def __init__(self, title):
        self._title = title
        self._todos = []

    @property
    def title(self):
        return self._title
    
    def __str__(self):
        output_lines = [f'----- {self.title} -----']
        output_lines += [str(todo) for todo in self._todos]
        return '\n'.join(output_lines)

    def add(self, other):
        if not isinstance(other, Todo):
            raise TypeError("Not a Todo Object")
        self._todos.append(other)

    def __len__(self):
        return len(self._todos)
    
    def first(self):
        if self._todos:
            return self._todos[0]
        raise IndexError("Empty list")
    
    def last(self):
        if self._todos:
            return self._todos[-1]
        raise IndexError("Empty list")
    
    def to_list(self):
        return self._todos.copy()
    
    def todo_at(self, value_index):
        if value_index <= len(self._todos):
            return self._todos[value_index]
        raise IndexError

    def mark_done_at(self, value_index):
        if value_index > len(self._todos):
            raise IndexError
        self.todo_at(value_index).done = True

    def mark_undone_at(self, value_index):
        if value_index > len(self._todos):
            raise IndexError
        self.todo_at(value_index).done = False

    def mark_all_done(self):

        def mark_done(todo):
            todo.done = True

        self.each(mark_done)


    def mark_all_undone(self):
       
        def mark_undone(todo):
            todo.done = False

        self.each(mark_undone)

    def all_done(self):
        return all(todo.done for todo in self._todos)
    
    def remove_at(self, value_index):
        if value_index > len(self._todos):
            raise IndexError
        return self._todos.pop(value_index)

    def each(self, callable):

        for item in self._todos:
            callable(item)

    def select(self, callable):
    
        result = TodoList(self.title)

        def choose(item):
            if callable(item):
                result.add(item)
         
        self.each(choose)

        return result

    def find_by_title(self, title):
        
        found = self.select(lambda item: item.title == title)
        return found.todo_at(0)


    def done_todos(self):

        return self.select(lambda item: item.done)
       

    def undone_todos(self):
        return self.select(lambda item: not item.done)

    def mark_done(self, title):
        found = self.find_by_title(title)
        found.done = True

empty_todo_list = TodoList('Nothing Doing')

def setup():
    todo1 = Todo('Buy milk')
    todo2 = Todo('Clean room')
    todo3 = Todo('Go to gym')

    todo2.done = True

    todo_list = TodoList("Today's Todos")
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.add(todo3)

    return todo_list
