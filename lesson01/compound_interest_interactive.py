# -*- coding: utf-8 -*-
"""
检查点 2：交互版复利计算器
在检查点 1 的基础上改为键盘输入，并对非法输入进行拦截：
  - 本金、年限必须为非负数
  - 年利率不允许为负数（拦截后要求重新输入，直到合法为止）
公式：A = P * (1 + r) ** t
"""


def input_non_negative_float(prompt, allow_zero=True):
    """读取一个非负小数；非法输入（非数字 / 负数）会被拦截并要求重输。"""
    while True:
        text = input(prompt).strip()
        try:
            value = float(text)
        except ValueError:
            print("  [拦截] 输入不是有效数字，请重新输入。")
            continue
        if value < 0 or (not allow_zero and value == 0):
            print("  [拦截] 数值不能为负数，请重新输入。")
            continue
        return value


def input_non_negative_int(prompt):
    """读取一个非负整数。"""
    while True:
        text = input(prompt).strip()
        try:
            value = int(text)
        except ValueError:
            print("  [拦截] 请输入整数年限。")
            continue
        if value < 0:
            print("  [拦截] 年限不能为负数，请重新输入。")
            continue
        return value


print("===== 复利计算器（交互版）=====")
principal = input_non_negative_float("请输入本金（元）：")

# 重点检查项：负利率拦截。利率允许为 0（本金不变），但绝不允许负数。
while True:
    rate_percent = input_non_negative_float("请输入年利率（%，不允许负数）：")
    if rate_percent < 0:
        # 双保险：input_non_negative_float 已拦截负数，这里保留显式判断
        print("  [拦截] 年利率不能为负，请重新输入。")
        continue
    break

years = input_non_negative_int("请输入期限（年，整数）：")

rate = rate_percent / 100
amount = principal * (1 + rate) ** years

print("------------------------------")
print("复利公式：A = %.2f * (1 + %.4f) ** %d" % (principal, rate, years))
print("到期本息合计：%.2f 元" % amount)
