#include <iostream>
using namespace std;
#include "ProcessGenerator.h"
#include "Memory.h"
void main()
{
	ProcessGenerator p ("IntputData.txt");
	p.ReadInput();
	p.GenerateOuput("output.txt");
	cout << "done";
	Memory m;
	m.addToMemory("output.txt");
	m.sort();
	int x;
	cin >> x;

}