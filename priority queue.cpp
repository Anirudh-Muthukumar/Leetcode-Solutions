#include<iostream>
#include<queue>
using namespace std;

int main()
{
    priority_queue<int, vector<int>, greater<int> > pq;
    pq.push(10);
    pq.push(23);
    pq.push(10);
    pq.push(4);
    pq.push(5);
    pq.push(5);
    while(!pq.empty())
    {
        cout<<pq.top()<<endl;
        pq.pop();
    }
    return 0;
}