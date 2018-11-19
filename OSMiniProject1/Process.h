#pragma once
class Process
{
	float arrivalTime;
	float brustTime;
	float turnaroundTime;
	int priority;
public:
	Process(int arrival , int brust , int priority);
	float getArrivalTime();
	float getBrustTime();
	int getPriority();
	float getTurnaroundTime();
	void setTurnaroundTime(float t);
	void setArrivalTime(float t);
	void setBrustTime(float t);
	void setPriority(int p);

	~Process();
};

