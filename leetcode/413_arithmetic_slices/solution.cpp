class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& A) {
        int numberOfSlicesFromLastNumber = 0;
        int totalNumberOfSlices = 0;
        for( int i = 2; i < A.size(); ++i )
        {
            if( A[i]-A[i-1] == A[i-1]-A[i-2] )
            {
                // Here starts an arithmetic sequence or continues an arithmetic sequence
                totalNumberOfSlices += numberOfSlicesFromLastNumber + 1;
                numberOfSlicesFromLastNumber = numberOfSlicesFromLastNumber + 1;
                // * When adding one more number to the sequence e.g. 3,5,7,9 -> 3,5,7,9,11
                // * every slice from previous sequence due to the previous last number will generate a new slice by appending the new last number
                // * and one more slice with size of 3 will be newly generated
                // * therefore, adding one number increase the slices number by previousSlices# + 1
            }
            else
            {
                // Here breaks any previous sequence
                numberOfSlicesFromLastNumber = 0;
            }
        }
        return totalNumberOfSlices;
    }
};
