import os
import numpy as np
import mne

#KAZIMEEG

file1 = r"C:\Users\selu-user\Desktop\BCI-Image Reconstruction\EEGdata\KazimEEG\Kazim\20220311231154_Patient01.nedf"

data1 = mne.io.read_raw_nedf(file1)
raw_data1 = data1.get_data()


info = data1.info
channels = data1.ch_names

events = mne.find_events(data1, stim_channel='STI 014')
#epochs = mne.Epochs(data1, events, tmin=-0.3, tmax=0.7)



print(raw_data1) 
data1.plot
data1.plot_psd(fmax=50)
data1.plot(duration=20, n_channels=31)





ica = mne.preprocessing.ICA(n_components=0.95, random_state=97, max_iter=800)
ica.fit(data1)
ica.exclude = [1, 2]
ica.plot_properties(data1, picks=ica.exclude)



#Channels
ch1=raw_data1[0]
ch2=raw_data1[1]
ch3=raw_data1[2]
ch4=raw_data1[3]
ch5=raw_data1[4]
ch6=raw_data1[5]
ch7=raw_data1[6]
ch8=raw_data1[7]
ch9=raw_data1[8]
ch10=raw_data1[9]
ch11=raw_data1[10]
ch12=raw_data1[11]
ch13=raw_data1[12]
ch14=raw_data1[13]
ch15=raw_data1[14]
ch16=raw_data1[15]
ch17=raw_data1[16]
ch18=raw_data1[17]
ch19=raw_data1[18]
ch20=raw_data1[19]
ch21=raw_data1[20]
ch22=raw_data1[21]
ch23=raw_data1[22]
ch24=raw_data1[23]
ch25=raw_data1[24]
ch26=raw_data1[25]
ch27=raw_data1[26]
ch28=raw_data1[27]
ch29=raw_data1[28]
ch30=raw_data1[29]
ch31=raw_data1[30]
ch32=raw_data1[31]


#Channel_1 EVENTS
ch1_eyeopen = ch1[0:30000]
ch1_eyeclosed = ch1[30000:60000]

ch1_A = ch1[60000:62500]
ch1_Arest= ch1[62500:65000] 
ch1_Aimagine= ch1[65000:67500] 

ch1_B = ch1[67500:70000]
ch1_Brest= ch1[70000:72500] 
ch1_Bimagine= ch1[72500:75000] 

ch1_C = ch1[75000:77500]
ch1_Crest= ch1[77500:80000] 
ch1_Cimagine= ch1[80000:82500]

ch1_D = ch1[82500:85000]
ch1_Drest= ch1[85000:87500] 
ch1_Dimagine= ch1[87500:90000]

ch1_E = ch1[90000:92500]
ch1_Erest= ch1[92500:95000] 
ch1_Eimagine= ch1[95000:97500]

ch1_F = ch1[97500:100000]
ch1_Frest= ch1[100000:102500] 
ch1_Fimagine= ch1[102500:105000] 

ch1_G = ch1[105000:107500]
ch1_Grest= ch1[107500:110000] 
ch1_Gimagine= ch1[110000:112500]

ch1_H = ch1[112500:115000]
ch1_Hrest= ch1[115000:117500] 
ch1_Himagine= ch1[117500:120000]

ch1_I = ch1[120000:122500]
ch1_Irest= ch1[122500:125000] 
ch1_Iimagine= ch1[125000:127500]

ch1_J = ch1[127500:130000]
ch1_Jrest= ch1[130000:132500] 
ch1_Jimagine= ch1[132500:135000] 

ch1_K = ch1[135000:137500]
ch1_Krest= ch1[137500:140000] 
ch1_Kimagine= ch1[140000:142500]

ch1_L = ch1[142500:145000]
ch1_Lrest= ch1[145000:147500] 
ch1_Limagine= ch1[147500:150000]

ch1_M = ch1[150000:152500]
ch1_Mrest= ch1[152500:155000] 
ch1_Mimagine= ch1[155000:157500]

ch1_N = ch1[157500:160000]
ch1_Nrest= ch1[160000:162500] 
ch1_Nimagine= ch1[162500:165000] 

ch1_O = ch1[165000:167500]
ch1_Orest= ch1[167500:170000] 
ch1_Oimagine= ch1[170000:172500]

ch1_P = ch1[172500:175000]
ch1_Prest= ch1[175000:177500] 
ch1_Pimagine= ch1[177500:180000]

ch1_Q = ch1[180000:182500]
ch1_Qrest= ch1[182500:185000] 
ch1_Qimagine= ch1[185000:187500]

ch1_R = ch1[187500:190000]
ch1_Rrest= ch1[190000:192500] 
ch1_Rimagine= ch1[192500:195000] 

ch1_S = ch1[195000:197500]
ch1_Srest= ch1[197500:200000] 
ch1_Simagine= ch1[200000:202500]

ch1_T = ch1[202500:205000]
ch1_Trest= ch1[205000:207500] 
ch1_Timagine= ch1[207500:210000]

ch1_U = ch1[210000:212500]
ch1_Urest= ch1[212500:215000] 
ch1_Uimagine= ch1[215000:217500]

ch1_V = ch1[217500:220000]
ch1_Vrest= ch1[220000:222500] 
ch1_Vimagine= ch1[222500:225000] 

ch1_W = ch1[225000:227500]
ch1_Wrest= ch1[227500:230000] 
ch1_Wimagine= ch1[230000:232500]

ch1_X = ch1[232500:235000]
ch1_Xrest= ch1[235000:237500] 
ch1_Ximagine= ch1[237500:240000]

ch1_Y = ch1[240000:242500]
ch1_Yrest= ch1[242500:245000] 
ch1_Yimagine= ch1[245000:247500]

ch1_Z = ch1[247500:250000]
ch1_Zrest= ch1[250000:252500] 
ch1_Zimagine= ch1[252500:255000]




#Channel_2 EVENTS
ch2_eyeopen = ch2[0:30000]
ch2_eyeclosed = ch2[30000:60000]

ch2_A = ch2[60000:62500]
ch2_Arest= ch2[62500:65000] 
ch2_Aimagine= ch2[65000:67500] 

ch2_B = ch2[67500:70000]
ch2_Brest= ch2[70000:72500] 
ch2_Bimagine= ch2[72500:75000] 

ch2_C = ch2[75000:77500]
ch2_Crest= ch2[77500:80000] 
ch2_Cimagine= ch2[80000:82500]

ch2_D = ch2[82500:85000]
ch2_Drest= ch2[85000:87500] 
ch2_Dimagine= ch2[87500:90000]

ch2_E = ch2[90000:92500]
ch2_Erest= ch2[92500:95000] 
ch2_Eimagine= ch2[95000:97500]

ch2_F = ch2[97500:100000]
ch2_Frest= ch2[100000:102500] 
ch2_Fimagine= ch2[102500:105000] 

ch2_G = ch2[105000:107500]
ch2_Grest= ch2[107500:110000] 
ch2_Gimagine= ch2[110000:112500]

ch2_H = ch2[112500:115000]
ch2_Hrest= ch2[115000:117500] 
ch2_Himagine= ch2[117500:120000]

ch2_I = ch2[120000:122500]
ch2_Irest= ch2[122500:125000] 
ch2_Iimagine= ch2[125000:127500]

ch2_J = ch2[127500:130000]
ch2_Jrest= ch2[130000:132500] 
ch2_Jimagine= ch2[132500:135000] 

ch2_K = ch2[135000:137500]
ch2_Krest= ch2[137500:140000] 
ch2_Kimagine= ch2[140000:142500]

ch2_L = ch2[142500:145000]
ch2_Lrest= ch2[145000:147500] 
ch2_Limagine= ch2[147500:150000]

ch2_M = ch2[150000:152500]
ch2_Mrest= ch2[152500:155000] 
ch2_Mimagine= ch2[155000:157500]

ch2_N = ch2[157500:160000]
ch2_Nrest= ch2[160000:162500] 
ch2_Nimagine= ch2[162500:165000] 

ch2_O = ch2[165000:167500]
ch2_Orest= ch2[167500:170000] 
ch2_Oimagine= ch2[170000:172500]

ch2_P = ch2[172500:175000]
ch2_Prest= ch2[175000:177500] 
ch2_Pimagine= ch2[177500:180000]

ch2_Q = ch2[180000:182500]
ch2_Qrest= ch2[182500:185000] 
ch2_Qimagine= ch2[185000:187500]

ch2_R = ch2[187500:190000]
ch2_Rrest= ch2[190000:192500] 
ch2_Rimagine= ch2[192500:195000] 

ch2_S = ch2[195000:197500]
ch2_Srest= ch2[197500:200000] 
ch2_Simagine= ch2[200000:202500]

ch2_T = ch2[202500:205000]
ch2_Trest= ch2[205000:207500] 
ch2_Timagine= ch2[207500:210000]

ch2_U = ch2[210000:212500]
ch2_Urest= ch2[212500:215000] 
ch2_Uimagine= ch2[215000:217500]

ch2_V = ch2[217500:220000]
ch2_Vrest= ch2[220000:222500] 
ch2_Vimagine= ch2[222500:225000] 

ch2_W = ch2[225000:227500]
ch2_Wrest= ch2[227500:230000] 
ch2_Wimagine= ch2[230000:232500]

ch2_X = ch2[232500:235000]
ch2_Xrest= ch2[235000:237500] 
ch2_Ximagine= ch2[237500:240000]

ch2_Y = ch2[240000:242500]
ch2_Yrest= ch2[242500:245000] 
ch2_Yimagine= ch2[245000:247500]

ch2_Z = ch2[247500:250000]
ch2_Zrest= ch2[250000:252500] 
ch2_Zimagine= ch2[252500:255000]



#Channel_3 EVENTS
ch3_eyeopen = ch3[0:30000]
ch3_eyeclosed = ch3[30000:60000]

ch3_A = ch3[60000:62500]
ch3_Arest= ch3[62500:65000] 
ch3_Aimagine= ch3[65000:67500] 

ch3_B = ch3[67500:70000]
ch3_Brest= ch3[70000:72500] 
ch3_Bimagine= ch3[72500:75000] 

ch3_C = ch3[75000:77500]
ch3_Crest= ch3[77500:80000] 
ch3_Cimagine= ch3[80000:82500]

ch3_D = ch3[82500:85000]
ch3_Drest= ch3[85000:87500] 
ch3_Dimagine= ch3[87500:90000]

ch3_E = ch3[90000:92500]
ch3_Erest= ch3[92500:95000] 
ch3_Eimagine= ch3[95000:97500]

ch3_F = ch3[97500:100000]
ch3_Frest= ch3[100000:102500] 
ch3_Fimagine= ch3[102500:105000] 

ch3_G = ch3[105000:107500]
ch3_Grest= ch3[107500:110000] 
ch3_Gimagine= ch3[110000:112500]

ch3_H = ch3[112500:115000]
ch3_Hrest= ch3[115000:117500] 
ch3_Himagine= ch3[117500:120000]

ch3_I = ch3[120000:122500]
ch3_Irest= ch3[122500:125000] 
ch3_Iimagine= ch3[125000:127500]

ch3_J = ch3[127500:130000]
ch3_Jrest= ch3[130000:132500] 
ch3_Jimagine= ch3[132500:135000] 

ch3_K = ch3[135000:137500]
ch3_Krest= ch3[137500:140000] 
ch3_Kimagine= ch3[140000:142500]

ch3_L = ch3[142500:145000]
ch3_Lrest= ch3[145000:147500] 
ch3_Limagine= ch3[147500:150000]

ch3_M = ch3[150000:152500]
ch3_Mrest= ch3[152500:155000] 
ch3_Mimagine= ch3[155000:157500]

ch3_N = ch3[157500:160000]
ch3_Nrest= ch3[160000:162500] 
ch3_Nimagine= ch3[162500:165000] 

ch3_O = ch3[165000:167500]
ch3_Orest= ch3[167500:170000] 
ch3_Oimagine= ch3[170000:172500]

ch3_P = ch3[172500:175000]
ch3_Prest= ch3[175000:177500] 
ch3_Pimagine= ch3[177500:180000]

ch3_Q = ch3[180000:182500]
ch3_Qrest= ch3[182500:185000] 
ch3_Qimagine= ch3[185000:187500]

ch3_R = ch3[187500:190000]
ch3_Rrest= ch3[190000:192500] 
ch3_Rimagine= ch3[192500:195000] 

ch3_S = ch3[195000:197500]
ch3_Srest= ch3[197500:200000] 
ch3_Simagine= ch3[200000:202500]

ch3_T = ch3[202500:205000]
ch3_Trest= ch3[205000:207500] 
ch3_Timagine= ch3[207500:210000]

ch3_U = ch3[210000:212500]
ch3_Urest= ch3[212500:215000] 
ch3_Uimagine= ch3[215000:217500]

ch3_V = ch3[217500:220000]
ch3_Vrest= ch3[220000:222500] 
ch3_Vimagine= ch3[222500:225000] 

ch3_W = ch3[225000:227500]
ch3_Wrest= ch3[227500:230000] 
ch3_Wimagine= ch3[230000:232500]

ch3_X = ch3[232500:235000]
ch3_Xrest= ch3[235000:237500] 
ch3_Ximagine= ch3[237500:240000]

ch3_Y = ch3[240000:242500]
ch3_Yrest= ch3[242500:245000] 
ch3_Yimagine= ch3[245000:247500]

ch3_Z = ch3[247500:250000]
ch3_Zrest= ch3[250000:252500] 
ch3_Zimagine= ch3[252500:255000]





#Channel_4 EVENTS
ch4_eyeopen = ch4[0:30000]
ch4_eyeclosed = ch4[30000:60000]

ch4_A = ch4[60000:62500]
ch4_Arest= ch4[62500:65000] 
ch4_Aimagine= ch4[65000:67500] 

ch4_B = ch4[67500:70000]
ch4_Brest= ch4[70000:72500] 
ch4_Bimagine= ch4[72500:75000] 

ch4_C = ch4[75000:77500]
ch4_Crest= ch4[77500:80000] 
ch4_Cimagine= ch4[80000:82500]

ch4_D = ch4[82500:85000]
ch4_Drest= ch4[85000:87500] 
ch4_Dimagine= ch4[87500:90000]

ch4_E = ch4[90000:92500]
ch4_Erest= ch4[92500:95000] 
ch4_Eimagine= ch4[95000:97500]

ch4_F = ch4[97500:100000]
ch4_Frest= ch4[100000:102500] 
ch4_Fimagine= ch4[102500:105000] 

ch4_G = ch4[105000:107500]
ch4_Grest= ch4[107500:110000] 
ch4_Gimagine= ch4[110000:112500]

ch4_H = ch4[112500:115000]
ch4_Hrest= ch4[115000:117500] 
ch4_Himagine= ch4[117500:120000]

ch4_I = ch4[120000:122500]
ch4_Irest= ch4[122500:125000] 
ch4_Iimagine= ch4[125000:127500]

ch4_J = ch4[127500:130000]
ch4_Jrest= ch4[130000:132500] 
ch4_Jimagine= ch4[132500:135000] 

ch4_K = ch4[135000:137500]
ch4_Krest= ch4[137500:140000] 
ch4_Kimagine= ch4[140000:142500]

ch4_L = ch4[142500:145000]
ch4_Lrest= ch4[145000:147500] 
ch4_Limagine= ch4[147500:150000]

ch4_M = ch4[150000:152500]
ch4_Mrest= ch4[152500:155000] 
ch4_Mimagine= ch4[155000:157500]

ch4_N = ch4[157500:160000]
ch4_Nrest= ch4[160000:162500] 
ch4_Nimagine= ch4[162500:165000] 

ch4_O = ch4[165000:167500]
ch4_Orest= ch4[167500:170000] 
ch4_Oimagine= ch4[170000:172500]

