#include <bits/stdc++.h>
#include <sys/resource.h>
using namespace std;
using Clock=chrono::steady_clock;
struct Node { uint32_t prev; uint16_t j,c,d; uint8_t pair,cost,bit; };
static uint64_t key(int j,int c,int d,int pair){return (((uint64_t)j<<16)|((uint64_t)c<<8)|d)<<2|pair;}
int main(int argc,char**argv){
 if(argc!=6){cerr<<"M k word cap_nodes cap_seconds\n";return 2;}
 int M=stoi(argv[1]), k=stoi(argv[2]); string h=argv[3]; size_t cap=stoull(argv[4]); double limit=stod(argv[5]);
 if(M<4||M>128||k<0||k>M||(int)h.size()!=M+2)return 3;
 auto begin=Clock::now(); clock_t cb=clock();
 int row=2*(h[M]-'0')+h[M+1]-'0';int J0=0,C0=0;
 for(int i=0;i<M;i++)if(2*(h[i]-'0')+h[i+1]-'0'==row){J0++;C0+=h[i+2]-'0';}
 double target=(C0+1.0)/(J0+2.0),eps=1/sqrt((double)M);
 vector<Node> nodes; nodes.reserve(min(cap,size_t(3000000)));vector<uint32_t> layer;
 for(int a=0;a<2;a++)for(int b=0;b<2;b++){
  int co=(a!=h[0]-'0')+(b!=h[1]-'0');if(co>k)continue;
  nodes.push_back({UINT32_MAX,0,0,0,(uint8_t)(2*a+b),(uint8_t)co,(uint8_t)(2*a+b)});layer.push_back(nodes.size()-1);
 }
 size_t peak=layer.size();string status="ok";
 for(int t=2;t<M+2 && status=="ok";t++){
  unordered_map<uint64_t,uint32_t> lookup;lookup.reserve(min(size_t(600001),layer.size()*2+1));vector<uint32_t> next;
  for(auto id:layer){
   Node n=nodes[id];
   for(int b=0;b<2;b++){
    if(t>=M && b!=h[t]-'0')continue;
    int co=n.cost+(t<M && b!=h[t]-'0');if(co>k)continue;
    int match=n.pair==row,j=n.j+match,c=n.c+match*b,d=n.d+(match && t-2<M/2),np=(n.pair%2)*2+b;
    auto code=key(j,c,d,np);auto p=lookup.find(code);
    if(p==lookup.end()){
      if(next.size()>=300000||nodes.size()>=cap){status="state_cap";break;}
      nodes.push_back({id,(uint16_t)j,(uint16_t)c,(uint16_t)d,(uint8_t)np,(uint8_t)co,(uint8_t)b}); uint32_t nn=nodes.size()-1;lookup.emplace(code,nn);next.push_back(nn);
    } else if(co<nodes[p->second].cost){Node &x=nodes[p->second];x.cost=co;x.prev=id;x.bit=b;}
   }
   if(status!="ok")break;
   if(chrono::duration<double>(Clock::now()-begin).count()>limit){status="time_cap";break;}
  }
  if(status!="ok")break;layer.swap(next);peak=max(peak,layer.size());
 }
 double best=-1;string witness="-";int bj=-1,bc=-1,bd=-1;
 if(status=="ok"){
  uint32_t bestid=UINT32_MAX;
  for(auto id:layer){auto &n=nodes[id];double a=(n.j>0 && 512*n.d>=n.j)?double(n.c)/n.j:double(row/2);double q=(1-2*eps)*a+eps;
   double loss=-target*log(q)-(1-target)*log1p(-q);if(loss>best){best=loss;bestid=id;bj=n.j;bc=n.c;bd=n.d;}}
  if(bestid==UINT32_MAX)return 4;
  witness=string(M+2,'?');uint32_t id=bestid;
  for(int t=M+1;t>=2;t--){Node n=nodes[id];witness[t]='0'+n.bit;id=n.prev;}
  witness[0]='0'+nodes[id].pair/2;witness[1]='0'+nodes[id].pair%2;
 }
 struct rusage r{};getrusage(RUSAGE_SELF,&r);
 cout<<setprecision(17)<<status<<","<<chrono::duration<double>(Clock::now()-begin).count()<<","<<double(clock()-cb)/CLOCKS_PER_SEC<<","<<r.ru_maxrss<<","<<peak<<","<<nodes.size()<<","<<best<<","<<bj<<","<<bc<<","<<bd<<","<<witness<<"\n";
}
