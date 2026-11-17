// Exact necessary scan of all minimal common orders <=96. C++17, no floating point.
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <vector>
using Row=std::array<long long,4>;
// Rank uses minors of the original rows. Every input entry has absolute value<=4;
// all determinants/intermediate sums have absolute value<=4!*4^4=6144.
long long determinant(const std::vector<Row>& rows,const std::vector<int>& cols){
 int n=cols.size();if(n==1)return rows[0][cols[0]];long long out=0;
 for(int j=0;j<n;j++){std::vector<Row> rest(rows.begin()+1,rows.end());auto c=cols;c.erase(c.begin()+j);out+=(j%2?-1:1)*rows[0][cols[j]]*determinant(rest,c);}return out;
}
struct Rank {std::vector<Row> rows;int n=0;void add(Row r){
 if(n==4)return;rows.push_back(r);bool nonzero=false;
 for(int mask=1;mask<16;mask++){std::vector<int> cols;for(int j=0;j<4;j++)if(mask&(1<<j))cols.push_back(j);if(int(cols.size())!=n+1)continue;if(determinant(rows,cols)){nonzero=true;break;}}
 if(nonzero)n++;else rows.pop_back();
}};
bool rank4(int N,int a[4]){Rank R;std::vector<std::pair<int,Row>> quad;
 for(int i=0;i<4;i++)for(int j=i;j<4;j++){Row v{};v[i]++;v[j]++;int s=(a[i]+a[j])%N;for(auto &[t,w]:quad)if(s==t){Row d;for(int k=0;k<4;k++)d[k]=v[k]-w[k];R.add(d);}quad.push_back({s,v});}
 for(int i=0;i<4;i++)for(int j=i;j<4;j++)for(int k=j;k<4;k++)if((a[i]+a[j]+a[k])%N==0){Row v{};v[i]++;v[j]++;v[k]++;R.add(v);}
 for(int i=0;i<4;i++)for(int j=i;j<4;j++)for(int k=j;k<4;k++)for(int l=k;l<4;l++)if((a[i]+a[j]+a[k]+a[l])%N==0&&(i!=l||2*a[i]==N)){Row v{};v[i]++;v[j]++;v[k]++;v[l]++;R.add(v);}
 return R.n==4;}
bool feasible(int N,int a[4]){int d[96]{},cap[96]{};for(int i=0;i<4;i++)for(int j=0;j<4;j++)d[(a[i]+a[j])%N]++;for(int j=0;j<N;j++)cap[j]=std::max(0,d[j]-1);unsigned dp=1;
 for(int s=0;s<=N/2;s++){int t=(N-s)%N;if(s>t)continue;unsigned ndp=0;if(s==t){for(int r=0;r<=cap[s]&&r<=6;r++)if(s==0||r%2==0)ndp|=dp<<r;}else{int m=std::min(cap[s],cap[t]);for(int r=0;r<=m&&r<=3;r++)ndp|=dp<<(2*r);}dp=ndp&127;}return dp&64;}
int main(){long long total=0,quadratic=0,cubic=0,quartic=0,rawrank4=0;std::vector<std::array<int,5>> result;
 for(int N=4;N<=96;N++)for(int a=0;a<N;a++)for(int b=a+1;b<N;b++)for(int c=b+1;c<N;c++)for(int d=c+1;d<N;d++){
  if(std::gcd(N,std::gcd(a,std::gcd(b,std::gcd(c,d))))!=1)continue;total++;int p[4]={a,b,c,d};std::uint64_t bits[2]{};bool collision=false;
  for(int i=0;i<4;i++)for(int j=i;j<4;j++){int v=(p[i]+p[j])%N;auto bit=std::uint64_t(1)<<(v%64);int k=v/64;if(bits[k]&bit)collision=true;bits[k]|=bit;}if(!collision)continue;quadratic++;
  int pure=0,mixed=0;for(int i=0;i<4;i++)for(int j=i;j<4;j++)for(int k=j;k<4;k++)if((p[i]+p[j]+p[k])%N==0){if(i==k)pure++;else mixed++;}if(!mixed&&pure<2)continue;cubic++;
  int support=0;for(int i=0;i<4;i++)for(int j=i;j<4;j++)for(int k=j;k<4;k++)for(int l=k;l<4;l++)if((p[i]+p[j]+p[k]+p[l])%N==0&&(i!=l||2*p[i]==N))support|=(1<<i)|(1<<j)|(1<<k)|(1<<l);if(support!=15)continue;quartic++;
  if(!rank4(N,p))continue;rawrank4++;if(!feasible(N,p))continue;result.push_back({N,a,b,c,d});
 }
 std::cout<<"{\"counts\":{\"minimal_order_sets\":"<<total<<",\"quadratic_collision\":"<<quadratic<<",\"cubic_resonance\":"<<cubic<<",\"quartic_support\":"<<quartic<<",\"raw_rank4\":"<<rawrank4<<",\"frobenius_feasible\":"<<result.size()<<"},\"candidates\":[";
 bool first=true;for(auto &r:result){if(!first)std::cout<<",";first=false;std::cout<<"[";for(int i=0;i<5;i++){if(i)std::cout<<",";std::cout<<r[i];}std::cout<<"]";}std::cout<<"]}\n";
}
