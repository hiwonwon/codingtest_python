class Solution {
    public int[] solution(long n) {
        String sn = String.valueOf(n);
        int[] answer = new int[sn.length()];

        
        for (int i = sn.length()-1,idx=0; i>=0 ; i--,idx++){
            answer[idx] = (sn.charAt(i)-'0');
        }
        return answer;
        
    }
}