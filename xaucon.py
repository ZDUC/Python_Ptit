def count_strings(N, M, s):
    MOD = M
    n = len(s)

    # Tạo một mảng để lưu số lượng xâu con của s có độ dài i kết thúc bằng ký tự j
    dp = [[0] * 26 for _ in range(n + 1)]
    
    # Khởi tạo dp cho độ dài xâu con là 0
    for j in range(26):
        dp[0][j] = 0
    
    # Thiết lập dp cho độ dài xâu con là 1
    dp[0][ord(s[0]) - ord('a')] = 1
    
    # Tính dp cho các độ dài xâu con từ 1 đến n
    for i in range(1, n):
        for j in range(26):
            dp[i][j] = dp[i - 1][j]
        
        dp[i][ord(s[i]) - ord('a')] += 1
    
    # Tính số lượng xâu t thỏa mãn yêu cầu
    result = 0
    
    # Duyệt qua từng vị trí trong xâu t
    for i in range(N):
        # Lấy ký tự tại vị trí i trong xâu t
        char = s[i % n]
        
        # Lấy số lượng xâu con của s có độ dài i + 1 kết thúc bằng ký tự char
        count = dp[n - 1][ord(char) - ord('a')]
        
        # Tính số cách để đặt ký tự char vào vị trí i trong xâu t
        ways_to_fill_char = pow(26, N - i - 1, MOD)
        
        # Tính số lượng xâu t thỏa mãn yêu cầu cho vị trí i
        result = (result + count * ways_to_fill_char) % MOD

    return result

# Đọc số lượng bộ test
T = int(input())

# Xử lý từng bộ test
for _ in range(T):
    N, M = map(int, input().split())
    s = input().strip()
    answer = count_strings(N, M, s)
    print(answer)