ch4_P = ch4[172500:175000]
ch4_Prest= ch4[175000:177500] 
ch4_Pimagine= ch4[177500:180000]

ch4_Q = ch4[180000:182500]
ch4_Qrest= ch4[182500:185000] 
ch4_Qimagine= ch4[185000:187500]

ch4_R = ch4[187500:190000]
ch4_Rrest= ch4[190000:192500] 
ch4_Rimagine= ch4[192500:195000] 

ch4_S = ch4[195000:197500]
ch4_Srest= ch4[197500:200000] 
ch4_Simagine= ch4[200000:202500]

ch4_T = ch4[202500:205000]
ch4_Trest= ch4[205000:207500] 
ch4_Timagine= ch4[207500:210000]

ch4_U = ch4[210000:212500]
ch4_Urest= ch4[212500:215000] 
ch4_Uimagine= ch4[215000:217500]

ch4_V = ch4[217500:220000]
ch4_Vrest= ch4[220000:222500] 
ch4_Vimagine= ch4[222500:225000] 

ch4_W = ch4[225000:227500]
ch4_Wrest= ch4[227500:230000] 
ch4_Wimagine= ch4[230000:232500]

ch4_X = ch4[232500:235000]
ch4_Xrest= ch4[235000:237500] 
ch4_Ximagine= ch4[237500:240000]

ch4_Y = ch4[240000:242500]
ch4_Yrest= ch4[242500:245000] 
ch4_Yimagine= ch4[245000:247500]

ch4_Z = ch4[247500:250000]
ch4_Zrest= ch4[250000:252500] 
ch4_Zimagine= ch4[252500:255000]




#Channel_5 EVENTS
ch5_eyeopen = ch5[0:30000]
ch5_eyeclosed = ch5[30000:60000]

ch5_A = ch5[60000:62500]
ch5_Arest= ch5[62500:65000] 
ch5_Aimagine= ch5[65000:67500] 

ch5_B = ch5[67500:70000]
ch5_Brest= ch5[70000:72500] 
ch5_Bimagine= ch5[72500:75000] 

ch5_C = ch5[75000:77500]
ch5_Crest= ch5[77500:80000] 
ch5_Cimagine= ch5[80000:82500]

ch5_D = ch5[82500:85000]
ch5_Drest= ch5[85000:87500] 
ch5_Dimagine= ch5[87500:90000]

ch5_E = ch5[90000:92500]
ch5_Erest= ch5[92500:95000] 
ch5_Eimagine= ch5[95000:97500]

ch5_F = ch5[97500:100000]
ch5_Frest= ch5[100000:102500] 
ch5_Fimagine= ch5[102500:105000] 

ch5_G = ch5[105000:107500]
ch5_Grest= ch5[107500:110000] 
ch5_Gimagine= ch5[110000:112500]

ch5_H = ch5[112500:115000]
ch5_Hrest= ch5[115000:117500] 
ch5_Himagine= ch5[117500:120000]

ch5_I = ch5[120000:122500]
ch5_Irest= ch5[122500:125000] 
ch5_Iimagine= ch5[125000:127500]

ch5_J = ch5[127500:130000]
ch5_Jrest= ch5[130000:132500] 
ch5_Jimagine= ch5[132500:135000] 

ch5_K = ch5[135000:137500]
ch5_Krest= ch5[137500:140000] 
ch5_Kimagine= ch5[140000:142500]

ch5_L = ch5[142500:145000]
ch5_Lrest= ch5[145000:147500] 
ch5_Limagine= ch5[147500:150000]

ch5_M = ch5[150000:152500]
ch5_Mrest= ch5[152500:155000] 
ch5_Mimagine= ch5[155000:157500]

ch5_N = ch5[157500:160000]
ch5_Nrest= ch5[160000:162500] 
ch5_Nimagine= ch5[162500:165000] 

ch5_O = ch5[165000:167500]
ch5_Orest= ch5[167500:170000] 
ch5_Oimagine= ch5[170000:172500]

ch5_P = ch5[172500:175000]
ch5_Prest= ch5[175000:177500] 
ch5_Pimagine= ch5[177500:180000]

ch5_Q = ch5[180000:182500]
ch5_Qrest= ch5[182500:185000] 
ch5_Qimagine= ch5[185000:187500]

ch5_R = ch5[187500:190000]
ch5_Rrest= ch5[190000:192500] 
ch5_Rimagine= ch5[192500:195000] 

ch5_S = ch5[195000:197500]
ch5_Srest= ch5[197500:200000] 
ch5_Simagine= ch5[200000:202500]

ch5_T = ch5[202500:205000]
ch5_Trest= ch5[205000:207500] 
ch5_Timagine= ch5[207500:210000]

ch5_U = ch5[210000:212500]
ch5_Urest= ch5[212500:215000] 
ch5_Uimagine= ch5[215000:217500]

ch5_V = ch5[217500:220000]
ch5_Vrest= ch5[220000:222500] 
ch5_Vimagine= ch5[222500:225000] 

ch5_W = ch5[225000:227500]
ch5_Wrest= ch5[227500:230000] 
ch5_Wimagine= ch5[230000:232500]

ch5_X = ch5[232500:235000]
ch5_Xrest= ch5[235000:237500] 
ch5_Ximagine= ch5[237500:240000]

ch5_Y = ch5[240000:242500]
ch5_Yrest= ch5[242500:245000] 
ch5_Yimagine= ch5[245000:247500]

ch5_Z = ch5[247500:250000]
ch5_Zrest= ch5[250000:252500] 
ch5_Zimagine= ch5[252500:255000]



#Channel_6 EVENTS
ch6_eyeopen = ch6[0:30000]
ch6_eyeclosed = ch6[30000:60000]

ch6_A = ch6[60000:62500]
ch6_Arest= ch6[62500:65000] 
ch6_Aimagine= ch6[65000:67500] 

ch6_B = ch6[67500:70000]
ch6_Brest= ch6[70000:72500] 
ch6_Bimagine= ch6[72500:75000] 

ch6_C = ch6[75000:77500]
ch6_Crest= ch6[77500:80000] 
ch6_Cimagine= ch6[80000:82500]

ch6_D = ch6[82500:85000]
ch6_Drest= ch6[85000:87500] 
ch6_Dimagine= ch6[87500:90000]

ch6_E = ch6[90000:92500]
ch6_Erest= ch6[92500:95000] 
ch6_Eimagine= ch6[95000:97500]

ch6_F = ch6[97500:100000]
ch6_Frest= ch6[100000:102500] 
ch6_Fimagine= ch6[102500:105000] 

ch6_G = ch6[105000:107500]
ch6_Grest= ch6[107500:110000] 
ch6_Gimagine= ch6[110000:112500]

ch6_H = ch6[112500:115000]
ch6_Hrest= ch6[115000:117500] 
ch6_Himagine= ch6[117500:120000]

ch6_I = ch6[120000:122500]
ch6_Irest= ch6[122500:125000] 
ch6_Iimagine= ch6[125000:127500]

ch6_J = ch6[127500:130000]
ch6_Jrest= ch6[130000:132500] 
ch6_Jimagine= ch6[132500:135000] 

ch6_K = ch6[135000:137500]
ch6_Krest= ch6[137500:140000] 
ch6_Kimagine= ch6[140000:142500]

ch6_L = ch6[142500:145000]
ch6_Lrest= ch6[145000:147500] 
ch6_Limagine= ch6[147500:150000]

ch6_M = ch6[150000:152500]
ch6_Mrest= ch6[152500:155000] 
ch6_Mimagine= ch6[155000:157500]

ch6_N = ch6[157500:160000]
ch6_Nrest= ch6[160000:162500] 
ch6_Nimagine= ch6[162500:165000] 

ch6_O = ch6[165000:167500]
ch6_Orest= ch6[167500:170000] 
ch6_Oimagine= ch6[170000:172500]

ch6_P = ch6[172500:175000]
ch6_Prest= ch6[175000:177500] 
ch6_Pimagine= ch6[177500:180000]

ch6_Q = ch6[180000:182500]
ch6_Qrest= ch6[182500:185000] 
ch6_Qimagine= ch6[185000:187500]

ch6_R = ch6[187500:190000]
ch6_Rrest= ch6[190000:192500] 
ch6_Rimagine= ch6[192500:195000] 

ch6_S = ch6[195000:197500]
ch6_Srest= ch6[197500:200000] 
ch6_Simagine= ch6[200000:202500]

ch6_T = ch6[202500:205000]
ch6_Trest= ch6[205000:207500] 
ch6_Timagine= ch6[207500:210000]

ch6_U = ch6[210000:212500]
ch6_Urest= ch6[212500:215000] 
ch6_Uimagine= ch6[215000:217500]

ch6_V = ch6[217500:220000]
ch6_Vrest= ch6[220000:222500] 
ch6_Vimagine= ch6[222500:225000] 

ch6_W = ch6[225000:227500]
ch6_Wrest= ch6[227500:230000] 
ch6_Wimagine= ch6[230000:232500]

ch6_X = ch6[232500:235000]
ch6_Xrest= ch6[235000:237500] 
ch6_Ximagine= ch6[237500:240000]

ch6_Y = ch6[240000:242500]
ch6_Yrest= ch6[242500:245000] 
ch6_Yimagine= ch6[245000:247500]

ch6_Z = ch6[247500:250000]
ch6_Zrest= ch6[250000:252500] 
ch6_Zimagine= ch6[252500:255000]


#Channel_7 EVENTS
ch7_eyeopen = ch7[0:30000]
ch7_eyeclosed = ch7[30000:60000]

ch7_A = ch7[60000:62500]
ch7_Arest= ch7[62500:65000] 
ch7_Aimagine= ch7[65000:67500] 

ch7_B = ch7[67500:70000]
ch7_Brest= ch7[70000:72500] 
ch7_Bimagine= ch7[72500:75000] 

ch7_C = ch7[75000:77500]
ch7_Crest= ch7[77500:80000] 
ch7_Cimagine= ch7[80000:82500]

ch7_D = ch7[82500:85000]
ch7_Drest= ch7[85000:87500] 
ch7_Dimagine= ch7[87500:90000]

ch7_E = ch7[90000:92500]
ch7_Erest= ch7[92500:95000] 
ch7_Eimagine= ch7[95000:97500]

ch7_F = ch7[97500:100000]
ch7_Frest= ch7[100000:102500] 
ch7_Fimagine= ch7[102500:105000] 

ch7_G = ch7[105000:107500]
ch7_Grest= ch7[107500:110000] 
ch7_Gimagine= ch7[110000:112500]

ch7_H = ch7[112500:115000]
ch7_Hrest= ch7[115000:117500] 
ch7_Himagine= ch7[117500:120000]

ch7_I = ch7[120000:122500]
ch7_Irest= ch7[122500:125000] 
ch7_Iimagine= ch7[125000:127500]

ch7_J = ch7[127500:130000]
ch7_Jrest= ch7[130000:132500] 
ch7_Jimagine= ch7[132500:135000] 

ch7_K = ch7[135000:137500]
ch7_Krest= ch7[137500:140000] 
ch7_Kimagine= ch7[140000:142500]

ch7_L = ch7[142500:145000]
ch7_Lrest= ch7[145000:147500] 
ch7_Limagine= ch7[147500:150000]

ch7_M = ch7[150000:152500]
ch7_Mrest= ch7[152500:155000] 
ch7_Mimagine= ch7[155000:157500]

ch7_N = ch7[157500:160000]
ch7_Nrest= ch7[160000:162500] 
ch7_Nimagine= ch7[162500:165000] 

ch7_O = ch7[165000:167500]
ch7_Orest= ch7[167500:170000] 
ch7_Oimagine= ch7[170000:172500]

ch7_P = ch7[172500:175000]
ch7_Prest= ch7[175000:177500] 
ch7_Pimagine= ch7[177500:180000]

ch7_Q = ch7[180000:182500]
ch7_Qrest= ch7[182500:185000] 
ch7_Qimagine= ch7[185000:187500]

ch7_R = ch7[187500:190000]
ch7_Rrest= ch7[190000:192500] 
ch7_Rimagine= ch7[192500:195000] 

ch7_S = ch7[195000:197500]
ch7_Srest= ch7[197500:200000] 
ch7_Simagine= ch7[200000:202500]

ch7_T = ch7[202500:205000]
ch7_Trest= ch7[205000:207500] 
ch7_Timagine= ch7[207500:210000]

ch7_U = ch7[210000:212500]
ch7_Urest= ch7[212500:215000] 
ch7_Uimagine= ch7[215000:217500]

ch7_V = ch7[217500:220000]
ch7_Vrest= ch7[220000:222500] 
ch7_Vimagine= ch7[222500:225000] 

ch7_W = ch7[225000:227500]
ch7_Wrest= ch7[227500:230000] 
ch7_Wimagine= ch7[230000:232500]

ch7_X = ch7[232500:235000]
ch7_Xrest= ch7[235000:237500] 
ch7_Ximagine= ch7[237500:240000]

ch7_Y = ch7[240000:242500]
ch7_Yrest= ch7[242500:245000] 
ch7_Yimagine= ch7[245000:247500]

ch7_Z = ch7[247500:250000]
ch7_Zrest= ch7[250000:252500] 
ch7_Zimagine= ch7[252500:255000]



#Channel_8 EVENTS
ch8_eyeopen = ch8[0:30000]
ch8_eyeclosed = ch8[30000:60000]

ch8_A = ch8[60000:62500]
ch8_Arest= ch8[62500:65000] 
ch8_Aimagine= ch8[65000:67500] 

ch8_B = ch8[67500:70000]
ch8_Brest= ch8[70000:72500] 
ch8_Bimagine= ch8[72500:75000] 

ch8_C = ch8[75000:77500]
ch8_Crest= ch8[77500:80000] 
ch8_Cimagine= ch8[80000:82500]

ch8_D = ch8[82500:85000]
ch8_Drest= ch8[85000:87500] 
ch8_Dimagine= ch8[87500:90000]

ch8_E = ch8[90000:92500]
ch8_Erest= ch8[92500:95000] 
ch8_Eimagine= ch8[95000:97500]

ch8_F = ch8[97500:100000]
ch8_Frest= ch8[100000:102500] 
ch8_Fimagine= ch8[102500:105000] 

ch8_G = ch8[105000:107500]
ch8_Grest= ch8[107500:110000] 
ch8_Gimagine= ch8[110000:112500]

ch8_H = ch8[112500:115000]
ch8_Hrest= ch8[115000:117500] 
ch8_Himagine= ch8[117500:120000]

ch8_I = ch8[120000:122500]
ch8_Irest= ch8[122500:125000] 
ch8_Iimagine= ch8[125000:127500]

ch8_J = ch8[127500:130000]
ch8_Jrest= ch8[130000:132500] 
ch8_Jimagine= ch8[132500:135000] 

ch8_K = ch8[135000:137500]
ch8_Krest= ch8[137500:140000] 
ch8_Kimagine= ch8[140000:142500]

ch8_L = ch8[142500:145000]
ch8_Lrest= ch8[145000:147500] 
ch8_Limagine= ch8[147500:150000]

ch8_M = ch8[150000:152500]
ch8_Mrest= ch8[152500:155000] 
ch8_Mimagine= ch8[155000:157500]

ch8_N = ch8[157500:160000]
ch8_Nrest= ch8[160000:162500] 
ch8_Nimagine= ch8[162500:165000] 

ch8_O = ch8[165000:167500]
ch8_Orest= ch8[167500:170000] 
ch8_Oimagine= ch8[170000:172500]

ch8_P = ch8[172500:175000]
ch8_Prest= ch8[175000:177500] 
ch8_Pimagine= ch8[177500:180000]

