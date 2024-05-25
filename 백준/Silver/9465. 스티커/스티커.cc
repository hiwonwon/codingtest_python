#include <iostream>
#include <vector>
using namespace std;
using my_data = pair<int, int>;

int main(void) {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	int T;
	cin >> T;

	for (int ti = 0; ti < T; ti++) {
		int n;
		cin >> n;

		vector<my_data> STdata(n);
		vector<my_data> DP(n);

		for (int ni = 0; ni < n; ni++) {
			cin >> STdata[ni].first;
		}
		for (int ni = 0; ni < n; ni++) {
			cin >> STdata[ni].second;
		}

		DP[0].first = STdata[0].first;
		DP[0].second = STdata[0].second;

		DP[1].first = DP[0].second + STdata[1].first;
		DP[1].second = DP[0].first + STdata[1].second;

		for (int i = 2; i < n; i++) {
			DP[i].first = STdata[i].first + max(DP[i - 1].second, max(DP[i - 2].first, DP[i - 2].second));
			DP[i].second = STdata[i].second + max(DP[i - 1].first, max(DP[i - 2].first, DP[i - 2].second));
		}

		cout << max(DP[n - 1].first, DP[n - 1].second) << "\n";
	}

	return 0;
}