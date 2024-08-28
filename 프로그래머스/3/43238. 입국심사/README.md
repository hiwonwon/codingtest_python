# [level 3] 입국심사 - 43238 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/43238) 

### 성능 요약

메모리: 14.1 MB, 시간: 621.49 ms

### 구분

코딩테스트 연습 > 이분탐색

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 08월 28일 16:22:47

### 문제 설명

<p data-pf_style_display="block" data-pf_style_visibility="visible">n명이 입국심사를 위해 줄을 서서 기다리고 있습니다. 각 입국심사대에 있는 심사관마다 심사하는데 걸리는 시간은 다릅니다. </p>

<p data-pf_style_display="block" data-pf_style_visibility="visible">처음에 모든 심사대는 비어있습니다. 한 심사대에서는 동시에 한 명만 심사를 할 수 있습니다. 가장 앞에 서 있는 사람은 비어 있는 심사대로 가서 심사를 받을 수 있습니다. 하지만 더 빨리 끝나는 심사대가 있으면 기다렸다가 그곳으로 가서 심사를 받을 수도 있습니다.</p>

<p data-pf_style_display="block" data-pf_style_visibility="visible">모든 사람이 심사를 받는데 걸리는 시간을 최소로 하고 싶습니다.</p>

<p data-pf_style_display="block" data-pf_style_visibility="visible">입국심사를 기다리는 사람 수 n, 각 심사관이 한 명을 심사하는데 걸리는 시간이 담긴 배열 times가 매개변수로 주어질 때, 모든 사람이 심사를 받는데 걸리는 시간의 최솟값을 return 하도록 solution 함수를 작성해주세요.</p>

<h5 data-pf_style_display="block" data-pf_style_visibility="visible">제한사항</h5>

<ul data-pf_style_display="block" data-pf_style_visibility="visible">
<li data-pf_style_display="list-item" data-pf_style_visibility="visible">입국심사를 기다리는 사람은 1명 이상 1,000,000,000명 이하입니다.</li>
<li data-pf_style_display="list-item" data-pf_style_visibility="visible">각 심사관이 한 명을 심사하는데 걸리는 시간은 1분 이상 1,000,000,000분 이하입니다.</li>
<li data-pf_style_display="list-item" data-pf_style_visibility="visible">심사관은 1명 이상 100,000명 이하입니다.</li>
</ul>

<h5 data-pf_style_display="block" data-pf_style_visibility="visible">입출력 예</h5>
<table class="table" data-pf_style_display="block" data-pf_style_visibility="visible">
        <thead data-pf_style_display="table-header-group" data-pf_style_visibility="visible"><tr data-pf_style_display="table-row" data-pf_style_visibility="visible">
<th data-pf_style_display="table-cell" data-pf_style_visibility="visible">n</th>
<th data-pf_style_display="table-cell" data-pf_style_visibility="visible">times</th>
<th data-pf_style_display="table-cell" data-pf_style_visibility="visible">return</th>
</tr>
</thead>
        <tbody data-pf_style_display="table-row-group" data-pf_style_visibility="visible"><tr data-pf_style_display="table-row" data-pf_style_visibility="visible">
<td data-pf_style_display="table-cell" data-pf_style_visibility="visible">6</td>
<td data-pf_style_display="table-cell" data-pf_style_visibility="visible">[7, 10]</td>
<td data-pf_style_display="table-cell" data-pf_style_visibility="visible">28</td>
</tr>
</tbody>
      </table>
<h5 data-pf_style_display="block" data-pf_style_visibility="visible">입출력 예 설명</h5>

<p data-pf_style_display="block" data-pf_style_visibility="visible">가장 첫 두 사람은 바로 심사를 받으러 갑니다. </p>

<p data-pf_style_display="block" data-pf_style_visibility="visible">7분이 되었을 때, 첫 번째 심사대가 비고 3번째 사람이 심사를 받습니다. </p>

<p data-pf_style_display="block" data-pf_style_visibility="visible">10분이 되었을 때, 두 번째 심사대가 비고 4번째 사람이 심사를 받습니다.</p>

<p data-pf_style_display="block" data-pf_style_visibility="visible">14분이 되었을 때, 첫 번째 심사대가 비고 5번째 사람이 심사를 받습니다.</p>

<p data-pf_style_display="block" data-pf_style_visibility="visible">20분이 되었을 때, 두 번째 심사대가 비지만 6번째 사람이 그곳에서 심사를 받지 않고 1분을 더 기다린 후에 첫 번째 심사대에서 심사를 받으면 28분에 모든 사람의 심사가 끝납니다.</p>

<h5 data-pf_style_display="block" data-pf_style_visibility="visible">문제가 잘 안풀린다면😢</h5>

<p data-pf_style_display="block" data-pf_style_visibility="visible">힌트가 필요한가요? [코딩테스트 연습 힌트 모음집]으로 오세요! → <a href="https://school.programmers.co.kr/learn/courses/14743?itm_content=lesson43238" target="_blank" rel="noopener" data-pf_style_display="inline" data-pf_style_visibility="visible">클릭</a></p>

<p data-pf_style_display="block" data-pf_style_visibility="visible">※ 공지 - 2019년 9월 4일 문제에 새로운 테스트 케이스를 추가하였습니다. 도움을 주신 weaver9651 님께 감사드립니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges