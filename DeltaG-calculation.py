import sys

#check command lines arguments
if len(sys.argv)!=6 :
    print("Number of input parameters not correct. Usage: ./DeltaG-calculation.py osmolyte-type osmolyte-concentration T-value T-approach P"); exit(1)
  
print("Computes transfer free energies that describe the transfer of a protein from water at 298 K and 1 bar to different osmolyte solutions, at any temperature (in K) and pressure (in bar) value. \n")

os = str(sys.argv[1]) #name of osmolyte
c = float(sys.argv[2]) #concentration of osmolyte, in M
T = float(sys.argv[3]) #temperature, in K
T_approach = int(sys.argv[4]) #temperature approach, either 2 or 3
P = float(sys.argv[5]) #pressure, in bar

if os not in ['sucrose', 'urea', 'TMAO', 'proline', 'betaine', 'none']:
	raise Exception("Unknown osmolyte type. Allowed types are: sucrose, urea, TMAO, proline, betaine or none")

if T_approach not in [2, 3]:
	raise Exception("Unknown T-approach type. Allowed types are: 2, 3")

if T<0:
	raise Exception("T value must be in K")

#input free energy of transfer data for osmolytes, in kJ/mol/M. From Auton and Bolen papers. Order is: ALA, ARG, ASN, ASP, CYS, GLN, GLU, GLY, HIS, ILE, LEU, LYS, MET, PHE, PRO, SER, THR, TRP, TYR, VAL, BACKBONE. Data are for 1M osmolytes

if os == 'sucrose':
	osTFE = [0.092, -0.332, -0.118, -0.156, 0, -0.171, -0.174, 0, -0.496, 0.118, 0.155, -0.166, -0.028, -0.403, -0.306, -0.012, 0.087, -0.901, -0.328, 0.142, 0.259]

if os == 'urea':
	osTFE = [0.003, 0.080, 0.0062, 0.183, 0, -0.061, 0.171, 0, -0.043, 0.008, -0.060, 0.073, -0.034, -0.179, 0.095, 0.082, 0.076, -0.423, -0.020, 0.078, -0.163]
	
if os == 'betaine': 
	osTFE = [0.020, -0.458, 0.139, -0.488, 0, 0.032, -0.469, 0, -0.150, -0.005, -0.074, -0.720, -0.059, -0.472, -0.524, -0.175, 0.001, -1.548, -0.892, -0.082, 0.280]

if os == 'proline': 
	osTFE = [-0.0003, -0.252, -0.074, -0.379, 0, -0.135, -0.373, 0, -0.189, -0.011, 0.020, -0.250, -0.147, -0.298, -0.268, -0.140, -0.077, -0.830, -0.579, 0.033, 0.201]
	
if os == 'TMAO': 	
	osTFE = [-0.061, -0.457, 0.233, -0.279, 0, 0.173, -0.348, 0, 0.176, -0.106, 0.049, -0.461, -0.032, -0.039, -0.576, -0.163, 0.015, -0.640, -0.478, -0.004, 0.377]

if os == 'none': 	
	osTFE = [0]*21

#input free energy of transfer data for temperature, in kJ/mol. From Arsiccio and Shea, J. Phys. Chem. B 2021, 125, 20, 5222-5232. Order is: ALA, ARG, ASN, ASP, CYS, GLN, GLU, GLY, HIS, ILE, LEU, LYS, MET, PHE, PRO, SER, THR, TRP, TYR, VAL, BACKBONE.

T_TFE = []

#approach 2
if (T_approach == 2 and T != 298):
	T_TFE.append(-2.995/1000*T**2+1.808*T-272.895)
	T_TFE.append(-3.182/1000*T**2+1.894*T-282.032)
	T_TFE.append(-1.047/1000*T**2+0.6068*T-87.846)
	T_TFE.append(-0.1794/1000*T**2+0.1091*T-16.526)
	T_TFE.append(-3.09/1000*T**2+1.835*T-272.26)
	T_TFE.append(-2.23/1000*T**2+1.335*T-199.707)
	T_TFE.append(-1.511/1000*T**2+0.8904*T-131.168)
	T_TFE.append(0)
	T_TFE.append(-3.482/1000*T**2+2.084*T-311.694)
	T_TFE.append(-6.364/1000*T**2+3.8*T-567.444)
	T_TFE.append(-7.466/1000*T**2+4.417*T-653.394)
	T_TFE.append(-2.091/1000*T**2+1.2458*T-185.549)
	T_TFE.append(-3.807/1000*T**2+2.272*T-339.007)
	T_TFE.append(-7.828/1000*T**2+4.644*T-688.874)
	T_TFE.append(-2.347/1000*T**2+1.411*T-212.059)
	T_TFE.append(1.813/1000*T**2-1.05*T+151.957)
	T_TFE.append(-2.64/1000*T**2+1.591*T-239.516)
	T_TFE.append(-11.66/1000*T**2+6.916*T-1025.293)
	T_TFE.append(-7.513/1000*T**2+4.478*T-667.261)
	T_TFE.append(-4.902/1000*T**2+2.921*T-435.309)
	T_TFE.append(-0.6962/1000*T**2+0.4426*T-70.015)

if (T_approach == 2 and T == 298):
	T_TFE = [0]*21
	
