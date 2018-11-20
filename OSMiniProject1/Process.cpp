#include "Process.h"

Process::Process(float arrival, float brust, int priority )
{
	setArrivalTime(arrival);
	setBrustTime(brust);
	setPriority(priority);
}

float Process::getArrivalTime()
{
	return arrivalTime;
}

float Process::getBrustTime()
{
	return brustTime;
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

void Process::setBrustTime(float t)
{
	if (t > 0)
	{
		brustTime = t;
	}
}

void Process::setPriority(int p)
{
	if (p >= 0)
	{
		priority = p;
	}
}


Process::~Process()
{
}
