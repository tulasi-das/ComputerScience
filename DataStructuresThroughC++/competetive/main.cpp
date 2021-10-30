#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int n;
	int a[3];
	cin>>n;


	for(int i=1;i<=n;n++){
            for(int i=0;i<3;i++){
	    cin>>a[i];
	}
	int count = 0;
	    for(int j=0;j<3;j++){
	        if(a[j]==7){
	            count+=1;
	        }
	    }
    if(count>1){
        cout<<"YES";
    }else
        cout<<"NO";

	}


	return 0;
}

