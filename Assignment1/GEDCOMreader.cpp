#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
	ifstream gedcom("FamilyTree.txt");
	//gedcom.open();
	//Opens the file and attempts to read each line
	printf("It worked asshole!");
	if(!gedcom){
		cout << "There appears to be an error withn opening the GEDCOM file" << endl;
	}
	else {
		cout << "The GEDCOM file opened" << endl;
	}
	while(!gedcom.eof()){
	}
	return(0);
}