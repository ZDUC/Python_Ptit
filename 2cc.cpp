#include <bits/stdc++.h>
using namespace std;
int n,a[20],b[20];
string c="ABCDEFGHIJKLMNOPQRSTUVXY";
void in()
{
	for(int i=1;i<=n;i++) cout<<c[a[i]-1]<<" ";
	cout<<endl;
}
void quaylui(int i)
{
	int j;
	for(j=1;j<=n;j++)
	{
		if(b[j]==0)
		{
			a[i]=j;b[j]=1;
			if(i==n) in();
			else quaylui(i+1);
			b[j]=0;
		}
	}
}
int main()
{
	cin>>n;
	quaylui(1);
}