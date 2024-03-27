#include <iostream>
using namespace std;

class Queue{
#define N 5
    int queue[N];
    int front = -1;
    int rear = -1;

public: void enqueue(int x){
        if(rear==(N-1)){  //if queue is full
            cout << "Queue is full." << endl;
        }else if(rear==-1 && front ==-1){  //if queue has no data
            front = 0;
            rear = 0;
            queue[rear] = x;
        }else{
            rear++;
            queue[rear] = x;
        }
    }

public: void dequeue(){
    if(rear==-1 && front==-1){
        cout << "Queue is empty." << endl;
    }else if(front==rear){
        front = -1;
        rear = -1;
    }else {
        cout << queue[front] << " is deleted from the Queue." << endl;
        front++;
    }
}
public: int top(){
    if(rear==-1 && front ==-1){
        cout << "The Queue is empty!";
        return 0;
    }else{
        return queue[front];
    }
}

public: bool isEmpty(){
    if(rear==-1 && front==-1){
        cout << "The queue is empty." << endl;
        return true;
    }else{
        cout << "The queue is not empty." << endl;
        return false;
    }

}

public: int size(){
    if(rear==-1 && front==-1){
        return 0;
    }else if(rear==front){
        return 1;
    }else{
        return (rear-front+1);
    }
}

};

int main() {

    Queue queue = *new Queue();

    cout << boolalpha << queue.isEmpty() << endl;

    queue.enqueue(99);
    cout << boolalpha << queue.isEmpty() << endl;

    queue.enqueue(6);
    queue.enqueue(9);

    cout<< "The Top element in the Queue : " << queue.top() << endl;
    queue.enqueue(68);
    cout << "Number of the elements in the Queue : " << queue.size() <<endl;
    queue.dequeue();
    cout << "Number of the elements in the Queue : " << queue.size() <<endl;
    
    return 0;
}
