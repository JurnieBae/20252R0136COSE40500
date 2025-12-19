# 파일 쓰기
with open("sample.txt", "w") as f:
    f.write("Hello, this is a test file!")

# 파일 읽기
with open("sample.txt", "r") as f:
    content = f.read()
    print(content)