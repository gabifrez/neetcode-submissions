class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> hashmap;
        for(int i=0; i<nums.size(); ++i){
            if(hashmap.count(nums[i]))
                return true;
            hashmap.insert(nums[i]);
        }
        return false;
    }
};