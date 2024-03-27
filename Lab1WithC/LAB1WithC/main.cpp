#include <iostream>
using namespace std;
int main() {

    //QUESTION 1:
    string name;
    string studentID;
    cout << "What is your name?" << endl;
    cin >> name;
    cout << "Hello " << name << endl;
    cout << "What is your Student ID?" << endl;
    cin >> studentID;
    cout << "Your ID is " << studentID << endl;

    //QUESTION 2:
    double var1;
    double var2;
    cout << "Enter a value for var1 :" << endl;
    cin >> var1;
    cout << "Enter a value for var2 :" << endl;
    cin >> var2;

    double sum = var1 + var2;
    double diff = var1-var2;
    double prod = var1*var2;
    cout << "The value entered for var1 = " << var1 << ", The value entered for var2 = " << var2 << endl;
    cout << "Sum= " << sum << endl;
    cout << "Diff= " << diff << endl;
    cout << "Prod= " << prod << endl;

    //QUESTION 3:
    string nameForStudent;
    double labGrade;
    double midtermGrade;
    double finalGrade;
    double lastScore;
    cout<< "What is your name: " << endl;
    cin >> nameForStudent;
    cout<< "What is your Lab Grade:" << endl;
    cin >> labGrade;
    cout<< "What is your Midterm Grade:" << endl;
    cin >> midtermGrade;
    cout << "What is your Final Grade:" << endl;
    cin >> finalGrade;
    cout<< "Name:" << nameForStudent << endl;
    cout<< "Lab:" << labGrade << endl;
    cout<< "Midterm:" <<midtermGrade << endl;
    cout << "Final:" << finalGrade << endl;
    lastScore = (labGrade/4)+((midtermGrade*35)/100)+((finalGrade*40)/100);
    cout << "Last Score=" << lastScore << endl;


    //QUESTION 4:
    cout<< "* \n**\n***\n**\n*"<< endl;



    return 0;
}
