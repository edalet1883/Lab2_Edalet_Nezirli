class Job:

    __slots__ = ("jid", "student", "pages", "after")

    def __init__(self, jid, student, pages):
        self.jid = jid
        self.student = student
        self.pages = pages
        self.after = None     
    def __str__(self):
        return f"job#{self.jid} {self.student} ({self.pages} sehife)"


class JobQueue:
 
    def __init__(self):
        self._head = None 
        self._tail = None   
        self._count = 0      
    def submit(self, jid, student, pages):
        job = Job(jid, student, pages)
        if self._tail is None:
            self._head = self._tail = job
        else:
            self._tail.after = job
            self._tail = job
        self._count += 1
        return job

    def process(self):
       
        if self._head is None:
            return None
        job = self._head
        self._head = job.after
        if self._head is None:
            self._tail = None
        job.after = None
        self._count -= 1
        return job

    def front(self):
    
        return self._head
    def is_empty(self):
        return self._head is None

    def __len__(self):
        return self._count
    def show(self):

        if self.is_empty():
            print("  [!] novbe bosdur")
            return
        cur = self._head
        while cur is not None:
            print(f"   {cur}")
            cur = cur.after


MENU = """\
-------------- PRINT QUEUE --------------
|  1 - submit job    2 - print next      |
|  3 - next job      4 - show queue      |
|  5 - pending       6 - quit            |
-----------------------------------------"""


def read_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        return None


def main():
    q = JobQueue()
    next_id = 1
    while True:
        print(MENU)
        choice = input("select> ").strip()

        if choice == "1":
            student = input("student name> ").strip()
            if not student:
                print("  [!] ad bos ola bilmez")
                continue
            pages = read_int("pages> ")
            if pages is None or pages <= 0:
                print("  [!] duzgun sehife sayi daxil edin")
                continue
            print(f"  [+] elave olundu: {q.submit(next_id, student, pages)}")
            next_id += 1

        elif choice == "2":
            job = q.process()
            print(f"  [x] cap olundu: {job}" if job else "  [!] novbe bosdur")

        elif choice == "3":
            job = q.front()
            print(f"  [>] novbeti: {job}" if job else "  [!] novbe bosdur")

        elif choice == "4":
            q.show()
            print(f"  umumi: {len(q)} is")

        elif choice == "5":
            print(f"  gozleyen is sayi: {len(q)}")

        elif choice == "6":
            print("goodbye!")
            break

        else:
            print("  [!] bilinmeyen secim")


if __name__ == "__main__":
    main()
