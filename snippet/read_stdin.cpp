#include <iostream>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

/*
stdin:
5
1 2 3 4 5

output:
hello world
Expected size is 5
Read-in size is 5
1
2
3
4
5
*/

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    std::cout << "hello world\n";
    std::string line;
    std::vector<int> nums;
    size_t asize = 0;
    for(int i = 0; std::getline(std::cin, line); ++i)
    {
        std::stringstream ss(line);
        if ( i == 0 )
        {
            ss >> asize;
        }
        else if( i == 1)
        {
            int intread = 0;
            while( ss >> intread )
            {
                nums.push_back(intread);
            }
        }
    }
    std::cout << "Expected size is " << asize << "\n";
    std::cout << "Read-in size is " << nums.size() << "\n";
    for( int i = 0; i < nums.size(); ++i )
    {
        std::cout << nums[i] << "\n";
    }
    return 0;
}