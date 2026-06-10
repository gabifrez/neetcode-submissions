//folosim hash map
    //iteram o data array.ul
    //pentru fiecare element, la cheia respectiva a elementului incrementam
    //la elementul la care ajungem verificam care este cel mai mic element salvat
    //cu numar minim de aparitii si il inlocuim.
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> hashmap;
        unordered_map<int,vector<int>> frecventa;
        vector<int> raspuns;
        int nMax = nums[0], aMax=0;
        for(auto& num: nums){
            hashmap[num] ++;
            if (num> nMax)
                nMax = num;
            if (hashmap[num] > aMax)
                aMax = hashmap[num];
        }
        for(auto& [numar, aparitii]: hashmap){
            frecventa[aparitii].push_back(numar);
        }

        while(k){
            for (auto& num: frecventa[aMax]) {
                raspuns.push_back(num);
            }
            k -= frecventa[aMax].size();
            --aMax;
        }
        for (auto& num: raspuns) {
            cout << num << " ";
        }
        return raspuns;
    }
};
