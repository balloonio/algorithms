class Solution {
public:
    string minWindow(string s, string t) {
        if(s.size() == 0 || t.size() == 0) return s;
        if(t.size() == 1 && s[0] == t[0]) return t;
        
        unordered_map<char,int> counts;
        for(int i = 0; i < t.size(); i++){
            counts[t[i]]++;
        }
        int head = 0;
        int tail = 0; 
        string res = "";
        update(counts, s[head], -1);
        while(tail < s.size()){
            //cout << head << "," << tail << endl;
            while(tail < s.size() - 1 && !complete(counts)){
                tail++;
                update(counts, s[tail], -1);
            }
            
            //have a complete window; move head until it's not
            if(complete(counts)){
                while(head < tail){
                    if(counts.find(s[head]) != counts.end() && counts[s[head]] == 0) break;
                    update(counts, s[head], 1);
                    head++;
                }
                if(res.size() == 0 || tail - head + 1 < res.size()){
                    res = s.substr(head,tail - head + 1);
                }
            }
            
            //move tail at least one every iteration
            tail++;
            if(tail < s.size()) update(counts, s[tail], -1);
        }
        
        return res;
    }
    
private:
    void update(unordered_map<char,int>& counts, char c, int sign){
        if(counts.find(c) != counts.end()) counts[c] += sign;
    }
    
    bool complete(unordered_map<char,int>& char_counts){
        for(const auto& myPair:char_counts){
            if(myPair.second > 0) return false;
        }
        return true;
    }
};
