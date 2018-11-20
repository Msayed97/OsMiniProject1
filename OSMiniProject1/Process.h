#pragma once
class Process
{
	float arrivalTime;
	float brustTime;
	float turnaroundTime;
	float finishingTime;
	int priority;
public:
	Process(float arrival , float brust , int priority);
	float getArrivalTime();
	float getBrustTime();
	int getPriority();
	float getTurnaroundTime();
	float getFinishingTime();
	void setFinishingTime(float t);
	void setTurnaroundTime(float t);
	void setArrivalTime(float t);
	void setBrustTime(float t);
	void setPriority(int p);

	~Process();
};

