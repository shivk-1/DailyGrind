from project import add_task, edit_task, remove_task

def test_add_task(monkeypatch):
    # Test adding a task with a different description
    monkeypatch.setattr("builtins.input", lambda _: "read a book")
    tasks, task_number = add_task([], 0)
    assert tasks == [{"Task Number": 1, "Task": "read a book"}] and task_number == 1

    # Test adding another task to ensure task numbering works
    monkeypatch.setattr("builtins.input", lambda _: "finish homework")
    tasks, task_number = add_task(tasks, task_number)
    assert tasks == [{"Task Number": 1, "Task": "read a book"}, {"Task Number": 2, "Task": "finish homework"}] and task_number == 2

def test_edit_task(monkeypatch):
    # Test editing an existing task
    inputs = iter(["2", "study for exams"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    tasks = edit_task([{"Task Number": 1, "Task": "read a book"}, {"Task Number": 2, "Task": "finish homework"}])
    assert tasks == [{"Task Number": 1, "Task": "read a book"}, {"Task Number": 2, "Task": "study for exams"}]

    # Test updating a task to an empty string
    inputs = iter(["1", ""])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    tasks = edit_task(tasks)
    assert tasks == [{"Task Number": 1, "Task": ""}, {"Task Number": 2, "Task": "study for exams"}]

def test_remove_task(monkeypatch):
    # Test removing the first task
    monkeypatch.setattr("builtins.input", lambda _: "1")
    tasks = remove_task([{"Task Number": 1, "Task": "read a book"}, {"Task Number": 2, "Task": "finish homework"}])
    assert tasks == [{"Task Number": 2, "Task": "finish homework"}]

    # Test removing the last remaining task
    monkeypatch.setattr("builtins.input", lambda _: "2")
    tasks = remove_task(tasks)
    assert tasks == []