ch8_Q = ch8[180000:182500]
ch8_Qrest= ch8[182500:185000] 
ch8_Qimagine= ch8[185000:187500]

ch8_R = ch8[187500:190000]
ch8_Rrest= ch8[190000:192500] 
ch8_Rimagine= ch8[192500:195000] 

ch8_S = ch8[195000:197500]
ch8_Srest= ch8[197500:200000] 
ch8_Simagine= ch8[200000:202500]

ch8_T = ch8[202500:205000]
ch8_Trest= ch8[205000:207500] 
ch8_Timagine= ch8[207500:210000]

ch8_U = ch8[210000:212500]
ch8_Urest= ch8[212500:215000] 
ch8_Uimagine= ch8[215000:217500]

ch8_V = ch8[217500:220000]
ch8_Vrest= ch8[220000:222500] 
ch8_Vimagine= ch8[222500:225000] 

ch8_W = ch8[225000:227500]
ch8_Wrest= ch8[227500:230000] 
ch8_Wimagine= ch8[230000:232500]

ch8_X = ch8[232500:235000]
ch8_Xrest= ch8[235000:237500] 
ch8_Ximagine= ch8[237500:240000]

ch8_Y = ch8[240000:242500]
ch8_Yrest= ch8[242500:245000] 
ch8_Yimagine= ch8[245000:247500]

ch8_Z = ch8[247500:250000]
ch8_Zrest= ch8[250000:252500] 
ch8_Zimagine= ch8[252500:255000]



#Channel_9 EVENTS
ch9_eyeopen = ch9[0:30000]
ch9_eyeclosed = ch9[30000:60000]

ch9_A = ch9[60000:62500]
ch9_Arest= ch9[62500:65000] 
ch9_Aimagine= ch9[65000:67500] 

ch9_B = ch9[67500:70000]
ch9_Brest= ch9[70000:72500] 
ch9_Bimagine= ch9[72500:75000] 

ch9_C = ch9[75000:77500]
ch9_Crest= ch9[77500:80000] 
ch9_Cimagine= ch9[80000:82500]

ch9_D = ch9[82500:85000]
ch9_Drest= ch9[85000:87500] 
ch9_Dimagine= ch9[87500:90000]

ch9_E = ch9[90000:92500]
ch9_Erest= ch9[92500:95000] 
ch9_Eimagine= ch9[95000:97500]

ch9_F = ch9[97500:100000]
ch9_Frest= ch9[100000:102500] 
ch9_Fimagine= ch9[102500:105000] 

ch9_G = ch9[105000:107500]
ch9_Grest= ch9[107500:110000] 
ch9_Gimagine= ch9[110000:112500]

ch9_H = ch9[112500:115000]
ch9_Hrest= ch9[115000:117500] 
ch9_Himagine= ch9[117500:120000]

ch9_I = ch9[120000:122500]
ch9_Irest= ch9[122500:125000] 
ch9_Iimagine= ch9[125000:127500]

ch9_J = ch9[127500:130000]
ch9_Jrest= ch9[130000:132500] 
ch9_Jimagine= ch9[132500:135000] 

ch9_K = ch9[135000:137500]
ch9_Krest= ch9[137500:140000] 
ch9_Kimagine= ch9[140000:142500]

ch9_L = ch9[142500:145000]
ch9_Lrest= ch9[145000:147500] 
ch9_Limagine= ch9[147500:150000]

ch9_M = ch9[150000:152500]
ch9_Mrest= ch9[152500:155000] 
ch9_Mimagine= ch9[155000:157500]

ch9_N = ch9[157500:160000]
ch9_Nrest= ch9[160000:162500] 
ch9_Nimagine= ch9[162500:165000] 

ch9_O = ch9[165000:167500]
ch9_Orest= ch9[167500:170000] 
ch9_Oimagine= ch9[170000:172500]

ch9_P = ch9[172500:175000]
ch9_Prest= ch9[175000:177500] 
ch9_Pimagine= ch9[177500:180000]

ch9_Q = ch9[180000:182500]
ch9_Qrest= ch9[182500:185000] 
ch9_Qimagine= ch9[185000:187500]

ch9_R = ch9[187500:190000]
ch9_Rrest= ch9[190000:192500] 
ch9_Rimagine= ch9[192500:195000] 

ch9_S = ch9[195000:197500]
ch9_Srest= ch9[197500:200000] 
ch9_Simagine= ch9[200000:202500]

ch9_T = ch9[202500:205000]
ch9_Trest= ch9[205000:207500] 
ch9_Timagine= ch9[207500:210000]

ch9_U = ch9[210000:212500]
ch9_Urest= ch9[212500:215000] 
ch9_Uimagine= ch9[215000:217500]

ch9_V = ch9[217500:220000]
ch9_Vrest= ch9[220000:222500] 
ch9_Vimagine= ch9[222500:225000] 

ch9_W = ch9[225000:227500]
ch9_Wrest= ch9[227500:230000] 
ch9_Wimagine= ch9[230000:232500]

ch9_X = ch9[232500:235000]
ch9_Xrest= ch9[235000:237500] 
ch9_Ximagine= ch9[237500:240000]

ch9_Y = ch9[240000:242500]
ch9_Yrest= ch9[242500:245000] 
ch9_Yimagine= ch9[245000:247500]

ch9_Z = ch9[247500:250000]
ch9_Zrest= ch9[250000:252500] 
ch9_Zimagine= ch9[252500:255000]



#Channel_10 EVENTS
ch10_eyeopen = ch10[0:30000]
ch10_eyeclosed = ch10[30000:60000]

ch10_A = ch10[60000:62500]
ch10_Arest= ch10[62500:65000] 
ch10_Aimagine= ch10[65000:67500] 

ch10_B = ch10[67500:70000]
ch10_Brest= ch10[70000:72500] 
ch10_Bimagine= ch10[72500:75000] 

ch10_C = ch10[75000:77500]
ch10_Crest= ch10[77500:80000] 
ch10_Cimagine= ch10[80000:82500]

ch10_D = ch10[82500:85000]
ch10_Drest= ch10[85000:87500] 
ch10_Dimagine= ch10[87500:90000]

ch10_E = ch10[90000:92500]
ch10_Erest= ch10[92500:95000] 
ch10_Eimagine= ch10[95000:97500]

ch10_F = ch10[97500:100000]
ch10_Frest= ch10[100000:102500] 
ch10_Fimagine= ch10[102500:105000] 

ch10_G = ch10[105000:107500]
ch10_Grest= ch10[107500:110000] 
ch10_Gimagine= ch10[110000:112500]

ch10_H = ch10[112500:115000]
ch10_Hrest= ch10[115000:117500] 
ch10_Himagine= ch10[117500:120000]

ch10_I = ch10[120000:122500]
ch10_Irest= ch10[122500:125000] 
ch10_Iimagine= ch10[125000:127500]

ch10_J = ch10[127500:130000]
ch10_Jrest= ch10[130000:132500] 
ch10_Jimagine= ch10[132500:135000] 

ch10_K = ch10[135000:137500]
ch10_Krest= ch10[137500:140000] 
ch10_Kimagine= ch10[140000:142500]

ch10_L = ch10[142500:145000]
ch10_Lrest= ch10[145000:147500] 
ch10_Limagine= ch10[147500:150000]

ch10_M = ch10[150000:152500]
ch10_Mrest= ch10[152500:155000] 
ch10_Mimagine= ch10[155000:157500]

ch10_N = ch10[157500:160000]
ch10_Nrest= ch10[160000:162500] 
ch10_Nimagine= ch10[162500:165000] 

ch10_O = ch10[165000:167500]
ch10_Orest= ch10[167500:170000] 
ch10_Oimagine= ch10[170000:172500]

ch10_P = ch10[172500:175000]
ch10_Prest= ch10[175000:177500] 
ch10_Pimagine= ch10[177500:180000]

ch10_Q = ch10[180000:182500]
ch10_Qrest= ch10[182500:185000] 
ch10_Qimagine= ch10[185000:187500]

ch10_R = ch10[187500:190000]
ch10_Rrest= ch10[190000:192500] 
ch10_Rimagine= ch10[192500:195000] 

ch10_S = ch10[195000:197500]
ch10_Srest= ch10[197500:200000] 
ch10_Simagine= ch10[200000:202500]

ch10_T = ch10[202500:205000]
ch10_Trest= ch10[205000:207500] 
ch10_Timagine= ch10[207500:210000]

ch10_U = ch10[210000:212500]
ch10_Urest= ch10[212500:215000] 
ch10_Uimagine= ch10[215000:217500]

ch10_V = ch10[217500:220000]
ch10_Vrest= ch10[220000:222500] 
ch10_Vimagine= ch10[222500:225000] 

ch10_W = ch10[225000:227500]
ch10_Wrest= ch10[227500:230000] 
ch10_Wimagine= ch10[230000:232500]

ch10_X = ch10[232500:235000]
ch10_Xrest= ch10[235000:237500] 
ch10_Ximagine= ch10[237500:240000]

ch10_Y = ch10[240000:242500]
ch10_Yrest= ch10[242500:245000] 
ch10_Yimagine= ch10[245000:247500]

ch10_Z = ch10[247500:250000]
ch10_Zrest= ch10[250000:252500] 
ch10_Zimagine= ch10[252500:255000]



#Channel_11 EVENTS
ch11_eyeopen = ch11[0:30000]
ch11_eyeclosed = ch11[30000:60000]

ch11_A = ch11[60000:62500]
ch11_Arest= ch11[62500:65000] 
ch11_Aimagine= ch11[65000:67500] 

ch11_B = ch11[67500:70000]
ch11_Brest= ch11[70000:72500] 
ch11_Bimagine= ch11[72500:75000] 

ch11_C = ch11[75000:77500]
ch11_Crest= ch11[77500:80000] 
ch11_Cimagine= ch11[80000:82500]

ch11_D = ch11[82500:85000]
ch11_Drest= ch11[85000:87500] 
ch11_Dimagine= ch11[87500:90000]

ch11_E = ch11[90000:92500]
ch11_Erest= ch11[92500:95000] 
ch11_Eimagine= ch11[95000:97500]

ch11_F = ch11[97500:100000]
ch11_Frest= ch11[100000:102500] 
ch11_Fimagine= ch11[102500:105000] 

ch11_G = ch11[105000:107500]
ch11_Grest= ch11[107500:110000] 
ch11_Gimagine= ch11[110000:112500]

ch11_H = ch11[112500:115000]
ch11_Hrest= ch11[115000:117500] 
ch11_Himagine= ch11[117500:120000]

ch11_I = ch11[120000:122500]
ch11_Irest= ch11[122500:125000] 
ch11_Iimagine= ch11[125000:127500]

ch11_J = ch11[127500:130000]
ch11_Jrest= ch11[130000:132500] 
ch11_Jimagine= ch11[132500:135000] 

ch11_K = ch11[135000:137500]
ch11_Krest= ch11[137500:140000] 
ch11_Kimagine= ch11[140000:142500]

ch11_L = ch11[142500:145000]
ch11_Lrest= ch11[145000:147500] 
ch11_Limagine= ch11[147500:150000]

ch11_M = ch11[150000:152500]
ch11_Mrest= ch11[152500:155000] 
ch11_Mimagine= ch11[155000:157500]

ch11_N = ch11[157500:160000]
ch11_Nrest= ch11[160000:162500] 
ch11_Nimagine= ch11[162500:165000] 

ch11_O = ch11[165000:167500]
ch11_Orest= ch11[167500:170000] 
ch11_Oimagine= ch11[170000:172500]

ch11_P = ch11[172500:175000]
ch11_Prest= ch11[175000:177500] 
ch11_Pimagine= ch11[177500:180000]

ch11_Q = ch11[180000:182500]
ch11_Qrest= ch11[182500:185000] 
ch11_Qimagine= ch11[185000:187500]

ch11_R = ch11[187500:190000]
ch11_Rrest= ch11[190000:192500] 
ch11_Rimagine= ch11[192500:195000] 

ch11_S = ch11[195000:197500]
ch11_Srest= ch11[197500:200000] 
ch11_Simagine= ch11[200000:202500]

ch11_T = ch11[202500:205000]
ch11_Trest= ch11[205000:207500] 
ch11_Timagine= ch11[207500:210000]

ch11_U = ch11[210000:212500]
ch11_Urest= ch11[212500:215000] 
ch11_Uimagine= ch11[215000:217500]

ch11_V = ch11[217500:220000]
ch11_Vrest= ch11[220000:222500] 
ch11_Vimagine= ch11[222500:225000] 

ch11_W = ch11[225000:227500]
ch11_Wrest= ch11[227500:230000] 
ch11_Wimagine= ch11[230000:232500]

ch11_X = ch11[232500:235000]
ch11_Xrest= ch11[235000:237500] 
ch11_Ximagine= ch11[237500:240000]

ch11_Y = ch11[240000:242500]
ch11_Yrest= ch11[242500:245000] 
ch11_Yimagine= ch11[245000:247500]

ch11_Z = ch11[247500:250000]
ch11_Zrest= ch11[250000:252500] 
ch11_Zimagine= ch11[252500:255000]



#Channel_12 EVENTS
ch12_eyeopen = ch12[0:30000]
ch12_eyeclosed = ch12[30000:60000]

ch12_A = ch12[60000:62500]
ch12_Arest= ch12[62500:65000] 
ch12_Aimagine= ch12[65000:67500] 

ch12_B = ch12[67500:70000]
ch12_Brest= ch12[70000:72500] 
ch12_Bimagine= ch12[72500:75000] 

ch12_C = ch12[75000:77500]
ch12_Crest= ch12[77500:80000] 
ch12_Cimagine= ch12[80000:82500]

ch12_D = ch12[82500:85000]
ch12_Drest= ch12[85000:87500] 
ch12_Dimagine= ch12[87500:90000]

ch12_E = ch12[90000:92500]
ch12_Erest= ch12[92500:95000] 
ch12_Eimagine= ch12[95000:97500]

ch12_F = ch12[97500:100000]
ch12_Frest= ch12[100000:102500] 
ch12_Fimagine= ch12[102500:105000] 

ch12_G = ch12[105000:107500]
ch12_Grest= ch12[107500:110000] 
ch12_Gimagine= ch12[110000:112500]

ch12_H = ch12[112500:115000]
ch12_Hrest= ch12[115000:117500] 
ch12_Himagine= ch12[117500:120000]

ch12_I = ch12[120000:122500]
ch12_Irest= ch12[122500:125000] 
ch12_Iimagine= ch12[125000:127500]

ch12_J = ch12[127500:130000]
ch12_Jrest= ch12[130000:132500] 
ch12_Jimagine= ch12[132500:135000] 

ch12_K = ch12[135000:137500]
ch12_Krest= ch12[137500:140000] 
ch12_Kimagine= ch12[140000:142500]

ch12_L = ch12[142500:145000]
ch12_Lrest= ch12[145000:147500] 
ch12_Limagine= ch12[147500:150000]

ch12_M = ch12[150000:152500]
ch12_Mrest= ch12[152500:155000] 
ch12_Mimagine= ch12[155000:157500]

ch12_N = ch12[157500:160000]
ch12_Nrest= ch12[160000:162500] 
ch12_Nimagine= ch12[162500:165000] 

ch12_O = ch12[165000:167500]
ch12_Orest= ch12[167500:170000] 
ch12_Oimagine= ch12[170000:172500]

ch12_P = ch12[172500:175000]
ch12_Prest= ch12[175000:177500] 
ch12_Pimagine= ch12[177500:180000]

ch12_Q = ch12[180000:182500]
ch12_Qrest= ch12[182500:185000] 
ch12_Qimagine= ch12[185000:187500]

ch12_R = ch12[187500:190000]
ch12_Rrest= ch12[190000:192500] 
ch12_Rimagine= ch12[192500:195000] 

