teaches_subject(jatin_sir,math).
teaches_subject(datta_sir,math).

teaches_subject(shrida_maam,dsa).
teaches_subject(ashwini_maam,dsa).

teaches_subject(vaibhav_sir,ppl).
teaches_subject(sumit_sir,ppl).

teaches_subject(pravin_sir,dld).

teaches_subject(aghav_sir,dtl).

 
has_subject(math_dept,math).

has_subject(comp_dept,dsa).

has_subject(comp_dept,ppl).

has_subject(comp_dept,dtl).

 

 

has_student(comp_dept,s1).

has_student(comp_dept,s2).

 

 

has_faculty(D,F) :- teaches_subject(F,S) , has_subject(D,S).

studies_subject(ST,SB) :- has_student(D,ST) , has_subject(D,SB).

studies_under(S,F) :- has_subject(D,SB) , has_student(D,S) , teaches_subject(F,SB).