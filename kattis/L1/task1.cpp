
/*

 If we implement a simply greedy alg. here we can do it by: 
 (let S be the set of all intervals  [a_i, b_i] and [A,B] is the set we want to cover)
 start with the set that starts at (or before) A and cover the most ground. 

 We first sort the smallest a then the second priority is the biggest b if they have the same a (or the biggest abs(a-b))

*/

#include <iostream>
#include <vector>
#include <algorithm> // for using the function template sort with complexity O(n log(n))


// We will use a vector that stores pairs of pairs(double double), int) basically a vector that stores [a_i,b_i], index)

using vec = std::vector<std::pair<std::pair<double, double>, int>>; // for simplicity
using Interval = std::pair<std::pair<double, double>, int>; 

std::vector<int> cover_interval(double A, double B, vec& intervals)
{
    sort(intervals.begin(), intervals.end(), [](const Interval& a, const Interval& b) {
        return a.start < b.start || (a.start == b.start && a.end > b.end);
    });
    
}