ch12_S = ch12[195000:197500]
ch12_Srest= ch12[197500:200000] 
ch12_Simagine= ch12[200000:202500]

ch12_T = ch12[202500:205000]
ch12_Trest= ch12[205000:207500] 
ch12_Timagine= ch12[207500:210000]

ch12_U = ch12[210000:212500]
ch12_Urest= ch12[212500:215000] 
ch12_Uimagine= ch12[215000:217500]

ch12_V = ch12[217500:220000]
ch12_Vrest= ch12[220000:222500] 
ch12_Vimagine= ch12[222500:225000] 

ch12_W = ch12[225000:227500]
ch12_Wrest= ch12[227500:230000] 
ch12_Wimagine= ch12[230000:232500]

ch12_X = ch12[232500:235000]
ch12_Xrest= ch12[235000:237500] 
ch12_Ximagine= ch12[237500:240000]

ch12_Y = ch12[240000:242500]
ch12_Yrest= ch12[242500:245000] 
ch12_Yimagine= ch12[245000:247500]

ch12_Z = ch12[247500:250000]
ch12_Zrest= ch12[250000:252500] 
ch12_Zimagine= ch12[252500:255000]



#Channel_13 EVENTS
ch13_eyeopen = ch13[0:30000]
ch13_eyeclosed = ch13[30000:60000]

ch13_A = ch13[60000:62500]
ch13_Arest= ch13[62500:65000] 
ch13_Aimagine= ch13[65000:67500] 

ch13_B = ch13[67500:70000]
ch13_Brest= ch13[70000:72500] 
ch13_Bimagine= ch13[72500:75000] 

ch13_C = ch13[75000:77500]
ch13_Crest= ch13[77500:80000] 
ch13_Cimagine= ch13[80000:82500]

ch13_D = ch13[82500:85000]
ch13_Drest= ch13[85000:87500] 
ch13_Dimagine= ch13[87500:90000]

ch13_E = ch13[90000:92500]
ch13_Erest= ch13[92500:95000] 
ch13_Eimagine= ch13[95000:97500]

ch13_F = ch13[97500:100000]
ch13_Frest= ch13[100000:102500] 
ch13_Fimagine= ch13[102500:105000] 

ch13_G = ch13[105000:107500]
ch13_Grest= ch13[107500:110000] 
ch13_Gimagine= ch13[110000:112500]

ch13_H = ch13[112500:115000]
ch13_Hrest= ch13[115000:117500] 
ch13_Himagine= ch13[117500:120000]

ch13_I = ch13[120000:122500]
ch13_Irest= ch13[122500:125000] 
ch13_Iimagine= ch13[125000:127500]

ch13_J = ch13[127500:130000]
ch13_Jrest= ch13[130000:132500] 
ch13_Jimagine= ch13[132500:135000] 

ch13_K = ch13[135000:137500]
ch13_Krest= ch13[137500:140000] 
ch13_Kimagine= ch13[140000:142500]

ch13_L = ch13[142500:145000]
ch13_Lrest= ch13[145000:147500] 
ch13_Limagine= ch13[147500:150000]

ch13_M = ch13[150000:152500]
ch13_Mrest= ch13[152500:155000] 
ch13_Mimagine= ch13[155000:157500]

ch13_N = ch13[157500:160000]
ch13_Nrest= ch13[160000:162500] 
ch13_Nimagine= ch13[162500:165000] 

ch13_O = ch13[165000:167500]
ch13_Orest= ch13[167500:170000] 
ch13_Oimagine= ch13[170000:172500]

ch13_P = ch13[172500:175000]
ch13_Prest= ch13[175000:177500] 
ch13_Pimagine= ch13[177500:180000]

ch13_Q = ch13[180000:182500]
ch13_Qrest= ch13[182500:185000] 
ch13_Qimagine= ch13[185000:187500]

ch13_R = ch13[187500:190000]
ch13_Rrest= ch13[190000:192500] 
ch13_Rimagine= ch13[192500:195000] 

ch13_S = ch13[195000:197500]
ch13_Srest= ch13[197500:200000] 
ch13_Simagine= ch13[200000:202500]

ch13_T = ch13[202500:205000]
ch13_Trest= ch13[205000:207500] 
ch13_Timagine= ch13[207500:210000]

ch13_U = ch13[210000:212500]
ch13_Urest= ch13[212500:215000] 
ch13_Uimagine= ch13[215000:217500]

ch13_V = ch13[217500:220000]
ch13_Vrest= ch13[220000:222500] 
ch13_Vimagine= ch13[222500:225000] 

ch13_W = ch13[225000:227500]
ch13_Wrest= ch13[227500:230000] 
ch13_Wimagine= ch13[230000:232500]

ch13_X = ch13[232500:235000]
ch13_Xrest= ch13[235000:237500] 
ch13_Ximagine= ch13[237500:240000]

ch13_Y = ch13[240000:242500]
ch13_Yrest= ch13[242500:245000] 
ch13_Yimagine= ch13[245000:247500]

ch13_Z = ch13[247500:250000]
ch13_Zrest= ch13[250000:252500] 
ch13_Zimagine= ch13[252500:255000]


#Channel_14 EVENTS
ch14_eyeopen = ch14[0:30000]
ch14_eyeclosed = ch14[30000:60000]

ch14_A = ch14[60000:62500]
ch14_Arest= ch14[62500:65000] 
ch14_Aimagine= ch14[65000:67500] 

ch14_B = ch14[67500:70000]
ch14_Brest= ch14[70000:72500] 
ch14_Bimagine= ch14[72500:75000] 

ch14_C = ch14[75000:77500]
ch14_Crest= ch14[77500:80000] 
ch14_Cimagine= ch14[80000:82500]

ch14_D = ch14[82500:85000]
ch14_Drest= ch14[85000:87500] 
ch14_Dimagine= ch14[87500:90000]

ch14_E = ch14[90000:92500]
ch14_Erest= ch14[92500:95000] 
ch14_Eimagine= ch14[95000:97500]

ch14_F = ch14[97500:100000]
ch14_Frest= ch14[100000:102500] 
ch14_Fimagine= ch14[102500:105000] 

ch14_G = ch14[105000:107500]
ch14_Grest= ch14[107500:110000] 
ch14_Gimagine= ch14[110000:112500]

ch14_H = ch14[112500:115000]
ch14_Hrest= ch14[115000:117500] 
ch14_Himagine= ch14[117500:120000]

ch14_I = ch14[120000:122500]
ch14_Irest= ch14[122500:125000] 
ch14_Iimagine= ch14[125000:127500]

ch14_J = ch14[127500:130000]
ch14_Jrest= ch14[130000:132500] 
ch14_Jimagine= ch14[132500:135000] 

ch14_K = ch14[135000:137500]
ch14_Krest= ch14[137500:140000] 
ch14_Kimagine= ch14[140000:142500]

ch14_L = ch14[142500:145000]
ch14_Lrest= ch14[145000:147500] 
ch14_Limagine= ch14[147500:150000]

ch14_M = ch14[150000:152500]
ch14_Mrest= ch14[152500:155000] 
ch14_Mimagine= ch14[155000:157500]

ch14_N = ch14[157500:160000]
ch14_Nrest= ch14[160000:162500] 
ch14_Nimagine= ch14[162500:165000] 

ch14_O = ch14[165000:167500]
ch14_Orest= ch14[167500:170000] 
ch14_Oimagine= ch14[170000:172500]

ch14_P = ch14[172500:175000]
ch14_Prest= ch14[175000:177500] 
ch14_Pimagine= ch14[177500:180000]

ch14_Q = ch14[180000:182500]
ch14_Qrest= ch14[182500:185000] 
ch14_Qimagine= ch14[185000:187500]

ch14_R = ch14[187500:190000]
ch14_Rrest= ch14[190000:192500] 
ch14_Rimagine= ch14[192500:195000] 

ch14_S = ch14[195000:197500]
ch14_Srest= ch14[197500:200000] 
ch14_Simagine= ch14[200000:202500]

ch14_T = ch14[202500:205000]
ch14_Trest= ch14[205000:207500] 
ch14_Timagine= ch14[207500:210000]

ch14_U = ch14[210000:212500]
ch14_Urest= ch14[212500:215000] 
ch14_Uimagine= ch14[215000:217500]

ch14_V = ch14[217500:220000]
ch14_Vrest= ch14[220000:222500] 
ch14_Vimagine= ch14[222500:225000] 

ch14_W = ch14[225000:227500]
ch14_Wrest= ch14[227500:230000] 
ch14_Wimagine= ch14[230000:232500]

ch14_X = ch14[232500:235000]
ch14_Xrest= ch14[235000:237500] 
ch14_Ximagine= ch14[237500:240000]

ch14_Y = ch14[240000:242500]
ch14_Yrest= ch14[242500:245000] 
ch14_Yimagine= ch14[245000:247500]

ch14_Z = ch14[247500:250000]
ch14_Zrest= ch14[250000:252500] 
ch14_Zimagine= ch14[252500:255000]



#Channel_15 EVENTS
ch15_eyeopen = ch15[0:30000]
ch15_eyeclosed = ch15[30000:60000]

ch15_A = ch15[60000:62500]
ch15_Arest= ch15[62500:65000] 
ch15_Aimagine= ch15[65000:67500] 

ch15_B = ch15[67500:70000]
ch15_Brest= ch15[70000:72500] 
ch15_Bimagine= ch15[72500:75000] 

ch15_C = ch15[75000:77500]
ch15_Crest= ch15[77500:80000] 
ch15_Cimagine= ch15[80000:82500]

ch15_D = ch15[82500:85000]
ch15_Drest= ch15[85000:87500] 
ch15_Dimagine= ch15[87500:90000]

ch15_E = ch15[90000:92500]
ch15_Erest= ch15[92500:95000] 
ch15_Eimagine= ch15[95000:97500]

ch15_F = ch15[97500:100000]
ch15_Frest= ch15[100000:102500] 
ch15_Fimagine= ch15[102500:105000] 

ch15_G = ch15[105000:107500]
ch15_Grest= ch15[107500:110000] 
ch15_Gimagine= ch15[110000:112500]

ch15_H = ch15[112500:115000]
ch15_Hrest= ch15[115000:117500] 
ch15_Himagine= ch15[117500:120000]

ch15_I = ch15[120000:122500]
ch15_Irest= ch15[122500:125000] 
ch15_Iimagine= ch15[125000:127500]

ch15_J = ch15[127500:130000]
ch15_Jrest= ch15[130000:132500] 
ch15_Jimagine= ch15[132500:135000] 

ch15_K = ch15[135000:137500]
ch15_Krest= ch15[137500:140000] 
ch15_Kimagine= ch15[140000:142500]

ch15_L = ch15[142500:145000]
ch15_Lrest= ch15[145000:147500] 
ch15_Limagine= ch15[147500:150000]

ch15_M = ch15[150000:152500]
ch15_Mrest= ch15[152500:155000] 
ch15_Mimagine= ch15[155000:157500]

ch15_N = ch15[157500:160000]
ch15_Nrest= ch15[160000:162500] 
ch15_Nimagine= ch15[162500:165000] 

ch15_O = ch15[165000:167500]
ch15_Orest= ch15[167500:170000] 
ch15_Oimagine= ch15[170000:172500]

ch15_P = ch15[172500:175000]
ch15_Prest= ch15[175000:177500] 
ch15_Pimagine= ch15[177500:180000]

ch15_Q = ch15[180000:182500]
ch15_Qrest= ch15[182500:185000] 
ch15_Qimagine= ch15[185000:187500]

ch15_R = ch15[187500:190000]
ch15_Rrest= ch15[190000:192500] 
ch15_Rimagine= ch15[192500:195000] 

ch15_S = ch15[195000:197500]
ch15_Srest= ch15[197500:200000] 
ch15_Simagine= ch15[200000:202500]

ch15_T = ch15[202500:205000]
ch15_Trest= ch15[205000:207500] 
ch15_Timagine= ch15[207500:210000]

ch15_U = ch15[210000:212500]
ch15_Urest= ch15[212500:215000] 
ch15_Uimagine= ch15[215000:217500]

ch15_V = ch15[217500:220000]
ch15_Vrest= ch15[220000:222500] 
ch15_Vimagine= ch15[222500:225000] 

ch15_W = ch15[225000:227500]
ch15_Wrest= ch15[227500:230000] 
ch15_Wimagine= ch15[230000:232500]

ch15_X = ch15[232500:235000]
ch15_Xrest= ch15[235000:237500] 
ch15_Ximagine= ch15[237500:240000]

ch15_Y = ch15[240000:242500]
ch15_Yrest= ch15[242500:245000] 
ch15_Yimagine= ch15[245000:247500]

ch15_Z = ch15[247500:250000]
ch15_Zrest= ch15[250000:252500] 
ch15_Zimagine= ch15[252500:255000]



#Channel_16 EVENTS
ch16_eyeopen = ch16[0:30000]
ch16_eyeclosed = ch16[30000:60000]

ch16_A = ch16[60000:62500]
ch16_Arest= ch16[62500:65000] 
ch16_Aimagine= ch16[65000:67500] 

ch16_B = ch16[67500:70000]
ch16_Brest= ch16[70000:72500] 
ch16_Bimagine= ch16[72500:75000] 

ch16_C = ch16[75000:77500]
ch16_Crest= ch16[77500:80000] 
ch16_Cimagine= ch16[80000:82500]

ch16_D = ch16[82500:85000]
ch16_Drest= ch16[85000:87500] 
ch16_Dimagine= ch16[87500:90000]

ch16_E = ch16[90000:92500]
ch16_Erest= ch16[92500:95000] 
ch16_Eimagine= ch16[95000:97500]

ch16_F = ch16[97500:100000]
ch16_Frest= ch16[100000:102500] 
ch16_Fimagine= ch16[102500:105000] 

ch16_G = ch16[105000:107500]
ch16_Grest= ch16[107500:110000] 
ch16_Gimagine= ch16[110000:112500]

ch16_H = ch16[112500:115000]
ch16_Hrest= ch16[115000:117500] 
ch16_Himagine= ch16[117500:120000]

ch16_I = ch16[120000:122500]
ch16_Irest= ch16[122500:125000] 
ch16_Iimagine= ch16[125000:127500]

ch16_J = ch16[127500:130000]
ch16_Jrest= ch16[130000:132500] 
ch16_Jimagine= ch16[132500:135000] 

ch16_K = ch16[135000:137500]
ch16_Krest= ch16[137500:140000] 
ch16_Kimagine= ch16[140000:142500]

ch16_L = ch16[142500:145000]
ch16_Lrest= ch16[145000:147500] 
ch16_Limagine= ch16[147500:150000]

ch16_M = ch16[150000:152500]
ch16_Mrest= ch16[152500:155000] 
ch16_Mimagine= ch16[155000:157500]

ch16_N = ch16[157500:160000]
ch16_Nrest= ch16[160000:162500] 
ch16_Nimagine= ch16[162500:165000] 

ch16_O = ch16[165000:167500]
ch16_Orest= ch16[167500:170000] 
ch16_Oimagine= ch16[170000:172500]

ch16_P = ch16[172500:175000]
ch16_Prest= ch16[175000:177500] 
ch16_Pimagine= ch16[177500:180000]

ch16_Q = ch16[180000:182500]
ch16_Qrest= ch16[182500:185000] 
ch16_Qimagine= ch16[185000:187500]

ch16_R = ch16[187500:190000]
ch16_Rrest= ch16[190000:192500] 
ch16_Rimagine= ch16[192500:195000] 

ch16_S = ch16[195000:197500]
ch16_Srest= ch16[197500:200000] 
ch16_Simagine= ch16[200000:202500]

ch16_T = ch16[202500:205000]
ch16_Trest= ch16[205000:207500] 
ch16_Timagine= ch16[207500:210000]

