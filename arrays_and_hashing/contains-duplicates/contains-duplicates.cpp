#include <stdio.h>
#include <stdlib.h>
#include <iostream>
// #include<bits/stdc++.h>
#include <vector>
#include <unordered_map>

using namespace std;

/**
 *
 * Given an integer array nums,
 * return true if any value appears more than once in the array, otherwise return false.
 *
 *
 * Input: nums = [1, 2, 3, 3]
    Output: true
 *

    * Input: nums = [1, 2, 3, 4]
        Output: false
 *
 */

class Solution
{
public:
    bool containsDuplicate(vector<int> &nums)
    {
        unordered_map<int, int> hm;
        for (int i = 0; i < nums.size(); i++)
        {
            // if value appears in hash map then it already exists more than once return true
            if (hm.find(nums[i]) != hm.end())
            {
                return true;
            }
            else
            // val doesnt exists insert in hash map
            {
                hm.insert({nums[i], i});
            }
        }
        // no value found more than once return false
        return false;
    }

    int main()
    {
        Solution s;
        vector<int> nums = {1, 2, 3, 3};
        cout << s.containsDuplicate(nums) << endl; // Output: true

        vector<int> nums2 = {1, 2, 3, 4};
        cout << s.containsDuplicate(nums2) << endl; // Output: false

        return 0;
    }
};