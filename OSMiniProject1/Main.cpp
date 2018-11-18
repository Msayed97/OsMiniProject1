#include <iostream>
using namespace std;
#include "ProcessGenerator.h"
void main() 
{
	ProcessGenerator p ("IntputData.txt");
	p.ReadInput();
	p.GenerateOuput("output.txt");
	cout << "done";
	int x = 0;
	cin >> x;


}