ch16_U = ch16[210000:212500]
ch16_Urest= ch16[212500:215000] 
ch16_Uimagine= ch16[215000:217500]

ch16_V = ch16[217500:220000]
ch16_Vrest= ch16[220000:222500] 
ch16_Vimagine= ch16[222500:225000] 

ch16_W = ch16[225000:227500]
ch16_Wrest= ch16[227500:230000] 
ch16_Wimagine= ch16[230000:232500]

ch16_X = ch16[232500:235000]
ch16_Xrest= ch16[235000:237500] 
ch16_Ximagine= ch16[237500:240000]

ch16_Y = ch16[240000:242500]
ch16_Yrest= ch16[242500:245000] 
ch16_Yimagine= ch16[245000:247500]

ch16_Z = ch16[247500:250000]
ch16_Zrest= ch16[250000:252500] 
ch16_Zimagine= ch16[252500:255000]


#Channel_17 EVENTS
ch17_eyeopen = ch17[0:30000]
ch17_eyeclosed = ch17[30000:60000]

ch17_A = ch17[60000:62500]
ch17_Arest= ch17[62500:65000] 
ch17_Aimagine= ch17[65000:67500] 

ch17_B = ch17[67500:70000]
ch17_Brest= ch17[70000:72500] 
ch17_Bimagine= ch17[72500:75000] 

ch17_C = ch17[75000:77500]
ch17_Crest= ch17[77500:80000] 
ch17_Cimagine= ch17[80000:82500]

ch17_D = ch17[82500:85000]
ch17_Drest= ch17[85000:87500] 
ch17_Dimagine= ch17[87500:90000]

ch17_E = ch17[90000:92500]
ch17_Erest= ch17[92500:95000] 
ch17_Eimagine= ch17[95000:97500]

ch17_F = ch17[97500:100000]
ch17_Frest= ch17[100000:102500] 
ch17_Fimagine= ch17[102500:105000] 

ch17_G = ch17[105000:107500]
ch17_Grest= ch17[107500:110000] 
ch17_Gimagine= ch17[110000:112500]

ch17_H = ch17[112500:115000]
ch17_Hrest= ch17[115000:117500] 
ch17_Himagine= ch17[117500:120000]

ch17_I = ch17[120000:122500]
ch17_Irest= ch17[122500:125000] 
ch17_Iimagine= ch17[125000:127500]

ch17_J = ch17[127500:130000]
ch17_Jrest= ch17[130000:132500] 
ch17_Jimagine= ch17[132500:135000] 

ch17_K = ch17[135000:137500]
ch17_Krest= ch17[137500:140000] 
ch17_Kimagine= ch17[140000:142500]

ch17_L = ch17[142500:145000]
ch17_Lrest= ch17[145000:147500] 
ch17_Limagine= ch17[147500:150000]

ch17_M = ch17[150000:152500]
ch17_Mrest= ch17[152500:155000] 
ch17_Mimagine= ch17[155000:157500]

ch17_N = ch17[157500:160000]
ch17_Nrest= ch17[160000:162500] 
ch17_Nimagine= ch17[162500:165000] 

ch17_O = ch17[165000:167500]
ch17_Orest= ch17[167500:170000] 
ch17_Oimagine= ch17[170000:172500]

ch17_P = ch17[172500:175000]
ch17_Prest= ch17[175000:177500] 
ch17_Pimagine= ch17[177500:180000]

ch17_Q = ch17[180000:182500]
ch17_Qrest= ch17[182500:185000] 
ch17_Qimagine= ch17[185000:187500]

ch17_R = ch17[187500:190000]
ch17_Rrest= ch17[190000:192500] 
ch17_Rimagine= ch17[192500:195000] 

ch17_S = ch17[195000:197500]
ch17_Srest= ch17[197500:200000] 
ch17_Simagine= ch17[200000:202500]

ch17_T = ch17[202500:205000]
ch17_Trest= ch17[205000:207500] 
ch17_Timagine= ch17[207500:210000]

ch17_U = ch17[210000:212500]
ch17_Urest= ch17[212500:215000] 
ch17_Uimagine= ch17[215000:217500]

ch17_V = ch17[217500:220000]
ch17_Vrest= ch17[220000:222500] 
ch17_Vimagine= ch17[222500:225000] 

ch17_W = ch17[225000:227500]
ch17_Wrest= ch17[227500:230000] 
ch17_Wimagine= ch17[230000:232500]

ch17_X = ch17[232500:235000]
ch17_Xrest= ch17[235000:237500] 
ch17_Ximagine= ch17[237500:240000]

ch17_Y = ch17[240000:242500]
ch17_Yrest= ch17[242500:245000] 
ch17_Yimagine= ch17[245000:247500]

ch17_Z = ch17[247500:250000]
ch17_Zrest= ch17[250000:252500] 
ch17_Zimagine= ch17[252500:255000]



#Channel_18 EVENTS
ch18_eyeopen = ch18[0:30000]
ch18_eyeclosed = ch18[30000:60000]

ch18_A = ch18[60000:62500]
ch18_Arest= ch18[62500:65000] 
ch18_Aimagine= ch18[65000:67500] 

ch18_B = ch18[67500:70000]
ch18_Brest= ch18[70000:72500] 
ch18_Bimagine= ch18[72500:75000] 

ch18_C = ch18[75000:77500]
ch18_Crest= ch18[77500:80000] 
ch18_Cimagine= ch18[80000:82500]

ch18_D = ch18[82500:85000]
ch18_Drest= ch18[85000:87500] 
ch18_Dimagine= ch18[87500:90000]

ch18_E = ch18[90000:92500]
ch18_Erest= ch18[92500:95000] 
ch18_Eimagine= ch18[95000:97500]

ch18_F = ch18[97500:100000]
ch18_Frest= ch18[100000:102500] 
ch18_Fimagine= ch18[102500:105000] 

ch18_G = ch18[105000:107500]
ch18_Grest= ch18[107500:110000] 
ch18_Gimagine= ch18[110000:112500]

ch18_H = ch18[112500:115000]
ch18_Hrest= ch18[115000:117500] 
ch18_Himagine= ch18[117500:120000]

ch18_I = ch18[120000:122500]
ch18_Irest= ch18[122500:125000] 
ch18_Iimagine= ch18[125000:127500]

ch18_J = ch18[127500:130000]
ch18_Jrest= ch18[130000:132500] 
ch18_Jimagine= ch18[132500:135000] 

ch18_K = ch18[135000:137500]
ch18_Krest= ch18[137500:140000] 
ch18_Kimagine= ch18[140000:142500]

ch18_L = ch18[142500:145000]
ch18_Lrest= ch18[145000:147500] 
ch18_Limagine= ch18[147500:150000]

ch18_M = ch18[150000:152500]
ch18_Mrest= ch18[152500:155000] 
ch18_Mimagine= ch18[155000:157500]

ch18_N = ch18[157500:160000]
ch18_Nrest= ch18[160000:162500] 
ch18_Nimagine= ch18[162500:165000] 

ch18_O = ch18[165000:167500]
ch18_Orest= ch18[167500:170000] 
ch18_Oimagine= ch18[170000:172500]

ch18_P = ch18[172500:175000]
ch18_Prest= ch18[175000:177500] 
ch18_Pimagine= ch18[177500:180000]

ch18_Q = ch18[180000:182500]
ch18_Qrest= ch18[182500:185000] 
ch18_Qimagine= ch18[185000:187500]

ch18_R = ch18[187500:190000]
ch18_Rrest= ch18[190000:192500] 
ch18_Rimagine= ch18[192500:195000] 

ch18_S = ch18[195000:197500]
ch18_Srest= ch18[197500:200000] 
ch18_Simagine= ch18[200000:202500]

ch18_T = ch18[202500:205000]
ch18_Trest= ch18[205000:207500] 
ch18_Timagine= ch18[207500:210000]

ch18_U = ch18[210000:212500]
ch18_Urest= ch18[212500:215000] 
ch18_Uimagine= ch18[215000:217500]

ch18_V = ch18[217500:220000]
ch18_Vrest= ch18[220000:222500] 
ch18_Vimagine= ch18[222500:225000] 

ch18_W = ch18[225000:227500]
ch18_Wrest= ch18[227500:230000] 
ch18_Wimagine= ch18[230000:232500]

ch18_X = ch18[232500:235000]
ch18_Xrest= ch18[235000:237500] 
ch18_Ximagine= ch18[237500:240000]

ch18_Y = ch18[240000:242500]
ch18_Yrest= ch18[242500:245000] 
ch18_Yimagine= ch18[245000:247500]

ch18_Z = ch18[247500:250000]
ch18_Zrest= ch18[250000:252500] 
ch18_Zimagine= ch18[252500:255000]



#Channel_19 EVENTS
ch19_eyeopen = ch19[0:30000]
ch19_eyeclosed = ch19[30000:60000]

ch19_A = ch19[60000:62500]
ch19_Arest= ch19[62500:65000] 
ch19_Aimagine= ch19[65000:67500] 

ch19_B = ch19[67500:70000]
ch19_Brest= ch19[70000:72500] 
ch19_Bimagine= ch19[72500:75000] 

ch19_C = ch19[75000:77500]
ch19_Crest= ch19[77500:80000] 
ch19_Cimagine= ch19[80000:82500]

ch19_D = ch19[82500:85000]
ch19_Drest= ch19[85000:87500] 
ch19_Dimagine= ch19[87500:90000]

ch19_E = ch19[90000:92500]
ch19_Erest= ch19[92500:95000] 
ch19_Eimagine= ch19[95000:97500]

ch19_F = ch19[97500:100000]
ch19_Frest= ch19[100000:102500] 
ch19_Fimagine= ch19[102500:105000] 

ch19_G = ch19[105000:107500]
ch19_Grest= ch19[107500:110000] 
ch19_Gimagine= ch19[110000:112500]

ch19_H = ch19[112500:115000]
ch19_Hrest= ch19[115000:117500] 
ch19_Himagine= ch19[117500:120000]

ch19_I = ch19[120000:122500]
ch19_Irest= ch19[122500:125000] 
ch19_Iimagine= ch19[125000:127500]

ch19_J = ch19[127500:130000]
ch19_Jrest= ch19[130000:132500] 
ch19_Jimagine= ch19[132500:135000] 

ch19_K = ch19[135000:137500]
ch19_Krest= ch19[137500:140000] 
ch19_Kimagine= ch19[140000:142500]

ch19_L = ch19[142500:145000]
ch19_Lrest= ch19[145000:147500] 
ch19_Limagine= ch19[147500:150000]

ch19_M = ch19[150000:152500]
ch19_Mrest= ch19[152500:155000] 
ch19_Mimagine= ch19[155000:157500]

ch19_N = ch19[157500:160000]
ch19_Nrest= ch19[160000:162500] 
ch19_Nimagine= ch19[162500:165000] 

ch19_O = ch19[165000:167500]
ch19_Orest= ch19[167500:170000] 
ch19_Oimagine= ch19[170000:172500]

ch19_P = ch19[172500:175000]
ch19_Prest= ch19[175000:177500] 
ch19_Pimagine= ch19[177500:180000]

ch19_Q = ch19[180000:182500]
ch19_Qrest= ch19[182500:185000] 
ch19_Qimagine= ch19[185000:187500]

ch19_R = ch19[187500:190000]
ch19_Rrest= ch19[190000:192500] 
ch19_Rimagine= ch19[192500:195000] 

ch19_S = ch19[195000:197500]
ch19_Srest= ch19[197500:200000] 
ch19_Simagine= ch19[200000:202500]

ch19_T = ch19[202500:205000]
ch19_Trest= ch19[205000:207500] 
ch19_Timagine= ch19[207500:210000]

ch19_U = ch19[210000:212500]
ch19_Urest= ch19[212500:215000] 
ch19_Uimagine= ch19[215000:217500]

ch19_V = ch19[217500:220000]
ch19_Vrest= ch19[220000:222500] 
ch19_Vimagine= ch19[222500:225000] 

ch19_W = ch19[225000:227500]
ch19_Wrest= ch19[227500:230000] 
ch19_Wimagine= ch19[230000:232500]

ch19_X = ch19[232500:235000]
ch19_Xrest= ch19[235000:237500] 
ch19_Ximagine= ch19[237500:240000]

ch19_Y = ch19[240000:242500]
ch19_Yrest= ch19[242500:245000] 
ch19_Yimagine= ch19[245000:247500]

ch19_Z = ch19[247500:250000]
ch19_Zrest= ch19[250000:252500] 
ch19_Zimagine= ch19[252500:255000]



#Channel_20 EVENTS
ch20_eyeopen = ch20[0:30000]
ch20_eyeclosed = ch20[30000:60000]

ch20_A = ch20[60000:62500]
ch20_Arest= ch20[62500:65000] 
ch20_Aimagine= ch20[65000:67500] 

ch20_B = ch20[67500:70000]
ch20_Brest= ch20[70000:72500] 
ch20_Bimagine= ch20[72500:75000] 

ch20_C = ch20[75000:77500]
ch20_Crest= ch20[77500:80000] 
ch20_Cimagine= ch20[80000:82500]

ch20_D = ch20[82500:85000]
ch20_Drest= ch20[85000:87500] 
ch20_Dimagine= ch20[87500:90000]

ch20_E = ch20[90000:92500]
ch20_Erest= ch20[92500:95000] 
ch20_Eimagine= ch20[95000:97500]

ch20_F = ch20[97500:100000]
ch20_Frest= ch20[100000:102500] 
ch20_Fimagine= ch20[102500:105000] 

ch20_G = ch20[105000:107500]
ch20_Grest= ch20[107500:110000] 
ch20_Gimagine= ch20[110000:112500]

ch20_H = ch20[112500:115000]
ch20_Hrest= ch20[115000:117500] 
ch20_Himagine= ch20[117500:120000]

ch20_I = ch20[120000:122500]
ch20_Irest= ch20[122500:125000] 
ch20_Iimagine= ch20[125000:127500]

ch20_J = ch20[127500:130000]
ch20_Jrest= ch20[130000:132500] 
ch20_Jimagine= ch20[132500:135000] 

ch20_K = ch20[135000:137500]
ch20_Krest= ch20[137500:140000] 
ch20_Kimagine= ch20[140000:142500]

ch20_L = ch20[142500:145000]
ch20_Lrest= ch20[145000:147500] 
ch20_Limagine= ch20[147500:150000]

ch20_M = ch20[150000:152500]
ch20_Mrest= ch20[152500:155000] 
ch20_Mimagine= ch20[155000:157500]

ch20_N = ch20[157500:160000]
ch20_Nrest= ch20[160000:162500] 
ch20_Nimagine= ch20[162500:165000] 

ch20_O = ch20[165000:167500]
ch20_Orest= ch20[167500:170000] 
ch20_Oimagine= ch20[170000:172500]

ch20_P = ch20[172500:175000]
ch20_Prest= ch20[175000:177500] 
ch20_Pimagine= ch20[177500:180000]

ch20_Q = ch20[180000:182500]
ch20_Qrest= ch20[182500:185000] 
ch20_Qimagine= ch20[185000:187500]

ch20_R = ch20[187500:190000]
ch20_Rrest= ch20[190000:192500] 
ch20_Rimagine= ch20[192500:195000] 

ch20_S = ch20[195000:197500]
ch20_Srest= ch20[197500:200000] 
ch20_Simagine= ch20[200000:202500]

ch20_T = ch20[202500:205000]
ch20_Trest= ch20[205000:207500] 
ch20_Timagine= ch20[207500:210000]

ch20_U = ch20[210000:212500]
ch20_Urest= ch20[212500:215000] 
ch20_Uimagine= ch20[215000:217500]

