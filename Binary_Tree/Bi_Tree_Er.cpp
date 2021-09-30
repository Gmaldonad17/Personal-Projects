#include<iostream>
#include<vector>
#define A 65
using namespace std;

struct node{
	char data;
	node* left_node = NULL;
	node* right_node = NULL;
};

class Tree{
	private:

		node* root = NULL;
		vector<bool> node_list{vector<bool>(26, false)};

		node* newNode (char data){
			if (this->node_list[int(data - A)] == false){
				this->node_list[int(data - A)] = true;
			}
			else {throw "E5";}

			node* node = new struct node;
			node->data = data;
			
			return node;
		}

	public:
		
		node* returnRoot(){return this->root;}

		node* find(char data, node* this_node){
			if (this_node != NULL){
				if (this_node->data == data){
					return this_node;
				} else {
					node* x = find(data, this_node->left_node);

					if (x == NULL){
						x = find(data, this_node->right_node);
					}
					return x;
				}
				
			} 
			else {throw "E4";}
		}

		void buildTree(vector<string> input){
			this->root = newNode(input[0][1]);

			for (int i = 0 ; i < int(input.size()) ; i++){
				node* this_node = find(input[i][1], this->root);
				//Null check required for this to work E2

				if (this_node->left_node == NULL){
					this_node->left_node = newNode(input[i][3]);
				} else {
					if (this_node->right_node == NULL){
						this_node->right_node = newNode(input[i][3]);
					} else {
						if (this_node->left_node->data == input[i][3] || this_node->right_node->data == input[i][3]){
							throw "E2";
						}
						else{throw "E3";}
					}
				}
			}
		}

		string printTree(node* this_node){
			string treePrint = "(";
			treePrint += this_node->data;

			if (this_node->left_node != NULL){
				treePrint += printTree(this_node->left_node);
			}

			if (this_node->right_node != NULL){
				treePrint += printTree(this_node->right_node);
			}
			treePrint += ")";

			return treePrint;
		}
};

int main(){
	vector<string> input {"(A,B)", "(A,B)", "(B,D)", "(B,F)", "(D,E)"};
	Tree myTree;

	try{
		myTree.buildTree(input);
		string treePrint = myTree.printTree(myTree.returnRoot());
		cout << treePrint << endl;
	} 
	catch(char const* e){cout << e << endl;}
	return 0;
}
