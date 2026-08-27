students = []

while True:
    print("1. 학생 정보 등록 프로그램.")
    print("2. 학생 정보 조회 프로그램.")
    print("3. 학생 정보 삭제 프로그램.")
    print("0. 학생 정보 종료 프로그램")

    cmd = int(input("실행할 프로그램 번호를 입력하시오."))

    if cmd == 1:
        name = input("학생 이름을 입력하시오.")
        
        age = input("학생 나이를 입력하시오.")
        
        score = input("학생 점수를 입력하시오.")

        students.append([name, age, score])

        print(students)
    elif cmd == 2:
        if len(students) == 0:
            print("조회할 학생 정보가 없습니다.")
            continue

        for i in range(len(students)):
            print(f"학생 이름은 {students[i][0]}이고, 학생 나이는 {students[i][1]}살이고, 학생 점수는 {students[i][2]}점 입니다.")
    elif cmd == 3:
        if len(students) == 0:
                print("조회할 학생 정보가 없습니다.")
                continue
        cmd2 = int(input("삭제할 학생 번호를 입력하시오."))
        cmd2 -= 1
        students.pop(cmd2)

    else:
         print("프로그램을 종료합니다.")
         break
