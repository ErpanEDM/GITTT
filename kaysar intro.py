print("欢迎来到Kaysar加密系统")
kirguz = input("请输入一串字符串:")
surguz = int(input("位移量:"))
for c in kirguz:
      if "a" <= c <= "z":
            print(chr(ord("a") + (ord(c) - ord("a") + surguz) %26), end= "")
      elif "A" <= c <= "Z":
            print(chr(ord("A") + (ord(c) - ord("A") + surguz) %26), end= "")
      else:
            print(c,  end= "")
