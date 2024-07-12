# assert是缩小版的if语句
# 判断值，如果为真则继续向下执行
# 如果条件为假，抛出AssertError异常
# 会尽早的检查出错误，防止漏洞，提高健壮性
math_mark = int(input('input num:'))
assert 0 <= math_mark <= 100
print("number is", math_mark)
