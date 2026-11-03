from fractions import Fraction
from math import comb
import json, sys
sys.set_int_max_str_digits(1000000)

with open('v10_research/half_gate_iid_identifiability_20261103_1009/comprehensive_records.jsonl','x') as f:
    for M in (8,64,1024,4096,16384):
        n = M//4
        k = M//1024
        threshold = Fraction(M,512)+2*k
        last = (threshold.numerator-1)//threshold.denominator
        for t_num in (1,2,3):
            theta=Fraction(t_num,4)
            for row in ('00','01','10','11'):
                p=Fraction(1)
                for bit in row:
                    p *= theta if bit=='1' else 1-theta
                a=int(16*p)
                assert Fraction(a,16)==p
                mu=n*p
                denominator=16**n
                terms=[comb(n,j)*a**j*(16-a)**(n-j) for j in range(min(n,last)+1)]
                numerator=sum(terms)
                assert mu>=Fraction(M,128)
                assert threshold<=mu/2
                # (1-1/1024)^M <= exp(-M/1024); this exact rational comparison is stronger.
                rational_bound_num=1023**M
                rational_bound_den=1024**M
                assert numerator*rational_bound_den <= rational_bound_num*denominator
                record={'M':M,'k':k,'theta_num':t_num,'theta_den':4,'row':row,
                        'disjoint_pairs_n':n,'match_p_num_over_16':a,
                        'mean_num':mu.numerator,'mean_den':mu.denominator,
                        'threshold_num':threshold.numerator,'threshold_den':threshold.denominator,
                        'last_included_count':last,'tail_denominator_decimal':str(denominator),
                        'tail_term_numerators_decimal':[str(v) for v in terms],
                        'tail_numerator_decimal':str(numerator),
                        'comparison_bound':'(1023/1024)^M',
                        'exact_rational_comparison_pass':True}
                f.write(json.dumps(record,sort_keys=True)+'\n')
print('PASS: 60 independent exact rational case records, summands included')
