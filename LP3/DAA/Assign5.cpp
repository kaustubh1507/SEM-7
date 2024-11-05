#include<bits/stdc++.h>
using namespace std;
bool isSafe(vector<vector<bool>> &board, int row, int col){
    for(int i=0; i<row; i++){
        if(board[i][col])
            return false;
    }
    for(int i=row-1, j=col-1; i>=0 && j>=0; i--, j--){
        if(board[i][j])
            return false;
    }
    for(int i=row-1, j = col+1; i>=0 && j<board.size(); i--, j++){
        if(board[i][j])
            return false;
    }
    return true;
}
bool solveNQueens(vector<vector<bool>> &board, int row){
    if(row ==board.size())
        return true;
    for(int col=0; col<board.size(); col++){
        if(isSafe(board, row, col)){
            board[row][col]=1;
            if(solveNQueens(board, row+1))
                return true;
            board[row][col]=0;
        }
    }
    return false;

}
void printBoard(vector<vector<bool>> &board){
    for(int i=0; i<board.size(); i++){
        cout<<endl;
        for(int j =0; j<board[0].size(); j++){
            cout<<board[i][j];
        }
    }
}
int main(){
    int N = 8;
    vector<vector<bool>> board(N, vector<bool>(N, 0));
    board[0][0]=1;
    if(solveNQueens(board, 1))
        printBoard(board);
    else   
        cout<<"No solution"<<endl;
    return 0;
}