#include<iostream>
using namespace std;

#define MAX_SIZE 10

class MyQueue {
private:
	int front;
	int rear;
	int queue[MAX_SIZE];
public:
	MyQueue() {
		front = -1;
		rear = -1;
	}

	bool isEmpty() {
		if (front == -1 && rear == -1) return true;
		else return false;
	}

	int enQueue(int x) {

		if (isEmpty()) {//checking for empty queue
			front = rear = 0;
		}
		else if ((rear + 1) % MAX_SIZE == front) {//checking if the queue is full
			cout << "Error: Queue is Full" << endl;
			return 0;
		}
		else {
			rear = (rear + 1) % MAX_SIZE;
		}
		//placing the value at rear.
		queue[rear] = x;
	}

	int frontOfQueue() {
		if (isEmpty()) return 0;

		return queue[front];
	}

	int rearOfQueue() {
		if (isEmpty()) return 0;
		
		return queue[rear];
	}
	int deQueue() {
		if (isEmpty()) {
			cout << "Queue is Empty. Nothing to DeQueue" << endl;
			return 0;
		}
		else if (front == rear) {
			int data = queue[front];
			front = rear = -1;
			return data;
		}
		int data = queue[front];
		front = (front + 1) % MAX_SIZE;
		return data;
	}

	void show() {
		if (!isEmpty()) {
			cout << "QUEUE is: ";
			for (int i = front; i <= rear; i++) {
				cout << queue[i] << "   ";
			}
			cout << endl;
		}
		else {
			cout << "Queue is Empty.!" << endl;
		}
	}
};

int main() {

	MyQueue q;
	q.isEmpty();
	q.show();
	q.enQueue(4);
	q.show();
	cout << "front of queue is : " << q.frontOfQueue() << endl;
	cout << "rear of queue is : " << q.rearOfQueue() << endl;
	q.enQueue(5);
	q.show();
	cout << "front of queue is : " << q.frontOfQueue() << endl;
	cout << "rear of queue is : " << q.rearOfQueue() << endl;
	q.enQueue(10);
	q.show();
	cout << "front of queue is : " << q.frontOfQueue() << endl;
	cout << "rear of queue is : " << q.rearOfQueue() << endl;
	q.enQueue(9);
	q.show();
	cout << "front of queue is : " << q.frontOfQueue() << endl;
	cout << "rear of queue is : " << q.rearOfQueue() << endl;
	
	q.enQueue(4);
	q.enQueue(9);
	q.enQueue(22);
	q.enQueue(5);
	q.enQueue(0);
	q.enQueue(99);
	q.show();
	q.enQueue(100);
	q.show();
	cout << q.deQueue() << " DeQueue" << endl;
	q.show();
	cout << q.deQueue() << " DeQueue" << endl;
	q.show();
	cout << q.deQueue() << " DeQueue" << endl;
	q.show();
	cout << q.deQueue() << " DeQueue" << endl;
	q.show();
	return 0;
}