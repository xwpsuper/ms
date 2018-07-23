'''
python习题，做一个命令行的猜字谜游戏
1. 游戏开始时，产生一个英文单词(可以预先准备好词库), 比如guess, 并在屏幕上打印 "单词 _ _ _ _ _ , 输入字母猜测是否在单词内: "(下划线的个数为单词的长度)
2. 接受键盘输入, 若大于1个字母，打印"请输入一个字母: "
               若非英文字母, 打印"请输入英文字母: "
               若为空, 打印"输入不能为空, 请继续输入: "
3. 比较输入的字母是否在单词里面, 如果在, 比如输入了'e', 则在屏幕上打印 "单词 _ _ e _ _, 输入字母猜测是否在单词内: "
                           如果不在, 打印"很遗憾, 'e'不在该单词中", 回到步骤1
4. 当所有字母都被猜出时， 打印 "恭喜你猜中了英文单词 guess, 共猜了5次, 依次猜测了a, e, s, g, u, 猜错次数1(a)"
'''

class Humman(object):
    def __init__(self, word, guessed = []):
        self.word = word
        self.guessed = guessed

    def status(self):
        pass

    def input_f(self):
        pass

    def success(self):
        pass