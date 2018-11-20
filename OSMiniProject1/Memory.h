#pragma once
#include "Process.h"
#include<string>
#include<fstream>
#include<vector>
#include<iostream>
using namespace std;
class Memory
{
	int numOfProcesses;
	vector<Process> processes;
public:
	Memory();
	void addToMemory(string);
	void sort();
	~Memory();
};

