#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
def twoTwo(a):
    #
    # Write your code here.
    #    
    def findlentwo():
        dmpln1 = []
        for i in range(0,801):
            ln = len(str(pow(2,i)))
            if ln not in dmpln1:
                dmpln1.append(ln)
        return dmpln1

    dmpln1 = findlentwo()
    num = 0
    l = len(a)+1
    
    for i in dmpln1: #range(1,l):
        for j in range(0,(l-i)):
            ans = int(a[j:j+i])
            if (int(a[j]) > 0 ): 
                if (ans & (ans - 1)):
                    continue
                else:
                    num += 1
                    #print(a[j:j+i])
                    
    return int(num)


# In[2]:


st = time.time()
#a = "9303535670983768199031344740966458039726609416797671171603074549512182887851493418575245449136173639177760276560207077549242900846267596823817051317718446589520242536874132581700120107002038199303870846751188192899823151552628349788604516295066307994130118526061826166445047808309163001841380667575628151274558987543914186376514799892578820116121531383164833962895501326553806236997089282520174174189206292883439012459432693877366459895758465185873923518437208883287869410049671804351768330228241833181048771841834309240249132277574952747489997467168763400466618303709392785810954982875161446396373040800947562126272731545618170968107390172263733095197200113358841034017182951507037254979515982202834948083154776267844089139019063040156654448338365040715366458968162887836583628774290327941701420576894069006881693378223441337877537377325813845730080900918242835443359855685076558915384842574884883772410178635875682021801984576460752303423488223007451985306231415357182726483615059804162147483648324"
a = "1844674407370955161674106937111882365071085430405560261026092790186009960985252853765064402969559046455624695217271474139797930007529685824264482073058782076648391351619055042102986574113383200344578589757929931868733441327844982041917746723970516381171568323982794317579807998610345501008899652130606847906255663073214172223323715616252538366448344131768098523799946916468379859578177088483047579320327229475734293036792189718636043847330179466014340038463189508943008496205724668159759037237747788792245498535675607031239995639976648680825923975906526582032462837994195753268665938105581321030972818840265816397736281374726739986666787659948666753771754907668409286105635143120275902562304104187725513747723032497684230019653080386848786186065006191528308813081840900501117522378138618035792858279853022394381967012525845615079380677438317669219470236837179906477475985598217372094136390078377123228155963917938085569707674435584356811923176489970264571492362373784095686656302231454903657293676544"
ans = twoTwo(a)
print(time.time()-st)
print(ans)


# In[ ]:




