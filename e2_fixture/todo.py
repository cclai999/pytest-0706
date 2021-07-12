
class Tasks:
    def __init__(self, items=None):
        self._tasks = items if items is not None else []

    def get_tasks(self):
        return self._tasks

    def get_task(self, task_id):
        task = [x for x in self._tasks if x['id'] == task_id]
        if len(task) == 0:
            return False
        return task[0]

    def create_task(self, item):
        task = {
            'id': self._tasks[-1]['id'] + 1,
            'title': item['title'],
            'note': item.get('note', ''),
            'done': False
        }
        self._tasks.append(task)
        return task['id']

    def delete_task(self, task_id):
        task = [x for x in self._tasks if x['id'] == task_id]
        if len(task) == 0:
            return False
        self._tasks.remove(task[0])
        return True

    def update_task(self, task_id, item):
        task = [x for x in self._tasks if x['id'] == task_id]
        if len(task) == 0:
            return False
        task[0]['title'] = item.get('title', task[0]['title'])
        task[0]['note'] = item.get('note', task[0]['note'])
        task[0]['done'] = item.get('done', task[0]['done'])
        return True

    def __len__(self):
        """The len of task"""
        return len(self._tasks)


if __name__ == '__main__':
    pass
