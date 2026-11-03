from fractions import Fraction as F
from math import comb
import json,gzip,sys,traceback
sys.set_int_max_str_digits(1000000)
source=sys.argv[1];dest=sys.argv[2];count=0
with open(source) as inp,open(dest,'xb') as raw,gzip.GzipFile(filename='',fileobj=raw,mode='wb',mtime=0) as out:
 for line in inp:
  rec=json.loads(line); d={'source_record':rec}
  try:
   M=rec['M'];n=M//4;k=M//1024;theta=F(rec['theta_num'],rec['theta_den']);p=F(1)
   for b in rec['row']:p*=theta if b=='1' else 1-theta
   T=F(M,512)+2*k;last=(T.numerator-1)//T.denominator; a=int(16*p); den=16**n;terms=[comb(n,j)*a**j*(16-a)**(n-j) for j in range(min(last,n)+1)];num=sum(terms); bn=1023**M;bd=1024**M;left=num*bd;right=bn*den
   d['independent']={'n':n,'k':k,'theta_num':theta.numerator,'theta_den':theta.denominator,'p_num':p.numerator,'p_den':p.denominator,'a':a,'mean_num':(n*p).numerator,'mean_den':(n*p).denominator,'threshold_num':T.numerator,'threshold_den':T.denominator,'last':last,'denominator':str(den),'terms':[str(v) for v in terms],'numerator':str(num),'bound_num':str(bn),'bound_den':str(bd),'left_cross_product':str(left),'right_cross_product':str(right),'comparison':left<=right}
   assert rec['k']==k and rec['disjoint_pairs_n']==n and p==F(a,16) and rec['match_p_num_over_16']==a and F(rec['mean_num'],rec['mean_den'])==n*p and F(rec['threshold_num'],rec['threshold_den'])==T and rec['last_included_count']==last and int(rec['tail_denominator_decimal'])==den and list(map(int,rec['tail_term_numerators_decimal']))==terms and int(rec['tail_numerator_decimal'])==num and rec['exact_rational_comparison_pass'] and left<=right
   d['status']='PASS';count+=1
  except Exception as ex:
   d['status']='FAIL';d['error']=repr(ex);d['traceback']=traceback.format_exc();out.write((json.dumps(d,separators=(',',':'))+'\n').encode());raise
  out.write((json.dumps(d,separators=(',',':'))+'\n').encode())
assert count==60
print('verified_source_records',count,'PASS; per-case source and all computed comparison values retained')