ch20_V = ch20[217500:220000]
ch20_Vrest= ch20[220000:222500] 
ch20_Vimagine= ch20[222500:225000] 

ch20_W = ch20[225000:227500]
ch20_Wrest= ch20[227500:230000] 
ch20_Wimagine= ch20[230000:232500]

ch20_X = ch20[232500:235000]
ch20_Xrest= ch20[235000:237500] 
ch20_Ximagine= ch20[237500:240000]

ch20_Y = ch20[240000:242500]
ch20_Yrest= ch20[242500:245000] 
ch20_Yimagine= ch20[245000:247500]

ch20_Z = ch20[247500:250000]
ch20_Zrest= ch20[250000:252500] 
ch20_Zimagine= ch20[252500:255000]


#Channel_21 EVENTS
ch21_eyeopen = ch21[0:30000]
ch21_eyeclosed = ch21[30000:60000]

ch21_A = ch21[60000:62500]
ch21_Arest= ch21[62500:65000] 
ch21_Aimagine= ch21[65000:67500] 

ch21_B = ch21[67500:70000]
ch21_Brest= ch21[70000:72500] 
ch21_Bimagine= ch21[72500:75000] 

ch21_C = ch21[75000:77500]
ch21_Crest= ch21[77500:80000] 
ch21_Cimagine= ch21[80000:82500]

ch21_D = ch21[82500:85000]
ch21_Drest= ch21[85000:87500] 
ch21_Dimagine= ch21[87500:90000]

ch21_E = ch21[90000:92500]
ch21_Erest= ch21[92500:95000] 
ch21_Eimagine= ch21[95000:97500]

ch21_F = ch21[97500:100000]
ch21_Frest= ch21[100000:102500] 
ch21_Fimagine= ch21[102500:105000] 

ch21_G = ch21[105000:107500]
ch21_Grest= ch21[107500:110000] 
ch21_Gimagine= ch21[110000:112500]

ch21_H = ch21[112500:115000]
ch21_Hrest= ch21[115000:117500] 
ch21_Himagine= ch21[117500:120000]

ch21_I = ch21[120000:122500]
ch21_Irest= ch21[122500:125000] 
ch21_Iimagine= ch21[125000:127500]

ch21_J = ch21[127500:130000]
ch21_Jrest= ch21[130000:132500] 
ch21_Jimagine= ch21[132500:135000] 

ch21_K = ch21[135000:137500]
ch21_Krest= ch21[137500:140000] 
ch21_Kimagine= ch21[140000:142500]

ch21_L = ch21[142500:145000]
ch21_Lrest= ch21[145000:147500] 
ch21_Limagine= ch21[147500:150000]

ch21_M = ch21[150000:152500]
ch21_Mrest= ch21[152500:155000] 
ch21_Mimagine= ch21[155000:157500]

ch21_N = ch21[157500:160000]
ch21_Nrest= ch21[160000:162500] 
ch21_Nimagine= ch21[162500:165000] 

ch21_O = ch21[165000:167500]
ch21_Orest= ch21[167500:170000] 
ch21_Oimagine= ch21[170000:172500]

ch21_P = ch21[172500:175000]
ch21_Prest= ch21[175000:177500] 
ch21_Pimagine= ch21[177500:180000]

ch21_Q = ch21[180000:182500]
ch21_Qrest= ch21[182500:185000] 
ch21_Qimagine= ch21[185000:187500]

ch21_R = ch21[187500:190000]
ch21_Rrest= ch21[190000:192500] 
ch21_Rimagine= ch21[192500:195000] 

ch21_S = ch21[195000:197500]
ch21_Srest= ch21[197500:200000] 
ch21_Simagine= ch21[200000:202500]

ch21_T = ch21[202500:205000]
ch21_Trest= ch21[205000:207500] 
ch21_Timagine= ch21[207500:210000]

ch21_U = ch21[210000:212500]
ch21_Urest= ch21[212500:215000] 
ch21_Uimagine= ch21[215000:217500]

ch21_V = ch21[217500:220000]
ch21_Vrest= ch21[220000:222500] 
ch21_Vimagine= ch21[222500:225000] 

ch21_W = ch21[225000:227500]
ch21_Wrest= ch21[227500:230000] 
ch21_Wimagine= ch21[230000:232500]

ch21_X = ch21[232500:235000]
ch21_Xrest= ch21[235000:237500] 
ch21_Ximagine= ch21[237500:240000]

ch21_Y = ch21[240000:242500]
ch21_Yrest= ch21[242500:245000] 
ch21_Yimagine= ch21[245000:247500]

ch21_Z = ch21[247500:250000]
ch21_Zrest= ch21[250000:252500] 
ch21_Zimagine= ch21[252500:255000]


#Channel_22 EVENTS
ch22_eyeopen = ch22[0:30000]
ch22_eyeclosed = ch22[30000:60000]

ch22_A = ch22[60000:62500]
ch22_Arest= ch22[62500:65000] 
ch22_Aimagine= ch22[65000:67500] 

ch22_B = ch22[67500:70000]
ch22_Brest= ch22[70000:72500] 
ch22_Bimagine= ch22[72500:75000] 

ch22_C = ch22[75000:77500]
ch22_Crest= ch22[77500:80000] 
ch22_Cimagine= ch22[80000:82500]

ch22_D = ch22[82500:85000]
ch22_Drest= ch22[85000:87500] 
ch22_Dimagine= ch22[87500:90000]

ch22_E = ch22[90000:92500]
ch22_Erest= ch22[92500:95000] 
ch22_Eimagine= ch22[95000:97500]

ch22_F = ch22[97500:100000]
ch22_Frest= ch22[100000:102500] 
ch22_Fimagine= ch22[102500:105000] 

ch22_G = ch22[105000:107500]
ch22_Grest= ch22[107500:110000] 
ch22_Gimagine= ch22[110000:112500]

ch22_H = ch22[112500:115000]
ch22_Hrest= ch22[115000:117500] 
ch22_Himagine= ch22[117500:120000]

ch22_I = ch22[120000:122500]
ch22_Irest= ch22[122500:125000] 
ch22_Iimagine= ch22[125000:127500]

ch22_J = ch22[127500:130000]
ch22_Jrest= ch22[130000:132500] 
ch22_Jimagine= ch22[132500:135000] 

ch22_K = ch22[135000:137500]
ch22_Krest= ch22[137500:140000] 
ch22_Kimagine= ch22[140000:142500]

ch22_L = ch22[142500:145000]
ch22_Lrest= ch22[145000:147500] 
ch22_Limagine= ch22[147500:150000]

ch22_M = ch22[150000:152500]
ch22_Mrest= ch22[152500:155000] 
ch22_Mimagine= ch22[155000:157500]

ch22_N = ch22[157500:160000]
ch22_Nrest= ch22[160000:162500] 
ch22_Nimagine= ch22[162500:165000] 

ch22_O = ch22[165000:167500]
ch22_Orest= ch22[167500:170000] 
ch22_Oimagine= ch22[170000:172500]

ch22_P = ch22[172500:175000]
ch22_Prest= ch22[175000:177500] 
ch22_Pimagine= ch22[177500:180000]

ch22_Q = ch22[180000:182500]
ch22_Qrest= ch22[182500:185000] 
ch22_Qimagine= ch22[185000:187500]

ch22_R = ch22[187500:190000]
ch22_Rrest= ch22[190000:192500] 
ch22_Rimagine= ch22[192500:195000] 

ch22_S = ch22[195000:197500]
ch22_Srest= ch22[197500:200000] 
ch22_Simagine= ch22[200000:202500]

ch22_T = ch22[202500:205000]
ch22_Trest= ch22[205000:207500] 
ch22_Timagine= ch22[207500:210000]

ch22_U = ch22[210000:212500]
ch22_Urest= ch22[212500:215000] 
ch22_Uimagine= ch22[215000:217500]

ch22_V = ch22[217500:220000]
ch22_Vrest= ch22[220000:222500] 
ch22_Vimagine= ch22[222500:225000] 

ch22_W = ch22[225000:227500]
ch22_Wrest= ch22[227500:230000] 
ch22_Wimagine= ch22[230000:232500]

ch22_X = ch22[232500:235000]
ch22_Xrest= ch22[235000:237500] 
ch22_Ximagine= ch22[237500:240000]

ch22_Y = ch22[240000:242500]
ch22_Yrest= ch22[242500:245000] 
ch22_Yimagine= ch22[245000:247500]

ch22_Z = ch22[247500:250000]
ch22_Zrest= ch22[250000:252500] 
ch22_Zimagine= ch22[252500:255000]



#Channel_23 EVENTS
ch23_eyeopen = ch23[0:30000]
ch23_eyeclosed = ch23[30000:60000]

ch23_A = ch23[60000:62500]
ch23_Arest= ch23[62500:65000] 
ch23_Aimagine= ch23[65000:67500] 

ch23_B = ch23[67500:70000]
ch23_Brest= ch23[70000:72500] 
ch23_Bimagine= ch23[72500:75000] 

ch23_C = ch23[75000:77500]
ch23_Crest= ch23[77500:80000] 
ch23_Cimagine= ch23[80000:82500]

ch23_D = ch23[82500:85000]
ch23_Drest= ch23[85000:87500] 
ch23_Dimagine= ch23[87500:90000]

ch23_E = ch23[90000:92500]
ch23_Erest= ch23[92500:95000] 
ch23_Eimagine= ch23[95000:97500]

ch23_F = ch23[97500:100000]
ch23_Frest= ch23[100000:102500] 
ch23_Fimagine= ch23[102500:105000] 

ch23_G = ch23[105000:107500]
ch23_Grest= ch23[107500:110000] 
ch23_Gimagine= ch23[110000:112500]

ch23_H = ch23[112500:115000]
ch23_Hrest= ch23[115000:117500] 
ch23_Himagine= ch23[117500:120000]

ch23_I = ch23[120000:122500]
ch23_Irest= ch23[122500:125000] 
ch23_Iimagine= ch23[125000:127500]

ch23_J = ch23[127500:130000]
ch23_Jrest= ch23[130000:132500] 
ch23_Jimagine= ch23[132500:135000] 

ch23_K = ch23[135000:137500]
ch23_Krest= ch23[137500:140000] 
ch23_Kimagine= ch23[140000:142500]

ch23_L = ch23[142500:145000]
ch23_Lrest= ch23[145000:147500] 
ch23_Limagine= ch23[147500:150000]

ch23_M = ch23[150000:152500]
ch23_Mrest= ch23[152500:155000] 
ch23_Mimagine= ch23[155000:157500]

ch23_N = ch23[157500:160000]
ch23_Nrest= ch23[160000:162500] 
ch23_Nimagine= ch23[162500:165000] 

ch23_O = ch23[165000:167500]
ch23_Orest= ch23[167500:170000] 
ch23_Oimagine= ch23[170000:172500]

ch23_P = ch23[172500:175000]
ch23_Prest= ch23[175000:177500] 
ch23_Pimagine= ch23[177500:180000]

ch23_Q = ch23[180000:182500]
ch23_Qrest= ch23[182500:185000] 
ch23_Qimagine= ch23[185000:187500]

ch23_R = ch23[187500:190000]
ch23_Rrest= ch23[190000:192500] 
ch23_Rimagine= ch23[192500:195000] 

ch23_S = ch23[195000:197500]
ch23_Srest= ch23[197500:200000] 
ch23_Simagine= ch23[200000:202500]

ch23_T = ch23[202500:205000]
ch23_Trest= ch23[205000:207500] 
ch23_Timagine= ch23[207500:210000]

ch23_U = ch23[210000:212500]
ch23_Urest= ch23[212500:215000] 
ch23_Uimagine= ch23[215000:217500]

ch23_V = ch23[217500:220000]
ch23_Vrest= ch23[220000:222500] 
ch23_Vimagine= ch23[222500:225000] 

ch23_W = ch23[225000:227500]
ch23_Wrest= ch23[227500:230000] 
ch23_Wimagine= ch23[230000:232500]

ch23_X = ch23[232500:235000]
ch23_Xrest= ch23[235000:237500] 
ch23_Ximagine= ch23[237500:240000]

ch23_Y = ch23[240000:242500]
ch23_Yrest= ch23[242500:245000] 
ch23_Yimagine= ch23[245000:247500]

ch23_Z = ch23[247500:250000]
ch23_Zrest= ch23[250000:252500] 
ch23_Zimagine= ch23[252500:255000]



#Channel_24 EVENTS
ch24_eyeopen = ch24[0:30000]
ch24_eyeclosed = ch24[30000:60000]

ch24_A = ch24[60000:62500]
ch24_Arest= ch24[62500:65000] 
ch24_Aimagine= ch24[65000:67500] 

ch24_B = ch24[67500:70000]
ch24_Brest= ch24[70000:72500] 
ch24_Bimagine= ch24[72500:75000] 

ch24_C = ch24[75000:77500]
ch24_Crest= ch24[77500:80000] 
ch24_Cimagine= ch24[80000:82500]

ch24_D = ch24[82500:85000]
ch24_Drest= ch24[85000:87500] 
ch24_Dimagine= ch24[87500:90000]

ch24_E = ch24[90000:92500]
ch24_Erest= ch24[92500:95000] 
ch24_Eimagine= ch24[95000:97500]

ch24_F = ch24[97500:100000]
ch24_Frest= ch24[100000:102500] 
ch24_Fimagine= ch24[102500:105000] 

ch24_G = ch24[105000:107500]
ch24_Grest= ch24[107500:110000] 
ch24_Gimagine= ch24[110000:112500]

ch24_H = ch24[112500:115000]
ch24_Hrest= ch24[115000:117500] 
ch24_Himagine= ch24[117500:120000]

ch24_I = ch24[120000:122500]
ch24_Irest= ch24[122500:125000] 
ch24_Iimagine= ch24[125000:127500]

ch24_J = ch24[127500:130000]
ch24_Jrest= ch24[130000:132500] 
ch24_Jimagine= ch24[132500:135000] 

ch24_K = ch24[135000:137500]
ch24_Krest= ch24[137500:140000] 
ch24_Kimagine= ch24[140000:142500]

ch24_L = ch24[142500:145000]
ch24_Lrest= ch24[145000:147500] 
ch24_Limagine= ch24[147500:150000]

ch24_M = ch24[150000:152500]
ch24_Mrest= ch24[152500:155000] 
ch24_Mimagine= ch24[155000:157500]

ch24_N = ch24[157500:160000]
ch24_Nrest= ch24[160000:162500] 
ch24_Nimagine= ch24[162500:165000] 

ch24_O = ch24[165000:167500]
ch24_Orest= ch24[167500:170000] 
ch24_Oimagine= ch24[170000:172500]

ch24_P = ch24[172500:175000]
ch24_Prest= ch24[175000:177500] 
ch24_Pimagine= ch24[177500:180000]

ch24_Q = ch24[180000:182500]
ch24_Qrest= ch24[182500:185000] 
ch24_Qimagine= ch24[185000:187500]

ch24_R = ch24[187500:190000]
ch24_Rrest= ch24[190000:192500] 
ch24_Rimagine= ch24[192500:195000] 

ch24_S = ch24[195000:197500]
ch24_Srest= ch24[197500:200000] 
ch24_Simagine= ch24[200000:202500]

ch24_T = ch24[202500:205000]
ch24_Trest= ch24[205000:207500] 
ch24_Timagine= ch24[207500:210000]

ch24_U = ch24[210000:212500]
ch24_Urest= ch24[212500:215000] 
ch24_Uimagine= ch24[215000:217500]

ch24_V = ch24[217500:220000]
ch24_Vrest= ch24[220000:222500] 
ch24_Vimagine= ch24[222500:225000] 

ch24_W = ch24[225000:227500]
ch24_Wrest= ch24[227500:230000] 
ch24_Wimagine= ch24[230000:232500]

