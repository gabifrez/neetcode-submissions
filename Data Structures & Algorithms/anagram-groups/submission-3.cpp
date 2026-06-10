#include <array>
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> answer;
        vector<vector<string>> raspuns;
        for (auto& cuvant : strs) {
            array<int, 26> alfabet = {0};
            string token;
            for (auto& caracter : cuvant) {
                alfabet[caracter - 'a'] += 1;
            }
            for (int i = 0; i < 26; i++) {
                    token += ("#" + to_string(alfabet[i]));
            }
            answer[token].push_back(cuvant);
        }
        for (auto& [key, value] : answer) {
            raspuns.push_back(move(value));
        }
        return raspuns;
    }
};
