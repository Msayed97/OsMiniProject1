#pragma once
class Process
{
	int id;
	float arrivalTime;
	float burstTime;
	float turnaroundTime;
	float weightedTat;
	float finishingTime;
	float remainingTime;
	int priority;
public:
	Process(int id , float arrival , float burst , int priority);
	float getArrivalTime();
	float getburstTime();
	int getPriority();
	float getTurnaroundTime();
	float getFinishingTime();
	float getweightedTat();
	float getremainingTime();
	float getid();

	void setFinishingTime(float t);
	void setTurnaroundTime(float t);
	void setArrivalTime(float t);
	void setburstTime(float t);
	void setPriority(int p);
	void setremainingTime(int r);
	float setid(int i);
	~Process();
};