ch24_X = ch24[232500:235000]
ch24_Xrest= ch24[235000:237500] 
ch24_Ximagine= ch24[237500:240000]

ch24_Y = ch24[240000:242500]
ch24_Yrest= ch24[242500:245000] 
ch24_Yimagine= ch24[245000:247500]

ch24_Z = ch24[247500:250000]
ch24_Zrest= ch24[250000:252500] 
ch24_Zimagine= ch24[252500:255000]



#Channel_25 EVENTS
ch25_eyeopen = ch25[0:30000]
ch25_eyeclosed = ch25[30000:60000]

ch25_A = ch25[60000:62500]
ch25_Arest= ch25[62500:65000] 
ch25_Aimagine= ch25[65000:67500] 

ch25_B = ch25[67500:70000]
ch25_Brest= ch25[70000:72500] 
ch25_Bimagine= ch25[72500:75000] 

ch25_C = ch25[75000:77500]
ch25_Crest= ch25[77500:80000] 
ch25_Cimagine= ch25[80000:82500]

ch25_D = ch25[82500:85000]
ch25_Drest= ch25[85000:87500] 
ch25_Dimagine= ch25[87500:90000]

ch25_E = ch25[90000:92500]
ch25_Erest= ch25[92500:95000] 
ch25_Eimagine= ch25[95000:97500]

ch25_F = ch25[97500:100000]
ch25_Frest= ch25[100000:102500] 
ch25_Fimagine= ch25[102500:105000] 

ch25_G = ch25[105000:107500]
ch25_Grest= ch25[107500:110000] 
ch25_Gimagine= ch25[110000:112500]

ch25_H = ch25[112500:115000]
ch25_Hrest= ch25[115000:117500] 
ch25_Himagine= ch25[117500:120000]

ch25_I = ch25[120000:122500]
ch25_Irest= ch25[122500:125000] 
ch25_Iimagine= ch25[125000:127500]

ch25_J = ch25[127500:130000]
ch25_Jrest= ch25[130000:132500] 
ch25_Jimagine= ch25[132500:135000] 

ch25_K = ch25[135000:137500]
ch25_Krest= ch25[137500:140000] 
ch25_Kimagine= ch25[140000:142500]

ch25_L = ch25[142500:145000]
ch25_Lrest= ch25[145000:147500] 
ch25_Limagine= ch25[147500:150000]

ch25_M = ch25[150000:152500]
ch25_Mrest= ch25[152500:155000] 
ch25_Mimagine= ch25[155000:157500]

ch25_N = ch25[157500:160000]
ch25_Nrest= ch25[160000:162500] 
ch25_Nimagine= ch25[162500:165000] 

ch25_O = ch25[165000:167500]
ch25_Orest= ch25[167500:170000] 
ch25_Oimagine= ch25[170000:172500]

ch25_P = ch25[172500:175000]
ch25_Prest= ch25[175000:177500] 
ch25_Pimagine= ch25[177500:180000]

ch25_Q = ch25[180000:182500]
ch25_Qrest= ch25[182500:185000] 
ch25_Qimagine= ch25[185000:187500]

ch25_R = ch25[187500:190000]
ch25_Rrest= ch25[190000:192500] 
ch25_Rimagine= ch25[192500:195000] 

ch25_S = ch25[195000:197500]
ch25_Srest= ch25[197500:200000] 
ch25_Simagine= ch25[200000:202500]

ch25_T = ch25[202500:205000]
ch25_Trest= ch25[205000:207500] 
ch25_Timagine= ch25[207500:210000]

ch25_U = ch25[210000:212500]
ch25_Urest= ch25[212500:215000] 
ch25_Uimagine= ch25[215000:217500]

ch25_V = ch25[217500:220000]
ch25_Vrest= ch25[220000:222500] 
ch25_Vimagine= ch25[222500:225000] 

ch25_W = ch25[225000:227500]
ch25_Wrest= ch25[227500:230000] 
ch25_Wimagine= ch25[230000:232500]

ch25_X = ch25[232500:235000]
ch25_Xrest= ch25[235000:237500] 
ch25_Ximagine= ch25[237500:240000]

ch25_Y = ch25[240000:242500]
ch25_Yrest= ch25[242500:245000] 
ch25_Yimagine= ch25[245000:247500]

ch25_Z = ch25[247500:250000]
ch25_Zrest= ch25[250000:252500] 
ch25_Zimagine= ch25[252500:255000]



#Channel_26 EVENTS
ch26_eyeopen = ch26[0:30000]
ch26_eyeclosed = ch26[30000:60000]

ch26_A = ch26[60000:62500]
ch26_Arest= ch26[62500:65000] 
ch26_Aimagine= ch26[65000:67500] 

ch26_B = ch26[67500:70000]
ch26_Brest= ch26[70000:72500] 
ch26_Bimagine= ch26[72500:75000] 

ch26_C = ch26[75000:77500]
ch26_Crest= ch26[77500:80000] 
ch26_Cimagine= ch26[80000:82500]

ch26_D = ch26[82500:85000]
ch26_Drest= ch26[85000:87500] 
ch26_Dimagine= ch26[87500:90000]

ch26_E = ch26[90000:92500]
ch26_Erest= ch26[92500:95000] 
ch26_Eimagine= ch26[95000:97500]

ch26_F = ch26[97500:100000]
ch26_Frest= ch26[100000:102500] 
ch26_Fimagine= ch26[102500:105000] 

ch26_G = ch26[105000:107500]
ch26_Grest= ch26[107500:110000] 
ch26_Gimagine= ch26[110000:112500]

ch26_H = ch26[112500:115000]
ch26_Hrest= ch26[115000:117500] 
ch26_Himagine= ch26[117500:120000]

ch26_I = ch26[120000:122500]
ch26_Irest= ch26[122500:125000] 
ch26_Iimagine= ch26[125000:127500]

ch26_J = ch26[127500:130000]
ch26_Jrest= ch26[130000:132500] 
ch26_Jimagine= ch26[132500:135000] 

ch26_K = ch26[135000:137500]
ch26_Krest= ch26[137500:140000] 
ch26_Kimagine= ch26[140000:142500]

ch26_L = ch26[142500:145000]
ch26_Lrest= ch26[145000:147500] 
ch26_Limagine= ch26[147500:150000]

ch26_M = ch26[150000:152500]
ch26_Mrest= ch26[152500:155000] 
ch26_Mimagine= ch26[155000:157500]

ch26_N = ch26[157500:160000]
ch26_Nrest= ch26[160000:162500] 
ch26_Nimagine= ch26[162500:165000] 

ch26_O = ch26[165000:167500]
ch26_Orest= ch26[167500:170000] 
ch26_Oimagine= ch26[170000:172500]

ch26_P = ch26[172500:175000]
ch26_Prest= ch26[175000:177500] 
ch26_Pimagine= ch26[177500:180000]

ch26_Q = ch26[180000:182500]
ch26_Qrest= ch26[182500:185000] 
ch26_Qimagine= ch26[185000:187500]

ch26_R = ch26[187500:190000]
ch26_Rrest= ch26[190000:192500] 
ch26_Rimagine= ch26[192500:195000] 

ch26_S = ch26[195000:197500]
ch26_Srest= ch26[197500:200000] 
ch26_Simagine= ch26[200000:202500]

ch26_T = ch26[202500:205000]
ch26_Trest= ch26[205000:207500] 
ch26_Timagine= ch26[207500:210000]

ch26_U = ch26[210000:212500]
ch26_Urest= ch26[212500:215000] 
ch26_Uimagine= ch26[215000:217500]

ch26_V = ch26[217500:220000]
ch26_Vrest= ch26[220000:222500] 
ch26_Vimagine= ch26[222500:225000] 

ch26_W = ch26[225000:227500]
ch26_Wrest= ch26[227500:230000] 
ch26_Wimagine= ch26[230000:232500]

ch26_X = ch26[232500:235000]
ch26_Xrest= ch26[235000:237500] 
ch26_Ximagine= ch26[237500:240000]

ch26_Y = ch26[240000:242500]
ch26_Yrest= ch26[242500:245000] 
ch26_Yimagine= ch26[245000:247500]

ch26_Z = ch26[247500:250000]
ch26_Zrest= ch26[250000:252500] 
ch26_Zimagine= ch26[252500:255000]



#Channel_27 EVENTS
ch27_eyeopen = ch27[0:30000]
ch27_eyeclosed = ch27[30000:60000]

ch27_A = ch27[60000:62500]
ch27_Arest= ch27[62500:65000] 
ch27_Aimagine= ch27[65000:67500] 

ch27_B = ch27[67500:70000]
ch27_Brest= ch27[70000:72500] 
ch27_Bimagine= ch27[72500:75000] 

ch27_C = ch27[75000:77500]
ch27_Crest= ch27[77500:80000] 
ch27_Cimagine= ch27[80000:82500]

ch27_D = ch27[82500:85000]
ch27_Drest= ch27[85000:87500] 
ch27_Dimagine= ch27[87500:90000]

ch27_E = ch27[90000:92500]
ch27_Erest= ch27[92500:95000] 
ch27_Eimagine= ch27[95000:97500]

ch27_F = ch27[97500:100000]
ch27_Frest= ch27[100000:102500] 
ch27_Fimagine= ch27[102500:105000] 

ch27_G = ch27[105000:107500]
ch27_Grest= ch27[107500:110000] 
ch27_Gimagine= ch27[110000:112500]

ch27_H = ch27[112500:115000]
ch27_Hrest= ch27[115000:117500] 
ch27_Himagine= ch27[117500:120000]

ch27_I = ch27[120000:122500]
ch27_Irest= ch27[122500:125000] 
ch27_Iimagine= ch27[125000:127500]

ch27_J = ch27[127500:130000]
ch27_Jrest= ch27[130000:132500] 
ch27_Jimagine= ch27[132500:135000] 

ch27_K = ch27[135000:137500]
ch27_Krest= ch27[137500:140000] 
ch27_Kimagine= ch27[140000:142500]

ch27_L = ch27[142500:145000]
ch27_Lrest= ch27[145000:147500] 
ch27_Limagine= ch27[147500:150000]

ch27_M = ch27[150000:152500]
ch27_Mrest= ch27[152500:155000] 
ch27_Mimagine= ch27[155000:157500]

ch27_N = ch27[157500:160000]
ch27_Nrest= ch27[160000:162500] 
ch27_Nimagine= ch27[162500:165000] 

ch27_O = ch27[165000:167500]
ch27_Orest= ch27[167500:170000] 
ch27_Oimagine= ch27[170000:172500]

ch27_P = ch27[172500:175000]
ch27_Prest= ch27[175000:177500] 
ch27_Pimagine= ch27[177500:180000]

ch27_Q = ch27[180000:182500]
ch27_Qrest= ch27[182500:185000] 
ch27_Qimagine= ch27[185000:187500]

ch27_R = ch27[187500:190000]
ch27_Rrest= ch27[190000:192500] 
ch27_Rimagine= ch27[192500:195000] 

ch27_S = ch27[195000:197500]
ch27_Srest= ch27[197500:200000] 
ch27_Simagine= ch27[200000:202500]

ch27_T = ch27[202500:205000]
ch27_Trest= ch27[205000:207500] 
ch27_Timagine= ch27[207500:210000]

ch27_U = ch27[210000:212500]
ch27_Urest= ch27[212500:215000] 
ch27_Uimagine= ch27[215000:217500]

ch27_V = ch27[217500:220000]
ch27_Vrest= ch27[220000:222500] 
ch27_Vimagine= ch27[222500:225000] 

ch27_W = ch27[225000:227500]
ch27_Wrest= ch27[227500:230000] 
ch27_Wimagine= ch27[230000:232500]

ch27_X = ch27[232500:235000]
ch27_Xrest= ch27[235000:237500] 
ch27_Ximagine= ch27[237500:240000]

ch27_Y = ch27[240000:242500]
ch27_Yrest= ch27[242500:245000] 
ch27_Yimagine= ch27[245000:247500]

ch27_Z = ch27[247500:250000]
ch27_Zrest= ch27[250000:252500] 
ch27_Zimagine= ch27[252500:255000]


#Channel_28 EVENTS
ch28_eyeopen = ch28[0:30000]
ch28_eyeclosed = ch28[30000:60000]

ch28_A = ch28[60000:62500]
ch28_Arest= ch28[62500:65000] 
ch28_Aimagine= ch28[65000:67500] 

ch28_B = ch28[67500:70000]
ch28_Brest= ch28[70000:72500] 
ch28_Bimagine= ch28[72500:75000] 

ch28_C = ch28[75000:77500]
ch28_Crest= ch28[77500:80000] 
ch28_Cimagine= ch28[80000:82500]

ch28_D = ch28[82500:85000]
ch28_Drest= ch28[85000:87500] 
ch28_Dimagine= ch28[87500:90000]

ch28_E = ch28[90000:92500]
ch28_Erest= ch28[92500:95000] 
ch28_Eimagine= ch28[95000:97500]

ch28_F = ch28[97500:100000]
ch28_Frest= ch28[100000:102500] 
ch28_Fimagine= ch28[102500:105000] 

ch28_G = ch28[105000:107500]
ch28_Grest= ch28[107500:110000] 
ch28_Gimagine= ch28[110000:112500]

ch28_H = ch28[112500:115000]
ch28_Hrest= ch28[115000:117500] 
ch28_Himagine= ch28[117500:120000]

ch28_I = ch28[120000:122500]
ch28_Irest= ch28[122500:125000] 
ch28_Iimagine= ch28[125000:127500]

ch28_J = ch28[127500:130000]
ch28_Jrest= ch28[130000:132500] 
ch28_Jimagine= ch28[132500:135000] 

ch28_K = ch28[135000:137500]
ch28_Krest= ch28[137500:140000] 
ch28_Kimagine= ch28[140000:142500]

ch28_L = ch28[142500:145000]
ch28_Lrest= ch28[145000:147500] 
ch28_Limagine= ch28[147500:150000]

ch28_M = ch28[150000:152500]
ch28_Mrest= ch28[152500:155000] 
ch28_Mimagine= ch28[155000:157500]

ch28_N = ch28[157500:160000]
ch28_Nrest= ch28[160000:162500] 
ch28_Nimagine= ch28[162500:165000] 

ch28_O = ch28[165000:167500]
ch28_Orest= ch28[167500:170000] 
ch28_Oimagine= ch28[170000:172500]

ch28_P = ch28[172500:175000]
ch28_Prest= ch28[175000:177500] 
ch28_Pimagine= ch28[177500:180000]

ch28_Q = ch28[180000:182500]
ch28_Qrest= ch28[182500:185000] 
ch28_Qimagine= ch28[185000:187500]

ch28_R = ch28[187500:190000]
ch28_Rrest= ch28[190000:192500] 
ch28_Rimagine= ch28[192500:195000] 

ch28_S = ch28[195000:197500]
ch28_Srest= ch28[197500:200000] 
ch28_Simagine= ch28[200000:202500]

ch28_T = ch28[202500:205000]
ch28_Trest= ch28[205000:207500] 
ch28_Timagine= ch28[207500:210000]

ch28_U = ch28[210000:212500]
ch28_Urest= ch28[212500:215000] 
ch28_Uimagine= ch28[215000:217500]

ch28_V = ch28[217500:220000]
ch28_Vrest= ch28[220000:222500] 
ch28_Vimagine= ch28[222500:225000] 

ch28_W = ch28[225000:227500]
ch28_Wrest= ch28[227500:230000] 
ch28_Wimagine= ch28[230000:232500]

ch28_X = ch28[232500:235000]
ch28_Xrest= ch28[235000:237500] 
ch28_Ximagine= ch28[237500:240000]

