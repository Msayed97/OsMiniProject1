#include "ProcessGenerator.h"



ProcessGenerator::ProcessGenerator(string Input)
{
	InputPath = Input;
}




ProcessGenerator::~ProcessGenerator()
{
}
void ProcessGenerator::ReadInput()
{
	ifstream inFile;
	inFile.open(InputPath);

	inFile >> NumOfProcesses;
	inFile >> ArrivalTMean>>ArrivalTVariance;
	inFile >> BurstTMean>>BurstTVariance;
	inFile >> priorityLambda;
	inFile.close();
}

void ProcessGenerator::GenerateOuput(string OutputPath)
{    
	// create random generator for every distribution
	std::random_device rd;

	std::mt19937 e2(rd());

	normal_distribution<double> ArrivalDistribution(ArrivalTMean, ArrivalTVariance);
	
	
	normal_distribution<double> BurstDistribution(BurstTMean, BurstTVariance);

	poisson_distribution<int> PoissonPriority(priorityLambda);

	// write the output to the file
	ofstream myfile;
	myfile.open(OutputPath);
	myfile << NumOfProcesses << endl;
	for (int  i = 0; i < NumOfProcesses; i++)
	{
		myfile << i + 1 << " " << round(abs(ArrivalDistribution(e2))) << " " << round(abs(BurstDistribution(e2))) << " " << PoissonPriority(e2) << endl;
	}
	myfile.close();
}