#include "Scheduler.h"



void Scheduler::HPF()
{
	while (!done)
	{
		refreshProcesses();
		// algo
		if (activeProcesses.size() == 1)
		{

		}
		// algo end
		time++;
	}
}

void Scheduler::FCFS()
{
	int start = 0;
	while (numOfProcesses)
	{
		refreshProcesses();
		// algo
	
		for (int i = start; i < activeProcesses.size(); i++)
		{
			float burst = activeProcesses[i].getburstTime();
			activeProcesses[i].setFinishingTime(burst + time);
			start++;
			busy(burst);
			time++; // assume context time = 1
			numOfProcesses--;
		}
		time++;
		// algo end
	}
	// To be deleted 
	cout << endl << "processes algo done" << endl;
	for (int i = 0; i < activeProcesses.size(); i++)
	{
		cout << activeProcesses[i].getArrivalTime() << "\t" <<activeProcesses[i].getburstTime()<<"\t" << activeProcesses[i].getFinishingTime() << endl;
	}
}

void Scheduler::RR()
{
}

void Scheduler::SRTN()
{
}

void Scheduler::busy(int t)
{
	for (int i = 0; i < t; i++)
	{
		time++;
		refreshProcesses();
	}
}

void Scheduler::refreshProcesses()
{
	for (int i = 0; i < processes.size(); i++)
	{
		if (processes[i].getArrivalTime() == time) {
			activeProcesses.push_back(processes[i]);
		}
		else if (processes[i].getArrivalTime() > time)
		{
			break;
		}
	}
}

Scheduler::Scheduler()
{
	done = false;
	time = 0;
}

void Scheduler::addToScheduler(string s)
{
	ifstream data;
	data.open(s, ios::in);
	if (data.is_open())
	{
		data >> numOfProcesses;
		for (int i = 0; i < numOfProcesses; i++)
		{
			float arrivalTime;
			float	burstTime;
			int priority;
			int id;
			data >> id >> arrivalTime >> burstTime >> priority;
			processes.push_back(Process(id , arrivalTime, burstTime, priority));
		}
	}

}

void Scheduler::sort()
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

void Scheduler::start(int algo)
{
	switch (algo)
	{
	case 1:
		HPF();
		break;
	case 2:
		FCFS();
		break;
	case 3:
		RR();
		break;
	case 4:
		SRTN();
		break;
	default:
		break;
	}
}


Scheduler::~Scheduler()
{
}
