# -*- coding: utf-8 -*-
"""
检查点 1：基础复利程序
公式：A = P * (1 + r) ** t
测试数据：本金 P=10000 元，年利率 r=5%，期限 t=3 年
预期输出：11576.25
"""

# 输入参数（课堂作业固定测试数据）
principal = 10000      # 本金 P（元）
rate = 0.05            # 年利率 r（5%）
years = 3              # 期限 t（年）

# 复利计算：每年计息一次，本息滚动计入下一年
amount = principal * (1 + rate) ** years

# 输出（保留两位小数，对应“分”）
print("本金：%.2f 元" % principal)
print("年利率：%.2f%%" % (rate * 100))
print("期限：%d 年" % years)
print("复利公式：A = P * (1 + r) ** t")
print("3 年后本息合计：%.2f 元" % amount)
