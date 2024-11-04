#include<bits/stdc++.h>
using namespace std;

class Node {
public:
    int val; 
    string symbol;
    string huffman;
    Node* left;
    Node* right;

    Node(int v, string s) : val(v), symbol(s), huffman(""), left(nullptr), right(nullptr) {}

    bool operator<(const Node& other) const {
        return val > other.val;  // Max-Heap behavior for priority queue
    }
};

void printNodes(Node* node, string val = "") {
    string newVal = val + node->huffman;
    if (node->left)
        printNodes(node->left, newVal);
    if (node->right)
        printNodes(node->right, newVal);
    if (!node->left && !node->right) {
        cout << node->symbol << " -> " << newVal << endl;
    }
}

int main() {
    vector<string> chars = {"a", "b", "c", "d", "e"};
    vector<int> freq = {100, 12, 24, 105, 38};

    // Priority queue of Node pointers
    priority_queue<Node*, vector<Node*>, function<bool(Node*, Node*)>> pq([](Node* a, Node* b) {
        return a->val > b->val;
    });

    for (int i = 0; i < 5; i++) {
        pq.push(new Node(freq[i], chars[i]));
    }

    while (pq.size() > 1) {
        Node* left = pq.top();
        pq.pop();
        Node* right = pq.top();
        pq.pop();

        left->huffman = "0";
        right->huffman = "1";

        Node* newNode = new Node(left->val + right->val, left->symbol + right->symbol);
        newNode->left = left;
        newNode->right = right;

        pq.push(newNode);
    }

    Node* root = pq.top();
    printNodes(root);

    // Memory cleanup (delete all nodes)
    delete root;

    return 0;
}
