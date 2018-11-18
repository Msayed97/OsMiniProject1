#pragma once
#include <iostream>
using namespace std;
#include <fstream>
#include<string>
#include <random>
#include <chrono>

class ProcessGenerator
{
	string InputPath;
	int NumOfProcesses;
	float ArrivalTMean;
	float ArrivalTVariance;
	float BurstTMean;
	float BurstTVariance;
	float priorityLambda;

public:
	ProcessGenerator(string );
	void GenerateOuput(string);
	~ProcessGenerator();
	void ReadInput();
};

