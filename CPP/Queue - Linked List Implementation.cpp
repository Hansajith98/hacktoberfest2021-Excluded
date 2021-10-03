//Queue Linked List Implementation

#include<iostream>
using namespace std;

class Node {
public:
	int data;
	Node* next;

	Node(int data, Node* next = NULL) {
		this->data = data;
		this->next = next;
	}
};

class MyQueue {
private:
	Node* front;
	Node* rear;

public:
	MyQueue() {
		front = rear = NULL;
	}
	bool isEmpty() {
		if (front == NULL) return true;
		else return false;
	}
	//this method is same as add to tail method of singly linked list.
	void enQueue(int i) {
		if (isEmpty()) {
			front = rear = new Node(i);
		}
		else {
			rear->next = new Node(i);
			rear = rear->next;
		}
	} 

	//this method is same as remove from head method of sinlgy linked list.
	int deQueue() {
		if (isEmpty()) return 0;
		else if (front == rear) {
			int data = front->data;
			front = rear = NULL;
			return data;
		}
		Node* temp = front;
		int data = temp->data;
		front = front->next;
		temp->next = NULL;
		delete temp;
		return data;
	}

	int frontOfQueue() {
		if (isEmpty()) return 0;
		return front->data;
	}

	void display() {
		if (isEmpty()) cout << "Empty List.!" << endl;
		else {
			Node* temp = front;
			cout << "Queue is: ";
			while (temp != NULL) {
				cout << temp->data << "  ";
				temp = temp->next;
			}
			cout << endl;
		}
	}
};

int main() {

	MyQueue q;
	if (q.isEmpty()) cout << "Queue is Empty!" << endl;
	
	q.enQueue(3);
	q.display();
	q.enQueue(4);
	q.display();
	q.enQueue(5);
	q.display();

	cout << "Front : " << q.frontOfQueue() << endl;

	q.enQueue(23);
	q.display();

	int dq;
	for (int i = 0; i < 4; i++) {
		dq = q.deQueue();
		if (dq == 0) {
			cout << "Empty Queue!" << endl;
		}
		else {
			cout << dq << " DeQueue" << endl;
		}
	}
	

	return 0;
}