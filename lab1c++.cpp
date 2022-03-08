#include <iostream>
#include <ctime>
#include <cmath>
using namespace std;

const int CRYSTAL_HEIGHT = 100, CRYSTAL_WIDTH = 100, TOTAL_DISLOCATIONS = 5000;
void PrintCrystal(int crystal[CRYSTAL_HEIGHT][CRYSTAL_WIDTH]){
    for (int i = 0; i < CRYSTAL_HEIGHT; i++){
        for (int j = 0; j < CRYSTAL_WIDTH; j++){
            cout << crystal[i][j] << " ";
        }
    cout << endl;
    }
}

bool IsBorderCell(int i, int j){
    return((i == 0) || (j == 0) || (i == CRYSTAL_HEIGHT - 1) || (j == CRYSTAL_WIDTH - 1));
}

bool CheckAdjacentCells(int crystal[CRYSTAL_HEIGHT][CRYSTAL_WIDTH], int i, int j, int value){
    return ((crystal[i][j - 1] == value) || (crystal[i - 1][j] == value) || (crystal[i][j + 1] == value) || (crystal[i + 1][j] == value)||
            (crystal[i][j - 1] == -1) || (crystal[i - 1][j] == -1) || (crystal[i][j + 1] == -1) || (crystal[i + 1][j] == -1));
}

void generate(int crystal[CRYSTAL_HEIGHT][CRYSTAL_WIDTH])
{
for (int i = 0; i < TOTAL_DISLOCATIONS; i++){
int a=rand()%CRYSTAL_WIDTH;
int b=rand()%CRYSTAL_HEIGHT;
if (crystal[a][b] == 1){i -= 1;}
crystal[a][b] = 1;
}
}

int main(){
    srand(time(NULL));
    int crystal[CRYSTAL_HEIGHT][CRYSTAL_WIDTH] = {0};
    generate(crystal);
    int finished = 200;
    int lenresults = finished;
    int results[finished] = {0};
    int iteration = 1;
    int s = 0;
    while(finished != 0){
        //PrintCrystal(crystal);
        //cout << "//////////////////////////////////////////////" << endl;
        int count_active_dislocs = 0;
        for (int i = 0; i < CRYSTAL_HEIGHT; i++){
            for (int j = 0; j < CRYSTAL_WIDTH; j++){
                if(crystal[i][j] == iteration){
                    count_active_dislocs++;
                    int direction = rand()%4+1;
                    int cell_to_move_i = i + (direction - 2) % 2;
                    int cell_to_move_j = j + (direction - 3) % 2;
                    if(IsBorderCell(i, j) == true){
                        crystal[i][j] = -1;
                    }
                    else if(CheckAdjacentCells(crystal, i, j, iteration)){
                        crystal[i][j] = -1;
                    }
                    else if(crystal[cell_to_move_i][cell_to_move_j] != 0){
                        crystal[i][j] = -1;
                    }
                    else{
                        crystal[cell_to_move_i][cell_to_move_j] = iteration + 1;
                        crystal[i][j] = 0;
                    }
                }
            }
        }
        if(count_active_dislocs == 0){
            finished -= 1;
            results[finished] = iteration-1;
            iteration = 0;
            for (int i = 0; i < CRYSTAL_HEIGHT; i++){
                for (int j = 0; j < CRYSTAL_WIDTH; j++){crystal[i][j]=0;}}
            generate(crystal);
        }
        iteration++;
    }
    for (int i = 0; i < lenresults; i++){s += results[i];}
    float b;
    b = s;
    cout<<b/lenresults;
    return 0;
}
