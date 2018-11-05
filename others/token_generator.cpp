/*
v1
一个void generator (int ms, int bufferSize), 每隔 m (ms) 会generate 一个token 到queue 里面。 另外一个int getter(int desiredAmount) 去queue 里面fetch 它最大可以拿的数目，就是如果queue 里面的size大于它想要的，那么就返回那个desiredAmount,不然就直接返回当前queue 所有的数目。
. Waral 博客有更多文章,
我用了个不熟的synchronousQueue来做，其实应该直接用锁就好了，对queue的size 来增加减少，那时候也没想出来。。。

v2
写一个token generator， api 就一个function gettoken(n), n 是想要的token数量，return 实际拿到手的token， 
parameter是frequency， eg freq=2 表示每两秒产生一个token。
不需要threading，解题思路： 记录每次call的timestamp算中间产生了多少个 + 原来剩下的

*/
#include <ctime>
#include <unistd.h>
#include <iostream>
#include <assert.h>

// no threading version
class TokenGenerator
{
public:
    TokenGenerator( size_t secIntvl )
    : secIntvl_( secIntvl )
    , remainToken_( 0 )
    , lastCall_( std::time(0) )
    { }
    ~TokenGenerator()
    { }

    size_t getToken( size_t n );

private:
    size_t      secIntvl_;
    size_t      remainToken_;
    std::time_t lastCall_;
};

size_t TokenGenerator::getToken( size_t n )
{
    std::time_t nowCall = std::time(0);
    //std::cout << "The last call time for fetching token is " << lastCall_ << "\n"
    //          << "The curr call time for fetching token is " << nowCall << "\n";
    
    double diff = difftime( nowCall, lastCall_ );
    size_t tokensBetween = size_t( diff / secIntvl_ );
    remainToken_ += tokensBetween;
    
    lastCall_ = nowCall;
    if ( remainToken_ > n )
    {
        remainToken_ -= n;
        return n;
    }
    else
    {
        size_t fetched = remainToken_;
        remainToken_ = 0;
        return fetched;
    }
}


int main( int argc, char ** argv )
{
    TokenGenerator tkg(2);
    std::cout << "Construct token generater with second interval 2 \n";

    // expect fetch 0
    sleep(0);
    std::cout << "sleep for 0 seconds\n";
    std::cout << "Try fetch 10, actual fetch " << tkg.getToken(10) << "\n";

    // expect fetch 1
    sleep(2);
    std::cout << "sleep for 2 seconds\n";
    std::cout << "Try fetch 10, actual fetch " << tkg.getToken(10) << "\n";

    // expect fetch 0
    sleep(4);
    std::cout << "sleep for 4 seconds\n";
    std::cout << "Try fetch 0, actual fetch " << tkg.getToken(0) << "\n";

    // expect fetch 2
    sleep(1);
    std::cout << "sleep for 1 seconds\n";
    std::cout << "Try fetch 10, actual fetch " << tkg.getToken(10) << "\n";

    // assert test
    TokenGenerator tkg2(1);
    sleep(3);
    assert(tkg2.getToken(2) == 2);
    assert(tkg2.getToken(3) == 1);

    sleep(10);
    assert(tkg2.getToken(1000) == 10);

    sleep(4);
    assert(tkg2.getToken(1) == 1);

    sleep(5);
    assert(tkg2.getToken(2) == 2);
    assert(tkg2.getToken(1000) == 6);

    return 0;
}