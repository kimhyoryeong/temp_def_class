# -*- coding; utf-8 -*-

import calculation as cal
from arithmetic import plus
from arithmetic import subtract
a = 3
b = 4

def main():
    print("안녕하세요 ,main 입니다.")
    print("a + b = ", plus.add(a,b))
    print("a - b =", subtract.minus(a, b))

if __name__ == "__main__":
    main();

# -*- coding: utf-8 -*-
from arithmetic import plus as pl
from arithmetic import subtract as sub
from datapreprocessing import processing
from datapreprocessing import importData

a = 3
b = 4

def main():
  print("~~ 사칙 연산을 시작합니다 ~~ ")
  print("a + b =", sub.minus(a, b))
  print("a - b =", pl.add(a, b))
  print("~~ 사칙 연산을 종료합니다 ~~ ")

  ## 데이터 전처리 시작
  data = importData.readData()
  processing.process_data(data)

if __name__ == "__main__":
  main()