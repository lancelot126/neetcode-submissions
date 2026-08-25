class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> sum;

        for (int i = 0; i < nums.size(); i++) {
            sum[nums[i]] = i;
        }

        for (int i = 0; i < nums.size(); i++) {
            int value = target - nums[i];
            if (sum.count(value) && sum[value] != i) {
                return {i, sum[value]};
            }
        }

        return {};
    }
};