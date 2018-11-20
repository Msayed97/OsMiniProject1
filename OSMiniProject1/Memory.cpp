#include "Memory.h"



Memory::Memory()
{
}

void Memory::addToMemory(string s)
{
	ifstream data;
	data.open(s, ios::in);
	if (data.is_open())
	{
		data >> numOfProcesses;
		for (int i = 0; i < numOfProcesses; i++)
		{
			float arrivalTime;
			float	brustTime;
			int priority;
			data >> arrivalTime >> arrivalTime >> brustTime >> priority;
			processes.push_back(Process(arrivalTime, brustTime, priority));
		}
	}

}

void Memory::sort()
{
	
	for (int i = 1; i < processes.size(); i++)
	{
		float key = processes[i].getArrivalTime();
		Process k = processes[i];
		int j = i - 1;
		while (j >= 0 && ((processes[j].getArrivalTime() > key)||(processes[j].getArrivalTime() == key && k.getPriority()> processes[j].getPriority()))) {
			processes[j + 1] = processes[j];
			j--;
		}
		processes[j + 1] = k;
	}
	// To be deleted 
	cout <<endl<< "processes sorted" << endl;
	for (int i = 0; i < processes.size(); i++)
	{
		cout << processes[i].getArrivalTime()<<"\t" << processes[i].getPriority()<< endl;
	}
}


Memory::~Memory()
{
}
