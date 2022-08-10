def Machine(fn):
    def wrapper(*args, **kwargs):
        v = fn(*args, **kwargs)
        v.send(None)
        return v

    return wrapper


# definir estados
class Estado:

    def __init__(self):
        self.start = self._create_start()
        self.q1 = self._create_q1()
        self.q2 = self._create_q2()
        self.q3 = self._create_q3()

        self.current_state = self.start
        self.stopped = False

    def send(self, char):
        try:
            self.current_state.send(char)
        except StopIteration:
            self.stopped = True

    def does_match(self):
        if self.stopped:
            return False
        return self.current_state == self.q3

    # estados

    @Machine
    def _create_start(self):
        while True:
            char = yield
            if char == 'a':
                self.current_state = self.q1
            elif char == 'b':
                self.current_state = self.q3
            else:
                break

    @Machine
    def _create_q1(self):
        while True:
            char = yield
            if char == 'a':
                self.current_state = self.q1
            elif char == 'b':
                self.current_state = self.q2
            else:
                break

    @Machine
    def _create_q2(self):
        while True:
            char = yield
            if char == 'b':
                self.current_state = self.q3
            elif char == 'a':
                self.current_state = self.q1
            else:
                break

    @Machine
    def _create_q3(self):
        while True:
            char = yield
            if char == 'b':
                self.current_state = self.q3
            elif char == 'a':
                self.current_state = self.q1
            else:
                break


def grep_regex(text):
    evaluator = Estado()
    for ch in text:
        evaluator.send(ch)
    return evaluator.does_match()


# ler arquivos txt

if __name__ == '__main__':

    with open("text") as file:
        for line in file:
            print(f"{line.rstrip()}: {grep_regex(line.rstrip())}")

    file.close()

if __name__ == '__main__':

    with open("text2") as file:
        for line in file:
            print(f"{line.rstrip()}: {grep_regex(line.rstrip())}")

    file.close()

if __name__ == '__main__':

    with open("text3") as file:
        for line in file:
            print(f"{line.rstrip()}: {grep_regex(line.rstrip())}")

    file.close()