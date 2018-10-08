struct Intvl
{
  int left; // idx of the leftmost empty seat in this Intvl
  int right;// idx of the rightmost empty seat in this Intvl
  static int N;
  Intvl(int l, int r)
  : left(l)
  , right(r)
  {}

  int getBestClosestDistance()
  {
    if( left == 0 )
    {  return right;  }
    if( right == N - 1 )
    {  return N - 1 - left;  }
    if( left == right )
    {  return 0;  }
    if( left > right )
    {  return -1;  }
    return (right - left) / 2;
  }

  int getBestSeatIdx()
  {
    if( left > right )
    {  return -1;  }
    return left + getBestClosestDistance();
  }

  bool operator< (Intvl& other)
  {
    if( this->getBestClosestDistance() != other.getBestClosestDistance() )
    {  return this->getBestClosestDistance() < other.getBestClosestDistance()  }
    return this->getBestSeatIdx() < other.getBestSeatIdx()
  }
};

class ExamRoom {
public:
    std::set<Intvl> intervals; // ordered intervals
    std::map<int, int> l2r, r2l;
    typedef std::set<Intvl>::iterator IntvlIt;

    ExamRoom(int N) {
      Intvl::N = N;
      Intvl interval = Intvl(0, N - 1);
      intervals.insert(interval);
      l2r[0] = N - 1;
      r2l[N - 1] = 0;
    }

    int seat() {
      IntvlIt it = intervals.begin();
      // something is wrong, no intervals available
      if( it == intervals.end() )
      {  return -1;  }
      Intvl interval = *it;
      intervals.erase(it);
      int position = interval.getBestSeatIdx();
      intervals.insert( Intvl(interval.left, position-1) );
      l2r[interval.left] = position - 1;
      r2l[position-1] = interval.left
      intervals.insert( Intvl(position+1, interval.right));
      l2r[position+1] = interval.right;
      r2l[interval.right] = position+1
      return position;
    }struct Intvl
{
  int left; // idx of the leftmost empty seat in this Intvl
  int right;// idx of the rightmost empty seat in this Intvl
  static int N;
  Intvl(int l, int r)
  : left(l)
  , right(r)
  {}

  int getBestClosestDistance() const
  {
    if( left == 0 )
    {  return right;  }
    if( right == N - 1 )
    {  return N - 1 - left;  }
    if( left > right )
    {  return -1;  }
    return (right - left) / 2;
  }

  int getBestSeatIdx() const
  {
    if( left == 0 )
    {  return 0;  }
    if( right == N - 1 )
    {  return N - 1;  }
    if( left > right )
    {  return -1;  }
    return left + getBestClosestDistance();
  }

  bool operator< (const Intvl& other) const
  {
    if( this->getBestClosestDistance() != other.getBestClosestDistance() )
    {  return this->getBestClosestDistance() > other.getBestClosestDistance();  }
    return this->getBestSeatIdx() < other.getBestSeatIdx();
  }
};

int Intvl::N = 0;

class ExamRoom {
public:
    std::set<Intvl> intervals; // ordered intervals
    std::map<int, int> l2r, r2l;
    typedef std::set<Intvl>::iterator IntvlIt;

    ExamRoom(int N) {
      Intvl::N = N;
      Intvl interval = Intvl(0, N - 1);
      intervals.insert(interval);
      l2r[0] = N - 1;
      r2l[N - 1] = 0;
    }

    int seat() {
      IntvlIt it = intervals.begin();
      // something is wrong, no intervals available
      if( it == intervals.end() )
      {  return -1;  }
      Intvl interval = *it;
      intervals.erase(it);
      int position = interval.getBestSeatIdx();
      intervals.insert( Intvl(interval.left, position-1) );
      l2r[interval.left] = position - 1;
      r2l[position-1] = interval.left;
      intervals.insert( Intvl(position+1, interval.right));
      l2r[position+1] = interval.right;
      r2l[interval.right] = position+1;
      return position;
    }

    void leave(int p) {
      int left = r2l[p-1];
      int right = l2r[p+1];
      intervals.erase( Intvl(left, p-1) );
      intervals.erase( Intvl(p+1, right) );
      intervals.insert( Intvl(left, right) );
      r2l.erase(p-1);
      l2r.erase(p+1);
      l2r[left] = right;
      r2l[right] = left;
    }
};

/**
 * Your ExamRoom object will be instantiated and called as such:
 * ExamRoom obj = new ExamRoom(N);
 * int param_1 = obj.seat();
 * obj.leave(p);
 */


    void leave(int p) {
      int left = r2l[p-1];
      int right = l2r[p+1];
      intervals.erase( Intvl(left, p-1) );
      intervals.erase( Intvl(right, p+1) );
      intervals.insert( Intvl(left, right) );
      r2l.erase(p-1);
      l2r.erase(p+1);
      l2r[left] = right;
      r2l[right] = left;
    }
};

/**
 * Your ExamRoom object will be instantiated and called as such:
 * ExamRoom obj = new ExamRoom(N);
 * int param_1 = obj.seat();
 * obj.leave(p);
 */

/*
按网上大神的思路写的, cpp很不熟练,要多练练
https://leetcode.com/problems/exam-room/discuss/141583/C++-O(logn)-seat()-and-O(logn)-leave()-with-STL-set-and-map
Store empty intervals
Seat: pick the largest interval from treeset
Leave: erase the 2 small interval, and insert the merged one
*/
