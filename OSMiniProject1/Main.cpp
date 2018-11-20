#include <iostream>
using namespace std;
#include "ProcessGenerator.h"
#include "Scheduler.h"
int chooseAlgo();
void main()
{
	ProcessGenerator p ("IntputData.txt");
	p.ReadInput();
	p.GenerateOuput("output.txt");
	cout << "done";
	Scheduler s;
	s.addToScheduler("output.txt");
	s.sort();
	int algo = chooseAlgo();
	s.start(algo);
	int x;
	cin >> x;

}

int chooseAlgo() {
	int algo = -1;
	cout << "Choose the wanted Algorithm \n 1. HPF \n 2. FCFS \n 3. RR \n 4. SRTN\n";
	cin >> algo;
	while (algo != 1 && algo != 2 && algo != 3 && algo != 4)
	{
		cout << "Enter valid number\n";
		cin >> algo;
	}
	return algo;
}