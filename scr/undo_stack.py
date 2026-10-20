import time


class ActionNode:
    __slots__ = ("action_id", "name", "timestamp", "below")

    def __init__(self, action_id, name):
        self.action_id = action_id
        self.name = name
        self.timestamp = time.strftime("%H:%M:%S")
        self.below = None  # node underneath this one in the stack


class UndoStack:
    def __init__(self):
        self._head = None
        self._count = 0

    def _nodes(self):
        node = self._head
        while node:
            yield node
            node = node.below

    def pushAction(self, action_id, name):
        node = ActionNode(action_id, name)
        node.below, self._head = self._head, node
        self._count += 1
        return node

    def undoAction(self):
        if not self._head:
            return None
        removed = self._head
        self._head = removed.below
        removed.below = None
        self._count -= 1
        return removed

    def currentAction(self):
        return self._head

    def displayHistory(self):
        if not self._head:
            print("History is empty.")
            return
        print("TOP")
        for node in self._nodes():
            print(f"  [{node.action_id}] {node.name} ({node.timestamp})")

    def countActions(self):
        return sum(1 for _ in self._nodes())


MENU = (
    "\n1. Perform Action"
    "\n2. Undo Action"
    "\n3. View Current Action"
    "\n4. Display Full History"
    "\n5. Exit"
)


def main():
    stack = UndoStack()
    counter = 1

    while True:
        print(MENU)
        choice = input("Choice: ").strip()

        if choice == "1":
            name = input("Action name: ").strip()
            stack.pushAction(counter, name)
            counter += 1
            print("Action performed.")
        elif choice == "2":
            node = stack.undoAction()
            print(f"Undo: {node.name}" if node else "Nothing to undo.")
        elif choice == "3":
            node = stack.currentAction()
            print(f"Current: {node.name} ({node.timestamp})" if node else "No actions.")
        elif choice == "4":
            stack.displayHistory()
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
