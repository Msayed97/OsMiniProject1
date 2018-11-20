#include "Process.h"

Process::Process( int ID , float arrival, float burst, int priority )
{
	setid(ID);
	setArrivalTime(arrival);
	setburstTime(burst);
	setPriority(priority);
}

float Process::getArrivalTime()
{
	return arrivalTime;
}

float Process::getburstTime()
{
	return burstTime;
}

int Process::getPriority()
{
	return priority;
}

float Process::getTurnaroundTime()
{
	return turnaroundTime;
}

float Process::getFinishingTime()
{
	return finishingTime;
}

float Process::getweightedTat()
{
	return turnaroundTime / burstTime;
}

float Process::getremainingTime()
{
	return remainingTime;
}

float Process::getid()
{
	return id;
}

void Process::setFinishingTime(float t)
{
	if (t > 0)
	{
		finishingTime = t;
	}
}

void Process::setTurnaroundTime(float t)
{
	if (t > 0)
	{
		turnaroundTime = t;
	}
}

void Process::setArrivalTime(float t)
{
	if (t > 0)
	{
		arrivalTime = t;
	}
}

void Process::setburstTime(float t)
{
	if (t > 0)
	{
		burstTime = t;
	}
}

void Process::setPriority(int p)
{
	if (p >= 0)
	{
		priority = p;
	}
}

void Process::setremainingTime(int r)
{
	if(r>=0)
	remainingTime = r;
}

float Process::setid(int ID)
{
	id = ID;
}


Process::~Process()
{
}
