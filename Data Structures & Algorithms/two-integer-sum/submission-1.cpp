class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> valori;
        for(int i=0; i < nums.size(); ++i){
            if(valori.count(target - nums[i]))
                return {valori[target - nums[i]], i};
            valori[nums[i]] = i;
            
        }
    }
};
