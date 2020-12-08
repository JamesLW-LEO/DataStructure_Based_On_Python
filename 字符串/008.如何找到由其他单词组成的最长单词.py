"""
给定一个字符串数组 找出数组中最长的字符串 使其能由数组中其他的字符串组成
例如给定字符串数组 ["test","tester","testertest","testing","apple","seattle","banana","batting","ngcat","batti","bat","testingtester","testbattingcat"]
满足要求的字符串 testbattingcat  组成的字符串 test batti ngcat
"""


class LongestWord():
    def find(self, strArray, strs):
        """
        判断字符串strs是否在字符串数组中
        :param strArray:
        :param strs:
        :return:
        """
        i = 0
        while i < len(strArray):
            if strs == strArray[i]:
                return True
            i += 1
        return False

    def isContian(self, strArray, word, length):
        lens = len(word)
        if lens == 0:
            return True
        i = 1
        while i < lens:
            if i == length:
                return False
            strs = word[0:i]
            if self.find(strArray, strs):
                if self.isContian(strArray, word[i:], length):
                    return True
            i += 1
        return False

    def getLongestStr(self, strArray):
        strArray = sorted(strArray, key=len, reverse=True)
        print(strArray)
        i = 0
        while i < len(strArray):
            if self.isContian(strArray, strArray[i], len(strArray[i])):
                return strArray[i]
            i += 1
        return None


if __name__ == '__main__':
    strArray = ["test", "tester", "testertest", "testing", "apple", "seattle", "banana", "batting", "ngcat", "batti",
                "bat", "testingtester", "testbattingcat"]
    l = LongestWord()
    longestStr = l.getLongestStr(strArray)
    if longestStr != None:
        print(longestStr)
    else:
        print('不存在了')