ch28_Y = ch28[240000:242500]
ch28_Yrest= ch28[242500:245000] 
ch28_Yimagine= ch28[245000:247500]

ch28_Z = ch28[247500:250000]
ch28_Zrest= ch28[250000:252500] 
ch28_Zimagine= ch28[252500:255000]


#Channel_29 EVENTS
ch29_eyeopen = ch29[0:30000]
ch29_eyeclosed = ch29[30000:60000]

ch29_A = ch29[60000:62500]
ch29_Arest= ch29[62500:65000] 
ch29_Aimagine= ch29[65000:67500] 

ch29_B = ch29[67500:70000]
ch29_Brest= ch29[70000:72500] 
ch29_Bimagine= ch29[72500:75000] 

ch29_C = ch29[75000:77500]
ch29_Crest= ch29[77500:80000] 
ch29_Cimagine= ch29[80000:82500]

ch29_D = ch29[82500:85000]
ch29_Drest= ch29[85000:87500] 
ch29_Dimagine= ch29[87500:90000]

ch29_E = ch29[90000:92500]
ch29_Erest= ch29[92500:95000] 
ch29_Eimagine= ch29[95000:97500]

ch29_F = ch29[97500:100000]
ch29_Frest= ch29[100000:102500] 
ch29_Fimagine= ch29[102500:105000] 

ch29_G = ch29[105000:107500]
ch29_Grest= ch29[107500:110000] 
ch29_Gimagine= ch29[110000:112500]

ch29_H = ch29[112500:115000]
ch29_Hrest= ch29[115000:117500] 
ch29_Himagine= ch29[117500:120000]

ch29_I = ch29[120000:122500]
ch29_Irest= ch29[122500:125000] 
ch29_Iimagine= ch29[125000:127500]

ch29_J = ch29[127500:130000]
ch29_Jrest= ch29[130000:132500] 
ch29_Jimagine= ch29[132500:135000] 

ch29_K = ch29[135000:137500]
ch29_Krest= ch29[137500:140000] 
ch29_Kimagine= ch29[140000:142500]

ch29_L = ch29[142500:145000]
ch29_Lrest= ch29[145000:147500] 
ch29_Limagine= ch29[147500:150000]

ch29_M = ch29[150000:152500]
ch29_Mrest= ch29[152500:155000] 
ch29_Mimagine= ch29[155000:157500]

ch29_N = ch29[157500:160000]
ch29_Nrest= ch29[160000:162500] 
ch29_Nimagine= ch29[162500:165000] 

ch29_O = ch29[165000:167500]
ch29_Orest= ch29[167500:170000] 
ch29_Oimagine= ch29[170000:172500]

ch29_P = ch29[172500:175000]
ch29_Prest= ch29[175000:177500] 
ch29_Pimagine= ch29[177500:180000]

ch29_Q = ch29[180000:182500]
ch29_Qrest= ch29[182500:185000] 
ch29_Qimagine= ch29[185000:187500]

ch29_R = ch29[187500:190000]
ch29_Rrest= ch29[190000:192500] 
ch29_Rimagine= ch29[192500:195000] 

ch29_S = ch29[195000:197500]
ch29_Srest= ch29[197500:200000] 
ch29_Simagine= ch29[200000:202500]

ch29_T = ch29[202500:205000]
ch29_Trest= ch29[205000:207500] 
ch29_Timagine= ch29[207500:210000]

ch29_U = ch29[210000:212500]
ch29_Urest= ch29[212500:215000] 
ch29_Uimagine= ch29[215000:217500]

ch29_V = ch29[217500:220000]
ch29_Vrest= ch29[220000:222500] 
ch29_Vimagine= ch29[222500:225000] 

ch29_W = ch29[225000:227500]
ch29_Wrest= ch29[227500:230000] 
ch29_Wimagine= ch29[230000:232500]

ch29_X = ch29[232500:235000]
ch29_Xrest= ch29[235000:237500] 
ch29_Ximagine= ch29[237500:240000]

ch29_Y = ch29[240000:242500]
ch29_Yrest= ch29[242500:245000] 
ch29_Yimagine= ch29[245000:247500]

ch29_Z = ch29[247500:250000]
ch29_Zrest= ch29[250000:252500] 
ch29_Zimagine= ch29[252500:255000]



#Channel_30 EVENTS
ch30_eyeopen = ch30[0:30000]
ch30_eyeclosed = ch30[30000:60000]

ch30_A = ch30[60000:62500]
ch30_Arest= ch30[62500:65000] 
ch30_Aimagine= ch30[65000:67500] 

ch30_B = ch30[67500:70000]
ch30_Brest= ch30[70000:72500] 
ch30_Bimagine= ch30[72500:75000] 

ch30_C = ch30[75000:77500]
ch30_Crest= ch30[77500:80000] 
ch30_Cimagine= ch30[80000:82500]

ch30_D = ch30[82500:85000]
ch30_Drest= ch30[85000:87500] 
ch30_Dimagine= ch30[87500:90000]

ch30_E = ch30[90000:92500]
ch30_Erest= ch30[92500:95000] 
ch30_Eimagine= ch30[95000:97500]

ch30_F = ch30[97500:100000]
ch30_Frest= ch30[100000:102500] 
ch30_Fimagine= ch30[102500:105000] 

ch30_G = ch30[105000:107500]
ch30_Grest= ch30[107500:110000] 
ch30_Gimagine= ch30[110000:112500]

ch30_H = ch30[112500:115000]
ch30_Hrest= ch30[115000:117500] 
ch30_Himagine= ch30[117500:120000]

ch30_I = ch30[120000:122500]
ch30_Irest= ch30[122500:125000] 
ch30_Iimagine= ch30[125000:127500]

ch30_J = ch30[127500:130000]
ch30_Jrest= ch30[130000:132500] 
ch30_Jimagine= ch30[132500:135000] 

ch30_K = ch30[135000:137500]
ch30_Krest= ch30[137500:140000] 
ch30_Kimagine= ch30[140000:142500]

ch30_L = ch30[142500:145000]
ch30_Lrest= ch30[145000:147500] 
ch30_Limagine= ch30[147500:150000]

ch30_M = ch30[150000:152500]
ch30_Mrest= ch30[152500:155000] 
ch30_Mimagine= ch30[155000:157500]

ch30_N = ch30[157500:160000]
ch30_Nrest= ch30[160000:162500] 
ch30_Nimagine= ch30[162500:165000] 

ch30_O = ch30[165000:167500]
ch30_Orest= ch30[167500:170000] 
ch30_Oimagine= ch30[170000:172500]

ch30_P = ch30[172500:175000]
ch30_Prest= ch30[175000:177500] 
ch30_Pimagine= ch30[177500:180000]

ch30_Q = ch30[180000:182500]
ch30_Qrest= ch30[182500:185000] 
ch30_Qimagine= ch30[185000:187500]

ch30_R = ch30[187500:190000]
ch30_Rrest= ch30[190000:192500] 
ch30_Rimagine= ch30[192500:195000] 

ch30_S = ch30[195000:197500]
ch30_Srest= ch30[197500:200000] 
ch30_Simagine= ch30[200000:202500]

ch30_T = ch30[202500:205000]
ch30_Trest= ch30[205000:207500] 
ch30_Timagine= ch30[207500:210000]

ch30_U = ch30[210000:212500]
ch30_Urest= ch30[212500:215000] 
ch30_Uimagine= ch30[215000:217500]

ch30_V = ch30[217500:220000]
ch30_Vrest= ch30[220000:222500] 
ch30_Vimagine= ch30[222500:225000] 

ch30_W = ch30[225000:227500]
ch30_Wrest= ch30[227500:230000] 
ch30_Wimagine= ch30[230000:232500]

ch30_X = ch30[232500:235000]
ch30_Xrest= ch30[235000:237500] 
ch30_Ximagine= ch30[237500:240000]

ch30_Y = ch30[240000:242500]
ch30_Yrest= ch30[242500:245000] 
ch30_Yimagine= ch30[245000:247500]

ch30_Z = ch30[247500:250000]
ch30_Zrest= ch30[250000:252500] 
ch30_Zimagine= ch30[252500:255000]




#Channel_31 EVENTS
ch31_eyeopen = ch31[0:30000]
ch31_eyeclosed = ch31[30000:60000]

ch31_A = ch31[60000:62500]
ch31_Arest= ch31[62500:65000] 
ch31_Aimagine= ch31[65000:67500] 

ch31_B = ch31[67500:70000]
ch31_Brest= ch31[70000:72500] 
ch31_Bimagine= ch31[72500:75000] 

ch31_C = ch31[75000:77500]
ch31_Crest= ch31[77500:80000] 
ch31_Cimagine= ch31[80000:82500]

ch31_D = ch31[82500:85000]
ch31_Drest= ch31[85000:87500] 
ch31_Dimagine= ch31[87500:90000]

ch31_E = ch31[90000:92500]
ch31_Erest= ch31[92500:95000] 
ch31_Eimagine= ch31[95000:97500]

ch31_F = ch31[97500:100000]
ch31_Frest= ch31[100000:102500] 
ch31_Fimagine= ch31[102500:105000] 

ch31_G = ch31[105000:107500]
ch31_Grest= ch31[107500:110000] 
ch31_Gimagine= ch31[110000:112500]

ch31_H = ch31[112500:115000]
ch31_Hrest= ch31[115000:117500] 
ch31_Himagine= ch31[117500:120000]

ch31_I = ch31[120000:122500]
ch31_Irest= ch31[122500:125000] 
ch31_Iimagine= ch31[125000:127500]

ch31_J = ch31[127500:130000]
ch31_Jrest= ch31[130000:132500] 
ch31_Jimagine= ch31[132500:135000] 

ch31_K = ch31[135000:137500]
ch31_Krest= ch31[137500:140000] 
ch31_Kimagine= ch31[140000:142500]

ch31_L = ch31[142500:145000]
ch31_Lrest= ch31[145000:147500] 
ch31_Limagine= ch31[147500:150000]

ch31_M = ch31[150000:152500]
ch31_Mrest= ch31[152500:155000] 
ch31_Mimagine= ch31[155000:157500]

ch31_N = ch31[157500:160000]
ch31_Nrest= ch31[160000:162500] 
ch31_Nimagine= ch31[162500:165000] 

ch31_O = ch31[165000:167500]
ch31_Orest= ch31[167500:170000] 
ch31_Oimagine= ch31[170000:172500]

ch31_P = ch31[172500:175000]
ch31_Prest= ch31[175000:177500] 
ch31_Pimagine= ch31[177500:180000]

ch31_Q = ch31[180000:182500]
ch31_Qrest= ch31[182500:185000] 
ch31_Qimagine= ch31[185000:187500]

ch31_R = ch31[187500:190000]
ch31_Rrest= ch31[190000:192500] 
ch31_Rimagine= ch31[192500:195000] 

ch31_S = ch31[195000:197500]
ch31_Srest= ch31[197500:200000] 
ch31_Simagine= ch31[200000:202500]

ch31_T = ch31[202500:205000]
ch31_Trest= ch31[205000:207500] 
ch31_Timagine= ch31[207500:210000]

ch31_U = ch31[210000:212500]
ch31_Urest= ch31[212500:215000] 
ch31_Uimagine= ch31[215000:217500]

ch31_V = ch31[217500:220000]
ch31_Vrest= ch31[220000:222500] 
ch31_Vimagine= ch31[222500:225000] 

ch31_W = ch31[225000:227500]
ch31_Wrest= ch31[227500:230000] 
ch31_Wimagine= ch31[230000:232500]

ch31_X = ch31[232500:235000]
ch31_Xrest= ch31[235000:237500] 
ch31_Ximagine= ch31[237500:240000]

ch31_Y = ch31[240000:242500]
ch31_Yrest= ch31[242500:245000] 
ch31_Yimagine= ch31[245000:247500]

ch31_Z = ch31[247500:250000]
ch31_Zrest= ch31[250000:252500] 
ch31_Zimagine= ch31[252500:255000]


#Channel_32 EVENTS
ch32_eyeopen = ch32[0:30000]
ch32_eyeclosed = ch32[30000:60000]

ch32_A = ch32[60000:62500]
ch32_Arest= ch32[62500:65000] 
ch32_Aimagine= ch32[65000:67500] 

ch32_B = ch32[67500:70000]
ch32_Brest= ch32[70000:72500] 
ch32_Bimagine= ch32[72500:75000] 

ch32_C = ch32[75000:77500]
ch32_Crest= ch32[77500:80000] 
ch32_Cimagine= ch32[80000:82500]

ch32_D = ch32[82500:85000]
ch32_Drest= ch32[85000:87500] 
ch32_Dimagine= ch32[87500:90000]

ch32_E = ch32[90000:92500]
ch32_Erest= ch32[92500:95000] 
ch32_Eimagine= ch32[95000:97500]

ch32_F = ch32[97500:100000]
ch32_Frest= ch32[100000:102500] 
ch32_Fimagine= ch32[102500:105000] 

ch32_G = ch32[105000:107500]
ch32_Grest= ch32[107500:110000] 
ch32_Gimagine= ch32[110000:112500]

ch32_H = ch32[112500:115000]
ch32_Hrest= ch32[115000:117500] 
ch32_Himagine= ch32[117500:120000]

ch32_I = ch32[120000:122500]
ch32_Irest= ch32[122500:125000] 
ch32_Iimagine= ch32[125000:127500]

ch32_J = ch32[127500:130000]
ch32_Jrest= ch32[130000:132500] 
ch32_Jimagine= ch32[132500:135000] 

ch32_K = ch32[135000:137500]
ch32_Krest= ch32[137500:140000] 
ch32_Kimagine= ch32[140000:142500]

ch32_L = ch32[142500:145000]
ch32_Lrest= ch32[145000:147500] 
ch32_Limagine= ch32[147500:150000]

ch32_M = ch32[150000:152500]
ch32_Mrest= ch32[152500:155000] 
ch32_Mimagine= ch32[155000:157500]

ch32_N = ch32[157500:160000]
ch32_Nrest= ch32[160000:162500] 
ch32_Nimagine= ch32[162500:165000] 

ch32_O = ch32[165000:167500]
ch32_Orest= ch32[167500:170000] 
ch32_Oimagine= ch32[170000:172500]

ch32_P = ch32[172500:175000]
ch32_Prest= ch32[175000:177500] 
ch32_Pimagine= ch32[177500:180000]

ch32_Q = ch32[180000:182500]
ch32_Qrest= ch32[182500:185000] 
ch32_Qimagine= ch32[185000:187500]

ch32_R = ch32[187500:190000]
ch32_Rrest= ch32[190000:192500] 
ch32_Rimagine= ch32[192500:195000] 

ch32_S = ch32[195000:197500]
ch32_Srest= ch32[197500:200000] 
ch32_Simagine= ch32[200000:202500]

ch32_T = ch32[202500:205000]
ch32_Trest= ch32[205000:207500] 
ch32_Timagine= ch32[207500:210000]

ch32_U = ch32[210000:212500]
ch32_Urest= ch32[212500:215000] 
ch32_Uimagine= ch32[215000:217500]

ch32_V = ch32[217500:220000]
ch32_Vrest= ch32[220000:222500] 
ch32_Vimagine= ch32[222500:225000] 

ch32_W = ch32[225000:227500]
ch32_Wrest= ch32[227500:230000] 
ch32_Wimagine= ch32[230000:232500]

ch32_X = ch32[232500:235000]
ch32_Xrest= ch32[235000:237500] 
ch32_Ximagine= ch32[237500:240000]

ch32_Y = ch32[240000:242500]
ch32_Yrest= ch32[242500:245000] 
ch32_Yimagine= ch32[245000:247500]

ch32_Z = ch32[247500:250000]
ch32_Zrest= ch32[250000:252500] 
ch32_Zimagine= ch32[252500:255000]


















































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































