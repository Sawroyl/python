try:
    with open("examply.txt", 'r') as f:
        data = f.read()
        print(data)
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(f"Error occurred:{e}")
