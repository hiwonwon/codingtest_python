class Solution {
    public int solution(int n, int k) {
        int answer = 0;
        int mok = n / 10;
        k = k - mok;
            
        answer = 12000 * n + k * 2000;
        return answer;
    }
}