def is_channel_reachable(channel,broken_buttons):
    channel_str=str(channel)
    for char in channel_str:
        if int(char) in broken_buttons:
            return False
    return True

def minimum_button_presses(N,broken_buttons):
    current_channel=100
    min_presses=abs(N-current_channel)
    for channel in range(max(0,N-500000),N+500000):
        if is_channel_reachable(channel,broken_buttons):
            presses=len(str(channel))+abs(N-channel)
            min_presses=min(min_presses, presses)
    return min_presses

N=int(input())
M=int(input())
if M > 0:
    broken_buttons=set(map(int, input().split()))
else:
    broken_buttons=set()

result=minimum_button_presses(N,broken_buttons)
print(result)