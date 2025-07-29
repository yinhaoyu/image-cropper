#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
For循环示例
包含多种常见的for循环用法
"""

def basic_for_loop():
    """基础for循环 - 遍历数字范围"""
    print("=== 基础for循环 ===")
    for i in range(5):
        print(f"第{i+1}次循环，i = {i}")

def range_for_loop():
    """使用range()的for循环"""
    print("\n=== 使用range()的for循环 ===")
    # 指定起始值和结束值
    for i in range(1, 6):
        print(f"i = {i}")
    
    # 指定步长
    print("\n使用步长:")
    for i in range(0, 10, 2):
        print(f"i = {i}")

def list_for_loop():
    """遍历列表的for循环"""
    print("\n=== 遍历列表 ===")
    fruits = ["苹果", "香蕉", "橙子", "葡萄"]
    for fruit in fruits:
        print(f"我喜欢吃{fruit}")

def enumerate_for_loop():
    """使用enumerate()获取索引和值"""
    print("\n=== 使用enumerate() ===")
    colors = ["红色", "绿色", "蓝色", "黄色"]
    for index, color in enumerate(colors):
        print(f"第{index+1}个颜色是: {color}")

def dict_for_loop():
    """遍历字典的for循环"""
    print("\n=== 遍历字典 ===")
    person = {
        "name": "张三",
        "age": 25,
        "city": "北京"
    }
    
    # 遍历键
    print("遍历键:")
    for key in person.keys():
        print(f"键: {key}")
    
    # 遍历值
    print("\n遍历值:")
    for value in person.values():
        print(f"值: {value}")
    
    # 遍历键值对
    print("\n遍历键值对:")
    for key, value in person.items():
        print(f"{key}: {value}")

def nested_for_loop():
    """嵌套for循环"""
    print("\n=== 嵌套for循环 ===")
    for i in range(1, 4):
        for j in range(1, 4):
            print(f"i={i}, j={j}, 乘积={i*j}")
        print("---")

def for_else_loop():
    """for-else循环"""
    print("\n=== for-else循环 ===")
    numbers = [2, 4, 6, 8, 10]
    search_num = 5
    
    for num in numbers:
        if num == search_num:
            print(f"找到了数字 {search_num}")
            break
    else:
        print(f"没有找到数字 {search_num}")

def list_comprehension():
    """列表推导式（基于for循环）"""
    print("\n=== 列表推导式 ===")
    # 传统for循环
    squares = []
    for i in range(1, 6):
        squares.append(i ** 2)
    print(f"传统for循环: {squares}")
    
    # 列表推导式
    squares_comp = [i ** 2 for i in range(1, 6)]
    print(f"列表推导式: {squares_comp}")

def main():
    """主函数，运行所有for循环示例"""
    print("For循环示例程序")
    print("=" * 30)
    
    basic_for_loop()
    range_for_loop()
    list_for_loop()
    enumerate_for_loop()
    dict_for_loop()
    nested_for_loop()
    for_else_loop()
    list_comprehension()
    
    print("\n程序结束")

if __name__ == "__main__":
    main()