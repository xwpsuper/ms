import string


class Hangman(object):
    errs = {
        1: '请输入一个英文字母: ',
        2: '请输入英文字母: ',
        3: '输入不能为空, 请继续输入: ',
    }

    def __init__(self, word, guessed=[]):
        self.guessed = guessed
        self.word = word


    def print_status(self):
        toguess = ' '.join([ch if ch in self.guessed else '_' for ch in self.word])
        print(f'单词 {toguess} 输入字母猜测是否在单词内:')

    def get_input(self):
        char = input().strip()
        errcode = 0
        if len(char) > 1:
            errcode = 1
        elif char not in string.ascii_letters:
            errcode = 2
        elif len(char) == 0:
            errcode = 3

        if errcode == 0:
            return char
        else:
            print(self.errs[errcode])
            return self.get_input()

    def check_success(self):
        return len(set(self.word) - set(self.guessed)) == 0


    def print_summary(self):
        count = len(self.guessed)
        seqs = ', '.join(self.guessed)
        errs = [ch for ch in self.guessed if ch not in self.word]
        errcount = len(errs)
        errs = ', '.join(errs)
        print((f'恭喜你猜中了英文单词 {self.word}, '
            f'共猜了{count}次, 依次猜测了{seqs}, '
            f'猜错次数{errcount}({errs})'))

    def play(self):
        while True:
            self.print_status()
            char = self.get_input()
            self.guessed.append(char)
            if char not in self.word:
                print(f'很遗憾, {char}不在该单词中')
            elif self.check_success():
                self.print_summary()
                break


if __name__ == '__main__':
    Hangman('apple').play()
