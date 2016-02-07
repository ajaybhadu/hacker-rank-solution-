#include<bits/stdc++.h>
using namespace std;

#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)

#define mygc(c) (c)=getchar_unlocked()
#define mypc(c) putchar_unlocked(c)

#define ll long long

void llIntSort(ll d[],int m[],int s){int i,j,a;ll k,t;if(s<=1)return;k=(d[0]+d[s-1])/2;i=-1;j=s;for(;;){while(d[++i]<k);while(d[--j]>k);if(i>=j)break;t=d[i];d[i]=d[j];d[j]=t;a=m[i];m[i]=m[j];m[j]=a;}llIntSort(d,m,i);llIntSort(d+j+1,m+j+1,s-j-1);}

void charCreateSuffixArray(char t[], int n, int res[], void *WorkMemory) {
  int i, h, *g, *b; ll *d;

  g = (int*)WorkMemory; WorkMemory = (void*)(g+n+1);
  b = (int*)WorkMemory; WorkMemory = (void*)(b+n+1);
  d = (ll*) WorkMemory;
  
  rep(i,n+1) res[i] = i, d[i] = g[i] = t[i];
  b[0] = 0; b[n] = 0;

  llIntSort(d,res,n+1);
  for(h=1;b[n]!=n;h*=2){
    rep(i,n+1){
      d[i] = g[res[i]] * (1LL<<32);
      if(res[i]+h<n+1) d[i] += g[res[i]+h];
    }
    llIntSort(d,res,n+1);
    rep(i,n){ b[i+1]=b[i]; if(g[res[i]]!=g[res[i+1]]||g[res[i]+h]!=g[res[i+1]+h]) b[i+1]++; }
    rep(i,n+1) g[res[i]]=b[i];
  }
}

/* Kasai-Lee-Arimura-Arikawa-Park: O(n) */
void charCreateLCPFromSA(char *t, int n, int *SA, int *res, void *WorkMemory) {
  int i, j, h=0, *b;

  b = (int*)WorkMemory;

  rep(i,n+1) b[SA[i]]=i;
  rep(i,n+1){
    if(b[i]){
      for(j=SA[b[i]-1];j+h<n&&i+h<n&&t[j+h]==t[i+h];h++);
      res[b[i]]=h;
    }else res[b[i]] = -1;
    if(h>0)h--;
  }
}

void reader(int *x){int k,m=0;*x=0;for(;;){mygc(k);if(k=='-'){m=1;break;}if('0'<=k&&k<='9'){*x=k-'0';break;}}for(;;){mygc(k);if(k<'0'||k>'9')break;*x=(*x)*10+k-'0';}if(m)(*x)=-(*x);}
void reader(ll *x){int k,m=0;*x=0;for(;;){mygc(k);if(k=='-'){m=1;break;}if('0'<=k&&k<='9'){*x=k-'0';break;}}for(;;){mygc(k);if(k<'0'||k>'9')break;*x=(*x)*10+k-'0';}if(m)(*x)=-(*x);}
int reader(char c[]){int i,s=0;for(;;){mygc(i);if(i!=' '&&i!='\n'&&i!='\r'&&i!='\t'&&i!=EOF) break;}c[s++]=i;for(;;){mygc(i);if(i==' '||i=='\n'||i=='\r'||i=='\t'||i==EOF) break;c[s++]=i;}return s;}
void writer(const char c[]){int i;for(i=0;c[i]!='\0';i++)mypc(c[i]);}

int T, N;
char S[200000];
ll K;

int SA[200000], LCP[200000];
int mem[2000000];

char res[10];

int main(){
  int i, j;
  ll len, all;

  scanf("%d",&T); //reader(&T);
  while(T--){
    scanf("%s",S); N = strlen(S); //N = reader(S);
    scanf("%lld",&K); // reader(&K);
    K--;
    assert(K>=0);

    rep(i,N) assert('a'<=S[i] && S[i]<='z');

    charCreateSuffixArray(S, N, SA, mem);
    charCreateLCPFromSA(S, N, SA, LCP, mem);

    res[0] = 0;
    REP(i,1,N+1){
      len = N - SA[i];
      all = len * (len+1) / 2 - ((ll)LCP[i] * (LCP[i]+1)) / 2;
      if(K >= all){ K -= all; continue; }
      REP(j,LCP[i],len){
        if(K >= j+1){ K -= j+1; continue; }
        res[0] = S[SA[i]+K];
        break;
      }
      assert(j<len);
      break;
    }
    assert(res[0]!=0);

    res[1] = '\n';
    res[2] = '\0';
    writer(res);
  }


  return 0;
}
