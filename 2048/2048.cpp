#include<iostream>
using namespace std;

int main(int argc, char const *argv[])
{
   int board[4][4];
   for (int i = 0; i < 4; i++)
   {
      for (int k = 0; k < 4; k++)
      {
         cin >> board[i][k];
      }
   }

   int direction;
   cin >> direction; 
   
   int new_board[4][4] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
   switch (direction)
   {
      case 0: //left
         for (int i = 0; i < 4; i++){
            int curr, next, last; 

            curr = board[i][0];
            next = board[i][1];
            if (curr != 0 && curr == next){
               new_board[i][0] = 2*curr;
               board[i][1] = 0;
            }
            else{
               new_board[i][0] = curr;
            }

            for (int k = 1; k < 3; k++){
               curr = board[i][k];
               next = board[i][k+1];
               last = board[i][k-1];
               if (curr != 0 && curr == next){
                  curr *= 2;
                  board[i][k+1] = 0;
               }
               if (last == 0){
                  new_board[i][k-1] = curr;
               }
               else{
                  new_board[i][k] = curr;
               }
                  
            }
            curr = board[i][3];
            last = board[i][2];
            if (last == 0){
                  new_board[i][2] = curr;
            }
            else{
                  new_board[i][3] = curr;
            }
         }
         break;
   
   }

   for (int i = 0; i < 4; i++)
   {
      for (int k = 0; k < 4; k++)
      {
         cout << new_board[i][k] << " ";
      }
      cout << "\n";
   }
   
}

