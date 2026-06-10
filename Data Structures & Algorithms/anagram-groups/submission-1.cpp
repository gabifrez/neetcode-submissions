#include <array>
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<array<int,26>, vector<string>> answer;
        vector<vector<string>> raspuns;

        for (auto& cuvant : strs) {
            array<int, 26> alfabet = {0};
            int dimensiune_cuvant = cuvant.length();
            while (dimensiune_cuvant) {
                dimensiune_cuvant --;
                int caracter = cuvant[dimensiune_cuvant] - 'a';
                alfabet[caracter] ++;
            }
            answer[alfabet].push_back(cuvant);
        }
        for (auto& [key, value] : answer) {
            raspuns.push_back(value);
        }
        return raspuns;

    
    }
};
