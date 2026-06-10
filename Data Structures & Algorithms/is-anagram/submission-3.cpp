class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> characters;
        if(s.length() != t.length())
            return false;
        for(int i=0; i<s.length(); ++i)
            characters[s[i]]++;
        for(int i=0; i<t.length(); ++i){
            if(!characters.count(t[i]))
                return false;
            characters[t[i]]--;
            if(characters[t[i]]<0)
                return false;    
        }
        return true;
    }
};
