//A = 1
//AA = 2  A e,i,o,u = 3,4,5,6
//_____  총 3125가지 수
//순서대로 hashmap 으로 저장 ?  그 후 검색
//길이 1~5까지 먼저 돌고 -> 모음 5개 돌기
import java.util.*;
class Solution {
    String [] chars = {"A","E","I","O","U"};
    ArrayList<String> list = new ArrayList<>();
    
    public int solution(String word) {
        int answer = 0;
        
        dfs(word,0,"");
        
        for (int i = 0; i< list.size();i++){
            if(list.get(i).equals(word)){
                answer = i;
                break;
            }
        
        }
        
        return answer;
    }
    public void dfs(String word, int depth, String str){
        list.add(str);
        if(depth == 5){
            return;
        }
        for (int i = 0; i < chars.length;i++){
            dfs(word,depth + 1, str + chars[i]);
        }
    }
}