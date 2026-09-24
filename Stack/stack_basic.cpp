#include <iostream>
#include <stack>
using namespace std;

int main(){
    stack<int> s;
    s.push(100);
    s.push(400);
    s.push(9000);

    cout << "Top element: " << s.top() << endl;

    s.pop();

    cout << "Top element after pop1: " << s.top() << endl;

    s.pop();

    cout << "Top element after pop2: " << s.top() << endl;

    return 0;
    
}