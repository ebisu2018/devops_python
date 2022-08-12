'''

assert是缩小版的if语句
判断值，如果为真则继续执
如果条件为假，会抛出AssertError异常
会尽早的检查出错误，防止漏洞，提高健壮性

'''

mathmark = int(input('请输入成绩：'))
assert 0 <= mathmark <= 100
print("数学考试分数为：", mathmark)
