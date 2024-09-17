def is_possible(channel, broken_buttons):
    for ch in str(channel):
        if int(ch) in broken_buttons:
            return False
    return True

def min_button_presses(target_channel, broken_buttons):
    min_presses = abs(target_channel - 100)  # +, - 버튼만으로 이동하는 경우

    for channel in range(1000000):  # 채널 범위 설정
        if is_possible(channel, broken_buttons):
            presses = len(str(channel)) + abs(channel - target_channel)
            min_presses = min(min_presses, presses)

    return min_presses

# 입력 받기
target_channel = int(input())
broken_count = int(input())
if broken_count > 0:
    broken_buttons = set(map(int, input().split()))
else:
    broken_buttons = set()

# 결과 출력
print(min_button_presses(target_channel, broken_buttons))