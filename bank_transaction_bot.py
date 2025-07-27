balance = 10000

while True:
    num = input("사용하실 기능의 번호를 선택해주세요 (1. 입금 2. 출금 3. 잔액확인 4. 종료) : ")

    if num == "4":
        print(f"서비스를 종료합니다. 현재 잔액은 {balance}원입니다.")
        break
    
    if num == '1':
        deposit_amount = input('입금할 금액을 입력해주세요: ')
        deposit_amount = int(deposit_amount)
        balance += deposit_amount
        print(f"입금한 금액은 {deposit_amount}원이고, 현재 잔액은 {balance}원입니다.")
        
    elif num == '2':
        withdraw_amount = input('출금할 금액을 입력해주세요: ')
        withdraw_amount = int(withdraw_amount)
        actual_withdraw = min(balance, withdraw_amount)
        balance -= actual_withdraw
        print(f"출금한 금액은 {actual_withdraw}원이고, 현재 잔액은 {balance}원입니다.")

    elif num == '3':
        print(f"현재 잔액은 {balance}원입니다.")
    else:
        print("잘못된 입력입니다. 1~4 중에서 선택해주세요.")

