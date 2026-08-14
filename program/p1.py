# name = input("이름을 입력하세요: ")
# print(f"안녕하세요, {name}님! 활동 기록을 시작합니다.")
# 함수가 받아오는 값을 매개변수로 넣음 / 함수 안에서 쓰는 변수들이랑은 다른 개념

import re   # 정규표현식 모듈
records = []
next_id = 1

def validate_date(s: str) -> bool: # s는 문자열로 쓰일 것임을 약속 & bool : T/F
    if not isinstance(s, str):  # isinstance()는 첫 번째가 두 번째의 인스턴스인지 확인 : s가 문자열 아니면 False
        return False
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", s): # 정규표현식으로 YYYY 4자리숫자, MM 2자리, DD 2자리 아니면 False
        return False
    try:    # 실행할 코드 : 코드 실행하다가 오류 날 수 있는 상황 처리할 때 쓰임 : 근데 여기선 더 안전하게 하려는 코드
        y, m, d = map(int, s.split("-"))    # map: 여러값 한꺼번에 변환, 문자열을 -기준으로 나누고 map 처리해서 y, m, d에 할당  
    except ValueError:  # 예외 발생 시 실행
        return False
    if y < 0 or m < 1 or m > 12 or d < 1 or d > 31: # 월은 1~12, 일은 1~31 아니면 False
        return False
    return True


def validate_spent_time(s: str) -> bool:
    if not isinstance(s, str):
        return False
    if not re.match(r"^\d{2}:\d{2}$", s):
        return False
    try:
        hh, mm = map(int, s.split(":"))
    except ValueError:
        return False
    if hh < 0 or hh > 24 or mm < 0 or mm > 59:
        return False
    return True


def input_validation(prompt: str, validator, input_func=input) -> str: # 매개변수 목록
    # 입력값 검증 함수, prompt: 입력 안내 메시지, validator: 검증 함수, input_func: 입력 함수
    # prompt는 문자열로 쓰일 것을 약속, validator는 입력값 검증하는 함수, input_func는 입력 받는 함수
    
    while True: 
        v = input_func(prompt).strip() # input_func로 prompt 입력받고 앞뒤 공백 제거 
        if validator(v):    # 검증 완료되면 v 반환
            return v
        print("형식 오류! 다시 확인하고 입력해주세요.") # 재입력 요구

def add_record(records: list, next_id: int, input_func=input) -> tuple: # input_func는 기본으로 input() 함수 사용 
    date = input_validation("날짜(YYYY-MM-DD): ", validate_date, input_func)    # prompt = "날짜(YYYY-MM-DD): ", validator = validate_date, input_func = input_func
    activity = input_func("활동: ").strip() # 앞뒤 공백 제거
    duration = input_validation("소요시간(HH:MM): ", validate_spent_time, input_func)
    memo = input_func("메모: ").strip() 

    entry = { # dict 형태로 기록 저장 (dict 이름은 entry)
        "id": next_id,
        "date": date,
        "duration": duration,
        "activity": activity,
        "memo": memo,
    }
    records.append(entry)   # 리스트 끝에 entry 추가
    print("저장됨:", entry) 
    return entry, next_id + 1   # entry, next_id + 1 튜플로 반환 (만든 새로운 기록, 다음 id를 돌려준다.)

def view_records(records: list): 
    print("\n<전체 기록 조회:>\n")
    # records가 비어있으면 "기록이 없습니다." 출력 후 함수 종료
    if not records: 
        print("기록이 없습니다.\n") 
        return
    
    for e in records:   # {}는 dict
        print(f"[{e['id']}] {e['date']} | {e['activity']} | {e['duration']} | {e['memo']}\n") 

def menu(records: list, next_id: int): 
    print("\n<메뉴>\n")
    print("1. 기록 추가")
    print("2. 전체 기록 조회")
    print("7. 종료\n")
    choice = input("선택하세요 (1-7): ").strip()
            
    if choice == "1":
        _, next_id = add_record(records, next_id)
    elif choice == "2":
        view_records(records)
    elif choice == "7":
        print("일일기록을 종료합니다.")
    else:
        print("다시 시도해주세요.")
        
    return choice, next_id  # 전역변수를 main한테 전달해야함
            
def main():
    global next_id
    while True:
        choice, next_id = menu(records, next_id) 
        if choice == "7":
            break
        


if __name__ == "__main__":
    main()
    
    
