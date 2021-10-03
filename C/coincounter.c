#include <stdio.h>
int calc_coins(int coin, int amount);

int main(){
	int amount;
	int coins[] = {50, 20, 5, 2, 1};
	printf("Type in your amount of money in cent : ");
	scanf("%d", &amount); 
	
	for(int i = 0; i < 5; i++){
		amount = calc_coins(coins[i], amount);
	}

	return 0;
}

int calc_coins(int coin, int amount){
	int n = amount/coin;
	printf("Amount of %2i-cent Coins: %3i\n", coin, n);
	amount = amount - n*coin;
	return amount;
}
