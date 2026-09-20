# -*- coding: utf-8 -*-
"""
检查点 3：30 年复利 vs 单利差额比较
单利公式：A_simple = P * (1 + r * t)
复利公式：A_compound = P * (1 + r) ** t
测试数据：本金 10000 元，年利率 5%，期限 30 年
预期：复利 43219.42，单利 25000.00，差额 18219.42
"""

principal = 10000
rate = 0.05
years = 30

amount_simple = principal * (1 + rate * years)
amount_compound = principal * (1 + rate) ** years
difference = amount_compound - amount_simple

print("本金：%.2f 元，年利率：%.2f%%，期限：%d 年" % (principal, rate * 100, years))
print("-" * 40)
print("单利本息：%.2f 元" % amount_simple)
print("复利本息：%.2f 元" % amount_compound)
print("-" * 40)
print("复利比单利多：%.2f 元" % difference)
