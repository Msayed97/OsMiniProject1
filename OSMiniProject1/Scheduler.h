#pragma once
#include "Process.h"
#include<string>
#include<fstream>
#include<vector>
#include<iostream>
using namespace std;
class Scheduler
{
	int numOfProcesses;
	bool done;
	float time;
	vector<Process> processes;
	vector<Process> activeProcesses;
	void HPF();
	void FCFS();
	void RR();
	void SRTN();
	void busy(int t);
	void refreshProcesses();
public:
	Scheduler();
	void addToScheduler(string);
	void sort();
	void start(int algo);
	~Scheduler();
};

