#include <iostream>
#include <string>
using namespace std;

struct Mydata{
    int id;
    string name;
};

int main(){
    Mydata data1 = {1, "Sourabh"};

    cout << "ID: " << data1.id << endl;
    cout << "Name:" << data1.name << endl;

    return 0;
}