#approach 3
if (T_approach == 3):
	T_TFE.append(-2.995/1000*T**2+1.808*T-272.105)
	T_TFE.append(-3.182/1000*T**2+1.894*T-284.086)
	T_TFE.append(-1.047/1000*T**2+0.6068*T-90.597)
	T_TFE.append(-0.1794/1000*T**2+0.1091*T-19.143)
	T_TFE.append(-3.09/1000*T**2+1.835*T-268.527)
	T_TFE.append(-2.23/1000*T**2+1.335*T-201.559)
	T_TFE.append(-1.511/1000*T**2+0.8904*T-133.543)
	T_TFE.append(0)
	T_TFE.append(-3.482/1000*T**2+2.084*T-315.398)
	T_TFE.append(-6.364/1000*T**2+3.8*T-564.825)
	T_TFE.append(-7.466/1000*T**2+4.417*T-651.483)
	T_TFE.append(-2.091/1000*T**2+1.2458*T-187.485)
	T_TFE.append(-3.807/1000*T**2+2.272*T-339.242)
	T_TFE.append(-7.828/1000*T**2+4.644*T-687.134)
	T_TFE.append(-2.347/1000*T**2+1.411*T-214.211)
	T_TFE.append(1.813/1000*T**2-1.05*T+150.289)
	T_TFE.append(-2.64/1000*T**2+1.591*T-240.267)
	T_TFE.append(-11.66/1000*T**2+6.916*T-1024.284)
	T_TFE.append(-7.513/1000*T**2+4.478*T-666.484)
	T_TFE.append(-4.902/1000*T**2+2.921*T-433.013)
	T_TFE.append(-0.6927/1000*T**2+0.4404*T-68.724)


#input free energy of transfer data for pressure, in kJ/mol. From Arsiccio and Shea, J. Phys. Chem. B 2021, 125, 30, 8431-8442. Order is: ALA, ARG, ASN, ASP, CYS, GLN, GLU, GLY, HIS, ILE, LEU, LYS, MET, PHE, PRO, SER, THR, TRP, TYR, VAL, BACKBONE.
DeltaP = P-1

P_TFE = []
#protein contribution
#difference in bulk and surface volume, cm3/mol
DeltaV = [-1.6, 0, 1.3, 0, -0.199999999999999, -0.799999999999997, 0, 0, -0.600000000000001, -4.09999999999999, -5.60000000000001, 0, -1.4, -3.40000000000001, -1, 0.799999999999997, 0.5, -4, -3.40000000000001, -2.90000000000001, 1]

#apparent compressibility of exposed groups, cm3/mol/bar
Ks = [0.0002, 0, -0.00033, 0, -0.00049, -0.0001, 0, 0, 0.00018, -8E-05, 4E-05, 0, -0.00014, 0.00024, -0.0004, -0.00013, -0.00022, 0.00038, -0.00022, 6E-05, -0.00011]

#apparent compressibility of buried groups, cm3/mol/bar
Km = [0.00039, 0, 0.00088, 0, 0.00074, 0.00125, 0, 0, 0.00141, 0.00149, 0.0015, 0, 0.00154, 0.00191, 0.00087, 0.00045, 0.00084, 0.00245, 0.00197, 0.00112, 0.00096]

for count, element in enumerate(DeltaV):
	P_TFE.append(-element*DeltaP*10**-4-1/2*(Ks[count]-Km[count])*DeltaP**2*10**-4)
	
P_TFE[-1] -= 1/6*(8.3*10**-7+2.6*10**-7)*DeltaP**3*10**-4

#add the water term
R = 0.008314 #kJ/mol/K
T_p = 298 #K
#difference in bulk and surface volume, cm3/mol
DeltaVw = [-25.722944, -77.598144, -44.827328, -42.287232, -37.02816, -55.595904, -53.091584, 0, -57.992896, -53.699776, -56.454528, -66.936896, -58.958848, -65.970944, -39.71136, -30.695808, -40.999296, -81.891264, -70.872256, -45.936384, -14.7450784]

#difference in compressibility, cm3/mol/bar
DeltaKw = [-0.0031870727616, -0.0096144100416, -0.0055541059392, -0.0052393880448, -0.004587789024, -0.0068883325056, -0.0065780472576, 0, -0.0071853198144, -0.0066534022464, -0.0069947160192, -0.0082934814144, -0.0073050012672, -0.0081737999616, -0.004920237504, -0.0038032106112, -0.0050798127744, -0.0101463276096, -0.0087810725184, -0.0056915179776, -0.00182691521376]

#SASA_max, A2
SASA_max = [71.9, 216.9, 125.3, 118.2, 103.5, 155.4, 148.4, 0, 162.1, 150.1, 157.8, 187.1, 164.8, 184.4, 111, 85.8, 114.6, 228.9, 198.1, 128.4, 41.215]

for count, element in enumerate(DeltaVw):
	P_TFE[count] += element*DeltaP*10**-4-1/2*DeltaKw[count]*DeltaP**2*10**-4+R*T_p*SASA_max[count]*1.4*(1/(24.5-24.5*0.348*DeltaP*10**-4)-1/24.5)
	

#Sum the different contributions: osmolyte, temperature and pressure
TFE = []
for count, element in enumerate(osTFE):
    TFE.append(element*c+T_TFE[count]+P_TFE[count])
    
#write output file
RES = ['ALA', 'ARG', 'ASN', 'ASP', 'CYS', 'GLN', 'GLU', 'GLY', 'HIS', 'ILE', 'LEU', 'LYS', 'MET', 'PHE', 'PRO', 'SER', 'THR', 'TRP', 'TYR', 'VAL', 'BACKBONE']
with open('DeltaG.dat', 'w') as f:
     for count, element in enumerate(RES):
         f.write("%s %s\n" %(element, TFE[count]))
